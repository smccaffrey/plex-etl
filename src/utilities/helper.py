
# for common helper objects

class AttrDict(dict):
    """Will recursively convert a python dictionary with a key,value
    data structure to an object with an attribute/value based
    data structure. This is so you can access dict values like _dict.key
    instead of _dict['key'], since this project is very ORM in nature :)"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
