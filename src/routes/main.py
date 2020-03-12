import os

from pathlib import Path
from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

from src.utilities.database.query import QueryEtlConfig
from src.utilities.database.query import QueryExtractedMovies
from src.utilities.database.query import QueryTransformedMovies

from src.utilities.database.insert import insert_test_movies
from src.utilities.database.insert import InsertEtlConfig
from src.utilities.database.insert import InsertTransformedMovies

# from src.utilities.database.delete import delete_test_movies
from src.utilities.database.delete import Delete

from src.utilities.parse import ParseExtractedMovies

from src.utilities.scan import ScanForMovies

from src.utilities.api.methods import AllowedMethods

class Application:

    application = Blueprint('application', __name__)

    @staticmethod
    @application.route('/index', methods=[AllowedMethods.GET])
    @application.route('/', methods=[AllowedMethods.GET])
    def index():
        return render_template('index.html')
