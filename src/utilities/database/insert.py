from flask import current_app

from src.utilities.database.models import ExtractedMovies
from src.utilities.database.models import EtlConfig
from src.utilities.database.models import TransformedMovies
from src.utilities.database.models import LoadMovies
from src.utilities.database.models import TestMovies

from src.utilities.database.query import QueryEtlConfig

from src.utilities.database.models import db
from src.utilities.database.database import create_or_update


class InsertExtractedMovies:

    def __init__(self):
        return

    @staticmethod
    @create_or_update
    def process(raw_torrent_name: str, full_path_loc: str) -> bool:
        return db.session.merge(ExtractedMovies(
            raw_torrent_name=raw_torrent_name,
            full_path_loc=full_path_loc
        ))


class InsertTransformedMovies:

    def __str__(self):
        return self.__class__.__name__

    @staticmethod
    @create_or_update
    def process(raw_torrent_name: str, parsed_title: str, parsed_year: int) -> bool:
        current_app.logger.info(
            f'Inserted raw_torrent_name={raw_torrent_name} | parsed_title={parsed_title} | parsed_year={parsed_year} to transformed_movies')
        return db.session.merge(TransformedMovies(
            raw_torrent_name=raw_torrent_name,
            parsed_title=parsed_title,
            parsed_year=parsed_year
        ))

    @staticmethod
    @create_or_update
    def process_merge(id: int, raw_torrent_name: str, parsed_title: str, parsed_year: int) -> bool:
        current_app.logger.info(
            f'Inserted raw_torrent_name={raw_torrent_name} | parsed_title={parsed_title} | parsed_year={parsed_year} to transformed_movies')
        return db.session.merge(TransformedMovies(
            id=id,
            raw_torrent_name=raw_torrent_name,
            parsed_title=parsed_title,
            parsed_year=parsed_year
        ))


class InsertLoadMovies:

    def __init__(self):
        return

    @staticmethod
    @create_or_update
    def process(raw_torrent_name: str, source_full: str, destination_parent: str = None, destination_full: str = None,
                new_dir: str = None, new_name: str = None, error: bool = False) -> bool:
        return db.session.merge(LoadMovies(
            raw_torrent_name=raw_torrent_name,
            source_full=source_full,
            destination_parent=destination_parent,
            destination_full=destination_full,
            new_dir=new_dir,
            new_name=new_name,
            error=error
        ))

    @staticmethod
    @create_or_update
    def process_merge(id: int, raw_torrent_name: str, source_full: str, destination_parent: str, destination_full: str,
                      new_dir: str, new_name: str, error: bool, loaded: bool) -> bool:
        return db.session.merge(LoadMovies(
            id=id,
            raw_torrent_name=raw_torrent_name,
            source_full=source_full,
            destination_parent=destination_parent,
            destination_full=destination_full,
            new_dir=new_dir,
            new_name=new_name,
            error=error,
            loaded=loaded
        ))

    @staticmethod
    @create_or_update
    def process_loaded(id: int, loaded: str) -> bool:
        return db.session.merge(LoadMovies(
            id=id,
            loaded=loaded
        ))


class InsertEtlConfig:

    def __init__(self):
        return

    @staticmethod
    @create_or_update
    def process(config_name: str, config_value: str) -> bool:
        active_config_items = QueryEtlConfig.get_all()

        _list = [active_config_item.config_name for active_config_item in active_config_items]

        if config_value == None and config_name in _list:
            return True
        return db.session.merge(EtlConfig(
            config_name=config_name,
            config_value=config_value
        ))

    @staticmethod
    @create_or_update
    def dump_location(dump_location: str) -> bool:
        return db.session.merge(EtlConfig(
            config_entity='dump_location',
            dump_location=dump_location
        ))


class InsertTestMovies:

    def __init__(self):
        return

    @staticmethod
    @create_or_update
    def process(raw_torrent_name: str) -> bool:
        return db.session.merge(TestMovies(
            raw_torrent_name=raw_torrent_name
        ))
