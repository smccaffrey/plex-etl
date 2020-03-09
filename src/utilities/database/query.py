from flask import current_app

from sqlalchemy import exc

from src.utilities.database.models import EtlConfig
from src.utilities.database.models import ExtractedMovies

class QueryExtractedMovies:

    @staticmethod
    def get_all():
        return ExtractedMovies.query.all()

class QueryEtlConfig:

    @staticmethod
    def get_all():
        return EtlConfig.query.all()

    @staticmethod
    def get_dump_location():
        return EtlConfig.query.filter_by(config_entity='dump_location').first()
