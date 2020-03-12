import os

from pathlib import Path
from flask import Blueprint
from flask import redirect
from flask import url_for

from src.utilities.database.query import QueryExtractedMovies

from src.utilities.database.insert import insert_test_movies

from src.utilities.api.methods import AllowedMethods


class TestMovies:

    test_movies = Blueprint('test_movies', __name__)

    @staticmethod
    @test_movies.route('/test', methods=[AllowedMethods.POST])
    def insert_test_movies():
        insert_test_movies()
        return redirect(url_for('application.index'))

    # @staticmethod
    # @test_movies.route('/delete', methods=[AllowedMethods.POST])
    # def delete_test_movies():
    #     delete_test_movies()
    #     return redirect(url_for('application.index'))

    @staticmethod
    @test_movies.route('/create-test-files', methods=[AllowedMethods.POST])
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
