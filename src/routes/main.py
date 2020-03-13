import os

from pathlib import Path
from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

from src.utilities.api.methods import AllowedMethods


class Application:

    application = Blueprint('application', __name__)

    @staticmethod
    @application.route('/index', methods=[AllowedMethods.GET])
    @application.route('/', methods=[AllowedMethods.GET])
    def index():
        return render_template('index.html')
