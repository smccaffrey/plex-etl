from flask import current_app

from sqlalchemy import exc

from src.utilities.helper import AttrDict

from src.utilities.database.database import create_or_update

from src.utilities.database.models import EtlConfig
from src.utilities.database.models import ExtractedMovies
from src.utilities.database.models import TransformedMovies
from src.utilities.database.models import LoadMovies


class QueryExtractedMovies:

    @staticmethod
    def get_all():
        return ExtractedMovies.query.all()

    @staticmethod
    def get_parsed_results():
        results = ExtractedMovies.query \
            .outerjoin(TransformedMovies) \
            .add_columns(TransformedMovies.id,TransformedMovies.parsed_title, TransformedMovies.parsed_year) \
            .all()
        return [AttrDict(result._asdict()) for result in results]


class QueryTransformedMovies:

    @staticmethod
    def get_all():
        return TransformedMovies.query.all()

class QueryLoadMovies:

    def __init__(self):
        return

    @staticmethod
    def get_all():
        return LoadMovies.query.all()

    @staticmethod
    def get_combined():
        results = LoadMovies.query \
            .outerjoin(TransformedMovies) \
            .add_columns(TransformedMovies.parsed_title, TransformedMovies.parsed_year) \
            .all()
        return [AttrDict(result._asdict()) for result in results]

class QueryEtlConfig:

    @staticmethod
    def get_all():
        return EtlConfig.query.all()

    @staticmethod
    def get_dump_location():
        return EtlConfig.query.filter_by(config_name='dump_location').first()

    @staticmethod
    def get_plex_movie_dir():
        return EtlConfig.query.filter_by(config_name='plex_movie_dir').first()
