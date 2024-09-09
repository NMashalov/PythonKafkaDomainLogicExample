from pydantic import BaseModel
from datetime import datetime


class Score(BaseModel):
    picture: bytes
    username: str
    datetime: datetime
