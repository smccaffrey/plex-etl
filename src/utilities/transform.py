import os

from src.utilities.helper import Movie

from src.utilities.database.insert import InsertLoadMovies
from src.utilities.database.query import QueryExtractedMovies
from src.utilities.database.query import QueryLoadMovies
from src.utilities.database.query import QueryEtlConfig

from src.utilities.database.database import create_or_update

class TransformMovies:

    @staticmethod
    @create_or_update
    def queue():
        movies = QueryExtractedMovies.get_all()
        for movie in movies:
            InsertLoadMovies.process(
                raw_torrent_name=movie.raw_torrent_name,
                source_full=movie.full_path_loc,
                destination_parent=None,
                destination_full=None,
                new_dir=None,
                new_name=None
            )

    @staticmethod
    @create_or_update
    def execute():
        movies = QueryLoadMovies.get_combined()
        destination_parent = QueryEtlConfig.get_plex_movie_dir().config_value

        if destination_parent is None:
            raise TypeError('Missing Plex Movies Directory in EtlConfig Table')

        for movie in movies:
            _new_dir = f'{movie.parsed_title} ({movie.parsed_year})'
            _ext = movie.LoadMovies.raw_torrent_name.split('.')[-1]
            _new_file_name = f'{_new_dir}.{_ext}'

            destination_full = os.path.join(destination_parent, _new_dir, _new_file_name)

            InsertLoadMovies.process_merge(
                id=movie.LoadMovies.id,
                raw_torrent_name=movie.LoadMovies.raw_torrent_name,
                source_full=movie.LoadMovies.source_full,
                destination_parent=destination_parent,
                destination_full=destination_full,
                new_dir=_new_dir,
                new_name=_new_file_name
            )


