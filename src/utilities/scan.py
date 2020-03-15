import os

from flask import current_app
from werkzeug.exceptions import NotFound

from src.utilities.database.query import QueryEtlConfig
from src.utilities.database.insert import InsertExtractedMovies


class ScanForMovies:

    @staticmethod
    def start():
        dump_location = QueryEtlConfig.get_dump_location().config_value

        if dump_location is None:
            raise NotFound

        for root, dirs, files in os.walk(dump_location):
            for file in files:
                full_path_loc = os.path.join(root, file)
                # current_app.logger.info(file)
                # current_app.logger.info(current)
                InsertExtractedMovies.process(raw_torrent_name=file, full_path_loc=full_path_loc)
        return True

