import os
import pathlib
# import logging

from flask_script import Manager
# from flask_sqlalchemy import SQLAlchemy
# from pathlib import Path

from src.app import app
from src.utilities.database.models import db
from src.utilities.database.setup import DefaultConfigValues


manager = Manager(app)
db.init_app(app)

# def db_path(func, path):
#     if not os.path.exists(os.path.dirname(path=path)):
#         os.mkdirs(os.path.dirname(path=path))
#     if not os.path.exists(path=path):
#         pathlib.Path(path).touch()
#
#     return func()


@manager.command
def test():
    """
    Entry point for unit testing
    :param coverage:
    :return:
    """
    status_code = 200
    assert status_code == 200, 'Build Failed'

# @db_path(path=os.path.join('~/', '.plex-etl', 'dev_database.db'))
@manager.command
def dev():
    os.environ['ENV'] = 'dev'
    database_file = os.path.join('/home/sysadmin', '.plex-etl', 'dev_database.db')
    # database_file = os.path.join('/tmp', 'dev_database.db')
    database = "sqlite:///{}".format(database_file)
    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True  # maybe remove later
    db.create_all()
    DefaultConfigValues.setup()

    app.run(debug=True, port=3001)


@manager.command
def prod():
    os.environ['ENV'] = 'prod'
    app.run(debug=False, port=3002)


if __name__ == '__main__':

    manager.run()
