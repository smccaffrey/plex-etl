import os

from pathlib import Path
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for

# from src.utilities.database.database import TestData
# from src.utilities.database.models import db
from src.utilities.database.models import Movies
from src.utilities.database.insert import insert_test_movies
from src.utilities.database.delete import delete_test_movies
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
        # movies = [dict(movie) for movie in Movies.query.all()]
        # movies = Movies.query.all()
        # print(movies)
        # print(type(movies))
        # for movie in movies:
        #     print(movie.__dict__)
        return render_template('queue.html', records=Movies.query.all())

    @staticmethod
    @application.route('/parse', methods=[AllowedMethods.POST])
    def parse():
        """Parse all active queue items.
        Also repsonsible for writing successes/failure records to the sqlite database"""
        return f'Welcome to the Plex ETL Engine!'

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
        test_movies = Movies.query.all()
        for test_file in test_movies:
            test_file_dir = os.path.join(root_path, test_file.torrent_name)
            test_file_path = os.path.join(root_path, test_file.torrent_name, str(test_file.torrent_name) + '.mp4')
            os.mkdir(test_file_dir)
            Path(test_file_path).touch()
        return redirect(url_for('application.index'))
