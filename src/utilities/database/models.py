from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EtlConfig(db.Model):
    __tablename__ = 'etl_config'
    # id = db.Column(db.Integer, primary_key=True)
    config_entity = db.Column(db.Text, unique=True, primary_key=True)
    dump_location = db.Column(db.Text)

    def __repr__(self):
        return str({'dump_location': self.dump_location})


class Movies(db.Model):
    # __tablename__ = 'movies-queue'
    # __table_args__ = {'extend_existing': True}
    torrent_name = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    file_path = db.Column(db.Text)

    def __repr__(self):
        return str({'name': self.torrent_name, 'fpath': self.file_path})


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
    raw_torrent_name = db.Column(db.String(), db.ForeignKey('extracted_movies.raw_torrent_name'),unique=True, nullable=False)
    parsed_title = db.Column(db.Text)
    parsed_year = db.Column(db.Text)
    error = db.Column(db.Boolean)

    extracted_movie = db.relationship('ExtractedMovies', backref='transformed_movies')

    def __repr__(self):
        return str({'raw_torrent_name': self.raw_torrent_name,
                    'parsed_title': self.parsed_title,
                    'parsed_year': self.parsed_year,
                    'error': self.error})

