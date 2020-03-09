from flask import current_app

from sqlalchemy import exc

from .database import create_or_update
from .models import EtlConfig
from .models import db
from .database import TestData

# @create_or_update
# def create_or_update_dump_location(dump_location=None):
#     dump_location = EtlConfig(config_entity='dump_location', dump_location=dump_location)
#     return db.session.merge(dump_location)
    # try:
    #     db.session.add(dump_location)
    #     db.session.commit()
    # except exc.IntegrityError as e:
    #     db.session.merge(dump_location)
