from .parser import NestedParser as NestPars
from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import ParseError
from django.http import QueryDict
from django.conf import settings

DRF_OPTIONS = {"querydict": True}


class NestedParser(NestPars):
    def __init__(self, data):
        # merge django settings to default DRF_OPTIONS ( special parser options in on parser)
        options = {
            **DRF_OPTIONS,
            **getattr(settings, "DRF_NESTED_MULTIPART_PARSER", {}),
        }
        super().__init__(data, options)

    def convert_value(self, value):
        pass

    @property
    def validate_data(self):
        pass


class DrfNestedParser(MultiPartParser):
    def parse(self, stream, media_type=None, parser_context=None):
        pass
