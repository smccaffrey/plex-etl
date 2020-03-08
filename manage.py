import os
# import logging

from flask_script import Manager
# from flask_sqlalchemy import SQLAlchemy
# from pathlib import Path

from src.app import app
from src.utilities.database.models import db


manager = Manager(app)
db.init_app(app)


@manager.command
def test():
    """
    Entry point for unit testing
    :param coverage:
    :return:
    """
    status_code = 200
    assert status_code == 200, 'Build Failed'


@manager.command
def dev():
    os.environ['ENV'] = 'dev'
    database_file = os.path.join('/tmp', 'plex-etl', 'dev_database.db')
    # database_file = os.path.join('/tmp', 'dev_database.db')
    database = "sqlite:///{}".format(database_file)
    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  # maybe remove later
    db.create_all()

    app.run(debug=True, port=3001)


@manager.command
def prod():
    os.environ['ENV'] = 'prod'
    app.run(debug=False, port=3002)


if __name__ == '__main__':

    manager.run()
