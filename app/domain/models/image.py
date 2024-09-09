from typing import ClassVar
from pydantic import BaseModel
from datetime import datetime


schema = {
    "doc": "A weather reading.",
    "name": "Weather",
    "namespace": "test",
    "type": "record",
    "fields": [
        {"name": "station", "type": "string"},
        {"name": "time", "type": "long"},
        {"name": "temp", "type": "int"},
    ],
}


class Image(BaseModel):
    image: bytes
    name: str
    datetime: datetime
