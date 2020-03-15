import os

from pathlib import Path
from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

# from src.utilities.database.query import QueryEtlConfig
from src.utilities.database.query import QueryExtractedMovies

from src.utilities.database.insert import InsertTransformedMovies

from src.utilities.scan import ScanForMovies
from src.utilities.transform import TransformMovies
from src.utilities.load import LoadMovies

from src.utilities.api.methods import AllowedMethods

class Movies:

    movies = Blueprint('movies', __name__)

    @staticmethod
    @movies.route('/queue', methods=[AllowedMethods.GET])
    def queue():
        """Returns a rendered template view off all new items in the queue"""
        movies = QueryExtractedMovies.get_full_results()
        return render_template('queue.html', records=movies)

    @staticmethod
    @movies.route('/scan', methods=[AllowedMethods.POST])
    def scan():
        if ScanForMovies.start():
            return redirect(url_for('movies.queue'))

    @staticmethod
    @movies.route('/update-parsed-data', methods=[AllowedMethods.POST])
    def update_parsed_data():
        if request.form:
            InsertTransformedMovies.process_merge(
                id=request.form.get('id'),
                raw_torrent_name=request.form.get('raw_torrent_name'),
                parsed_title=request.form.get('parsed_title'),
                parsed_year=request.form.get('parsed_year')
            )
        return redirect(url_for('movies.queue'))

    @staticmethod
    @movies.route('/transform', methods=[AllowedMethods.POST])
    def transform():
        TransformMovies.queue()
        TransformMovies.execute()
        return redirect(url_for('movies.queue'))

    @staticmethod
    @movies.route('/load-into-plex', methods=[AllowedMethods.POST])
    def load_into_plex():
        LoadMovies.execute()
        return redirect(url_for('movies.queue'))




