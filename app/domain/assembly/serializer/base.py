from typing import Generic, TypeVar
from fastavro import parse_schema

T_output = TypeVar('T_output')

class BaseSerializer(Generic[T_output]):
    def __init__(self):
        pass