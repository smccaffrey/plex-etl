import os
import shutil

from flask import current_app

from src.utilities.database.query import QueryLoadMovies
from src.utilities.database.insert import InsertLoadMovies


class LoadMovies:

    def __init__(self):
        return

    @staticmethod
    def execute():
        movies = QueryLoadMovies.get_all(filter_errors=True)

        # print(movies)

        for movie in movies:

            _old_file_dir = movie.source_full

            _new_full_dir = os.path.join(
                movie.destination_parent,
                movie.new_dir
            )

            _new_file_dir = os.path.join(
                movie.destination_full
            )

            try:
                os.mkdir(_new_full_dir)
                current_app.logger.info(f'Created directory: {_new_full_dir}')
            except Exception as e:
                current_app.logger.info(e)

            shutil.move(_old_file_dir, _new_file_dir)

            InsertLoadMovies.process_loaded(
                id=movie.id,
                loaded=True
            )

            current_app.logger.info(f'Moved file \n \t {_old_file_dir} \n \t\t --> {_new_file_dir}')
