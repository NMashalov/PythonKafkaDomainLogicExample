from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class ScoreType(Enum):
    novice = 'novice'
    expert = 'expert'

class ScoreInput(BaseModel):
    username: str
    score_type: ScoreType
    datetime: datetime

class ScoreInput(BaseModel):
    username: str
    score_type: ScoreType
    datetime: datetime
