from nested_multipart_parser.options import (
    NestedParserOptionsBracket,
    NestedParserOptionsDot,
    NestedParserOptionsMixed,
    NestedParserOptionsMixedDot,
)
from nested_multipart_parser.temp_element import TempDict, TempList

DEFAULT_OPTIONS = {
    "separator": "mixed-dot",
    "raise_duplicate": True,
    "assign_duplicate": False,
}

REGEX_SEPARATOR = {
    "bracket": NestedParserOptionsBracket,
    "dot": NestedParserOptionsDot,
    "mixed": NestedParserOptionsMixed,
    "mixed-dot": NestedParserOptionsMixedDot,
}


class NestedParser:
    _valid = None
    errors = None

    def __init__(self, data, options=None):
        self.data = data
        self._options = {**DEFAULT_OPTIONS, **(options or {})}

        assert self._options["separator"] in [
            "dot",
            "bracket",
            "mixed",
            "mixed-dot",
        ]
        assert isinstance(self._options["raise_duplicate"], bool)
        assert isinstance(self._options["assign_duplicate"], bool)

        self._cls_options = REGEX_SEPARATOR[self._options["separator"]]

    def _split_keys(self, data):
        pass

    def convert_value(self, value):
        pass

    def construct(self, data):
        pass

    def is_valid(self):
        pass

    @property
    def validate_data(self):
        pass
