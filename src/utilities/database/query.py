
from src.utilities.helper import AttrDict


from src.utilities.database.models import EtlConfig
from src.utilities.database.models import ExtractedMovies
from src.utilities.database.models import TransformedMovies
from src.utilities.database.models import LoadMovies
from src.utilities.database.models import TestMovies


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
        return [AttrDict(result._asdict()) for result in results]\

    @staticmethod
    def get_full_results():
        results = ExtractedMovies.query \
            .outerjoin(TransformedMovies) \
            .add_columns(TransformedMovies.id,TransformedMovies.parsed_title, TransformedMovies.parsed_year) \
            .outerjoin(LoadMovies) \
            .add_columns(LoadMovies.error, LoadMovies.loaded) \
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
    def get_all(filter_errors=False):
        if filter_errors:
            return LoadMovies.query.filter_by(error=False).filter_by(loaded=False).all()
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

class QueryTestMovies:

    def __init__(self):
        return

    @staticmethod
    def get_all():
        return TestMovies.query.all()
