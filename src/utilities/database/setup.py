
from src.utilities.database.insert import InsertEtlConfig
from src.utilities.database.query import QueryEtlConfig
from src.utilities.database.database import create_or_update

class DefaultConfigValues:

    @staticmethod
    @create_or_update
    def setup():

        current_config_items = QueryEtlConfig.get_all()

        default_config_values = {
            'dump_location': None,
            'plex_movie_dir': None
        }

        for k,v in default_config_values.items():
            InsertEtlConfig.process(
                config_name=k,
                config_value=v
            )
