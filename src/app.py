import logging
from flask import Flask

from src.routes.main import Application
from src.routes.actions import Actions
from src.routes.config import Config
from src.routes.movies import Movies
from src.routes.test import TestMovies

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')

app = Flask(__name__)

app.register_blueprint(Application.application)
app.register_blueprint(Movies.movies)
app.register_blueprint(Actions.actions)
app.register_blueprint(TestMovies.test_movies)
app.register_blueprint(Config.config)
