import logging
from flask import Flask

from src.routes.main import Application

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')

app = Flask(__name__)

app.register_blueprint(Application.application)
