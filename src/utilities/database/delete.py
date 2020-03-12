import logging

from src.utilities.database.models import db

from src.utilities.database.database import create_or_update

from src.utilities.database.models import ExtractedMovies
from src.utilities.database.models import TransformedMovies

# def delete_test_movies():
#     movies = Movies.query.all()
#     count = 0
#     for movie in movies:
#         db.session.delete(movie)
#         db.session.commit()
#         count += 1
#
#     logging.info(f'Deleted {count} test movies')

class Delete:

    def __init__(self):
        return

    @staticmethod
    @create_or_update
    def all():
        db.session.query(ExtractedMovies).delete()
        db.session.query(TransformedMovies).delete()

