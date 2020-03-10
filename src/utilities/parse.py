from src.utilities.parser.parse import ParseFileName

from src.utilities.database.query import QueryExtractedMovies

from src.utilities.database.insert import InsertTransformedMovies

class ParseExtractedMovies:

    Parser = ParseFileName()

    @classmethod
    def process(cls):
        for movie in QueryExtractedMovies.get_all():
            parts = cls.Parser.parse(name=movie.raw_torrent_name)
            InsertTransformedMovies.process(
                raw_torrent_name=movie.raw_torrent_name,
                parsed_title=parts['title'] if parts.keys().__contains__('title') else None,
                parsed_year=parts['year'] if parts.keys().__contains__('year') else None
            )

