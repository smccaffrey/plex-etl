
from flask import current_app

from sqlalchemy import exc

from src.utilities.database.models import db

def create_or_update(func):
    def persist(*args, **kwargs):
        func(*args, **kwargs)
        try:
            db.session.commit()
            # current_app.logger.info(f'DB Success: {str(func)}')
            return True
        except exc.SQLAlchemyError as e:
            current_app.logger.info(f'DB Failure: {str(func)}')
            current_app.logger.info(f'Error: {e}')
            db.session.rollback()
            return False
    return persist