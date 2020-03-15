
from flask import Blueprint
from flask import render_template

from src.utilities.database.query import QueryEtlConfig
from src.utilities.api.methods import AllowedMethods


class Application:

    application = Blueprint('application', __name__)

    @staticmethod
    @application.route('/index', methods=[AllowedMethods.GET])
    @application.route('/', methods=[AllowedMethods.GET])
    def index():
        config = QueryEtlConfig.get_all()
        return render_template('index.html', config=config)
