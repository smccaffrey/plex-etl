import logging

from .models import Movies
from .models import db

def delete_test_movies():
    movies = Movies.query.all()
    count = 0
    for movie in movies:
        db.session.delete(movie)
        db.session.commit()
        count += 1

    logging.info(f'Deleted {count} test movies')