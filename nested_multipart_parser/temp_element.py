import abc
from typing import Any


class TempElement(abc.ABC):
    @abc.abstractclassmethod
    def __setitem__(self, key, val):
        """method to set element"""

    def check(self, key, value):
        pass

    def __getitem__(self, key):
        if key not in self._elements:
            self[key] = type(self)(options=self._options)
        return self._elements[key]

    def conv_value(self, value: Any) -> Any:
        pass

    @abc.abstractmethod
    def convert(self):
        """method to convert tempoary element to real python element"""


class TempList(TempElement):
    def __init__(self, options=None):
        self._options = options or {}
        self._elements = {}

    def __setitem__(self, key: int, value: Any):
        assert isinstance(key, int), (
            f"Invalid key for list, need to be int, type={type(key)}"
        )
        self.check(key, value)

    def convert(self) -> list:
        pass


class TempDict(TempElement):
    def __init__(self, options=None):
        self._options = options or {}
        self._elements = {}

    def __setitem__(self, key: str, value: Any):
        assert isinstance(key, str), (
            f"Invalid key for dict, need to be str, type={type(key)}"
        )
        self.check(key, value)

    def convert(self) -> dict:
        pass
