import logging

from src.utilities.database.models import db

from src.utilities.database.database import create_or_update

from src.utilities.database.models import ExtractedMovies
from src.utilities.database.models import TransformedMovies
from src.utilities.database.models import LoadMovies


class Delete:

    def __init__(self):
        return

    @staticmethod
    @create_or_update
    def all():
        db.session.query(ExtractedMovies).delete()
        db.session.query(TransformedMovies).delete()
        db.session.query(LoadMovies).delete()

