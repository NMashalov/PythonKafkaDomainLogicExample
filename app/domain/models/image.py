from pydantic import BaseModel
from datetime import datetime 

class Image(BaseModel):
    picture: bytes
    username: str
    datetime: datetime 