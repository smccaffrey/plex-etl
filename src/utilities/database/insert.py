from flask import current_app

from sqlalchemy import exc

from .models import Movies
from .models import db
from .database import TestData


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
