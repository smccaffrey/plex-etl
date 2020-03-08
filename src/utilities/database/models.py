# from src.app import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movies(db.Model):
    # __tablename__ = 'movies-queue'
    # __table_args__ = {'extend_existing': True}
    torrent_name = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    file_path = db.Column(db.Text)

    def __repr__(self):
        return str({'name': self.torrent_name, 'fpath': self.file_path})
        # return f'<Movie {self.torrent_name}>'
