from flask import current_app

from sqlalchemy import exc

from src.utilities.database.models import Movies
from src.utilities.database.models import ExtractedMovies
from src.utilities.database.models import EtlConfig
from src.utilities.database.models import TransformedMovies

from src.utilities.database.models import db
from src.utilities.database.database import create_or_update

from src.utilities.database.database import TestData


class InsertExtractedMovies:

    @staticmethod
    @create_or_update
    def process(raw_torrent_name: str, full_path_loc: str):
        return db.session.merge(ExtractedMovies(
            raw_torrent_name=raw_torrent_name,
            full_path_loc=full_path_loc
        ))


class InsertTransformedMovies:

    @staticmethod
    @create_or_update
    def process(raw_torrent_name, parsed_title, parsed_year, error=None):
        return db.session.merge(TransformedMovies(
            raw_torrent_name=raw_torrent_name,
            parsed_title=parsed_title,
            parsed_year=parsed_year,
            error=error
        ))


class InsertEtlConfig:

    @staticmethod
    @create_or_update
    def dump_location(dump_location: str):
        return db.session.merge(EtlConfig(
            config_entity='dump_location',
            dump_location=dump_location
        ))


def insert_test_movies():
    for test_movie in TestData.get():
        # for name, fpath in test_movie.items():
        movie = Movies(torrent_name=test_movie['name'], file_path=test_movie['fpath'])
        try:
            db.session.add(movie)
            db.session.commit()
            current_app.logger.info(f'Inserted {test_movie["name"]} to database')
        except exc.IntegrityError as e:
            current_app.logger.debug(f'Attempted to insert duplicate movie: {test_movie["name"]}')
            db.session.rollback()
