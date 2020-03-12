import os

from pathlib import Path
from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

from src.utilities.database.delete import Delete

from src.utilities.parse import ParseExtractedMovies
from src.utilities.api.methods import AllowedMethods


class Actions:

    actions = Blueprint('actions', __name__)

    @staticmethod
    @actions.route('/parse', methods=[AllowedMethods.POST])
    def parse():
        ParseExtractedMovies.process()
        return redirect(url_for('movies.queue'))

    @staticmethod
    @actions.route('/cleanup', methods=[AllowedMethods.POST])
    def cleanup():
        Delete.all()
        return redirect(url_for('movies.queue'))
