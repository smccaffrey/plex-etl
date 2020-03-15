import os
import pathlib
# import logging

from flask_script import Manager
# from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

from src.app import app
from src.utilities.database.models import db
from src.utilities.database.setup import DefaultConfigValues


manager = Manager(app)
db.init_app(app)

APPLICATION_DIR = os.path.join(Path.home(), '.plex-etl')
if not os.path.exists(APPLICATION_DIR):
    os.mkdir(APPLICATION_DIR)

@manager.command
def test():
    status_code = 200
    assert status_code == 200, 'Build Failed'


@manager.command
def dev():
    os.environ['ENV'] = 'dev'
    database_file = os.path.join(APPLICATION_DIR, 'dev_database.db')
    database = "sqlite:///{}".format(database_file)
    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  # maybe remove later
    db.create_all()
    DefaultConfigValues.setup()

    app.run(debug=True, port=3001)


@manager.command
def prod():
    os.environ['ENV'] = 'prod'

    database_file = os.path.join(APPLICATION_DIR, 'prod_database.db')
    database = "sqlite:///{}".format(database_file)
    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  # maybe remove later
    db.create_all()
    DefaultConfigValues.setup()

    app.run(debug=False, port=3002)


if __name__ == '__main__':

    manager.run()
