
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for

from src.utilities.database.insert import InsertEtlConfig

from src.utilities.api.methods import AllowedMethods


class Config:

    config = Blueprint('config', __name__)

    @staticmethod
    @config.route('/update-dump-location', methods=[AllowedMethods.POST])
    def update():
        if request.form:
            InsertEtlConfig.dump_location(dump_location=request.form.get("dump_location"))
        return redirect(url_for('movies.queue'))

    @staticmethod
    @config.route('/update-config', methods=[AllowedMethods.POST])
    def update_config():
        if request.form:
            InsertEtlConfig.process(config_name=request.form.get("config_name"),
                                    config_value=request.form.get("config_value"))
        return redirect(url_for('movies.queue'))