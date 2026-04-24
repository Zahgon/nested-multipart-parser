import re

# compatibilty python < 3.9
try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache


@cache
def cache_regex_compile(*ar, **kw):
    pass


class InvalidFormat(Exception):
    """key is invalid formated"""

    def __init__(self, key):
        super().__init__(f"invaid key format: {key}")


class NestedParserOptionsType(type):
    def __new__(cls, cls_name, ns, childs):
        if cls_name != "NestedParserOptionsAbstract" and cls_name:
            if "sanitize" not in childs:
                raise ValueError("you need to define sanitize methods")
        return super().__new__(cls, cls_name, ns, childs)


INVALID_TOKEN_PARSER = ("[", "]", ".")


class NestedParserOptionsAbstract(metaclass=NestedParserOptionsType):
    def check(self, key, keys):
        pass

    def split(self, key):
        pass


class NestedParserOptionsDot(NestedParserOptionsAbstract):
    def __init__(self):
        self._reg_spliter = cache_regex_compile(r"^([^\.]+)(.*?)(\.)?$")
        self._reg_options = cache_regex_compile(r"(\.[^\.]+)")

    def sanitize(self, key, value):
        pass


class NestedParserOptionsBracket(NestedParserOptionsAbstract):
    def __init__(self):
        self._reg_spliter = cache_regex_compile(r"^([^\[\]]+)(.*?)(\[\])?$")
        self._reg_options = cache_regex_compile(r"(\[[^\[\]]+\])")

    def sanitize(self, key, value):
        pass


class NestedParserOptionsMixedDot(NestedParserOptionsAbstract):
    def __init__(self):
        self._reg_spliter = cache_regex_compile(
            r"^([^\[\]\.]+)(.*?)((?:\.)|(?:\[\]))?$"
        )
        self._reg_options = cache_regex_compile(r"(\[\d+\])|(\.[^\[\]\.]+)")

    def sanitize(self, key, value):
        pass


class NestedParserOptionsMixed(NestedParserOptionsMixedDot):
    def __init__(self):
        self._reg_spliter = cache_regex_compile(
            r"^([^\[\]\.]+)(.*?)((?:\.)|(?:\[\]))?$"
        )
        self._reg_options = cache_regex_compile(r"(\[\d+\])|(\.?[^\[\]\.]+)")

    def sanitize(self, key, value):
        pass
