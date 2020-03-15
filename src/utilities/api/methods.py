import enum


class AllowedMethods(enum.EnumMeta):
    """This class exists because I'm tired of
	typing quotes to validate request.method
	types"""

    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
