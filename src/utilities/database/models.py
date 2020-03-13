from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EtlConfig(db.Model):
    __tablename__ = 'etl_config'
    # id = db.Column(db.Integer, primary_key=True)
    config_name = db.Column(db.Text, unique=True, primary_key=True)
    config_value = db.Column(db.Text)

    def __repr__(self):
        return str({'config_name': self.config_name,
                    'config_value': self.config_value})


class ExtractedMovies(db.Model):
    __tablename__ = 'extracted_movies'
    raw_torrent_name = db.Column(db.String(), unique=True, nullable=False, primary_key=True)
    full_path_loc = db.Column(db.Text)

    def __repr__(self):
        return str({'raw_torrent_name': self.raw_torrent_name,
                    'full_path_loc': self.full_path_loc})


class TransformedMovies(db.Model):
    __tablename__ = 'transformed_movies'
    id = db.Column(db.Integer, primary_key=True)
    raw_torrent_name = db.Column(db.String(),
                                 db.ForeignKey('extracted_movies.raw_torrent_name'),
                                 unique=True,
                                 nullable=False)
    parsed_title = db.Column(db.Text)
    parsed_year = db.Column(db.Integer)
    error = db.Column(db.Boolean)

    extracted_movie = db.relationship('ExtractedMovies', backref='transformed_movies')

    def __repr__(self):
        return str({'raw_torrent_name': self.raw_torrent_name,
                    'parsed_title': self.parsed_title,
                    'parsed_year': self.parsed_year,
                    'error': self.error})

class LoadMovies(db.Model):
    __tablename__ = 'load_movies'
    id = db.Column(db.Integer, primary_key=True)
    raw_torrent_name = db.Column(db.String(),
                                 db.ForeignKey('transformed_movies.raw_torrent_name'),
                                 unique=True,
                                 nullable=False)
    source_full = db.Column(db.Text)
    destination_parent = db.Column(db.Text)
    destination_full = db.Column(db.Text)
    new_dir = db.Column(db.Text)
    new_name = db.Column(db.Text)

    transformed_movie = db.relationship('TransformedMovies', backref='load_movies')

    def __repr__(self):
        return str({'id': self.id,
                    'raw_torrent_name': self.raw_torrent_name,
                    'source_full': self.source_full,
                    'destination_parent': self.destination_parent,
                    'destination_full': self.destination_parent,
                    'new_dir': self.new_dir,
                    'new_name': self.new_name})