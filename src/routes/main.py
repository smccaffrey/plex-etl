import os

from pathlib import Path
from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

from src.utilities.database.query import QueryEtlConfig
from src.utilities.database.query import QueryExtractedMovies
from src.utilities.database.query import QueryTransformedMovies

from src.utilities.database.insert import insert_test_movies
from src.utilities.database.insert import InsertEtlConfig

from src.utilities.database.delete import delete_test_movies

from src.utilities.parse import ParseExtractedMovies

from src.utilities.scan import ScanForMovies

from src.utilities.api.methods import AllowedMethods

class Application:

    application = Blueprint('application', __name__)

    @staticmethod
    @application.route('/index', methods=[AllowedMethods.GET])
    @application.route('/', methods=[AllowedMethods.GET])
    def index():
        return render_template('index.html')

    @staticmethod
    @application.route('/queue', methods=[AllowedMethods.GET])
    def queue():
        """Returns a rendered template view off all new items in the queue"""
        config = QueryEtlConfig.get_dump_location()
        movies = QueryExtractedMovies.get_parsed_results()
        return render_template('queue.html', records=movies, config=config)

    @staticmethod
    @application.route('/scan', methods=[AllowedMethods.POST])
    def scan():
        if ScanForMovies.start():
            return redirect(url_for('application.queue'))

    @staticmethod
    @application.route('/update-dump-location', methods=[AllowedMethods.POST])
    def update():
        if request.form:
            InsertEtlConfig.dump_location(dump_location=request.form.get("dump_location"))
        return redirect(url_for('application.queue'))


    @staticmethod
    @application.route('/parse', methods=[AllowedMethods.POST])
    def parse():
        ParseExtractedMovies.process()
        return redirect(url_for('application.queue'))

    @staticmethod
    @application.route('/test', methods=[AllowedMethods.POST])
    def insert_test_movies():
        insert_test_movies()
        return redirect(url_for('application.index'))

    @staticmethod
    @application.route('/delete', methods=[AllowedMethods.POST])
    def delete_test_movies():
        delete_test_movies()
        return redirect(url_for('application.index'))

    @staticmethod
    @application.route('/create-test-files', methods=[AllowedMethods.POST])
    def generate_test_movie_files():
        root_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'tests', 'movies')
        if not os.path.exists(root_path):
            os.mkdir(root_path)
        test_movies = QueryExtractedMovies.get_all()
        for test_file in test_movies:
            test_file_dir = os.path.join(root_path, test_file.torrent_name)
            test_file_path = os.path.join(root_path, test_file.torrent_name, str(test_file.torrent_name) + '.mp4')
            os.mkdir(test_file_dir)
            Path(test_file_path).touch()
        return redirect(url_for('application.index'))
