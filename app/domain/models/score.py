from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel


class ScoreType(StrEnum):
    novice = 'novice'
    expert = 'expert'

class ScoreInput(BaseModel):
    username: str
    score_type: ScoreType
    datetime: datetime

class ScoreOutput(BaseModel):
    username: str
    score_type: ScoreType
    datetime: datetime
