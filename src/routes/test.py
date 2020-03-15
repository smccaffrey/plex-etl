import os

from pathlib import Path
from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import current_app

from src.utilities.helper import AttrDict

from src.utilities.database.query import QueryTestMovies
from src.utilities.database.insert import InsertTestMovies
from src.utilities.tests.test import TestData

from src.utilities.api.methods import AllowedMethods


class TestMovies:

    test_movies = Blueprint('test_movies', __name__)

    @staticmethod
    @test_movies.route('/insert-test-files', methods=[AllowedMethods.POST])
    def insert_test_files():
        for test_item in TestData.get():
            test_item = AttrDict(test_item)
            InsertTestMovies.process(
                raw_torrent_name=test_item.name
            )
        return redirect(url_for('application.index'))

    @staticmethod
    @test_movies.route('/create-test-files', methods=[AllowedMethods.POST])
    def generate_test_movie_files():
        root_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'tests', 'movies')
        if not os.path.exists(root_path):
            os.mkdir(root_path)
        test_movies = QueryTestMovies.get_all()
        print(test_movies)
        for test_file in test_movies:
            test_file_dir = os.path.join(root_path, test_file.raw_torrent_name)
            test_file_path = os.path.join(root_path, test_file.raw_torrent_name, str(test_file.raw_torrent_name) + '.mp4')
            try:
                os.mkdir(test_file_dir)
                Path(test_file_path).touch()
                current_app.logger.info(f'TESTING: Created {test_file_path}')
            except FileExistsError as e:
                current_app.logger.info(f'File {test_file.raw_torrent_name} Already exists ... Skipping')
        return redirect(url_for('application.index'))
