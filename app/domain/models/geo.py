from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class GeoType(Enum):
    mobile = 'mobile'
    transaction = 'transaction'
    gps = 'gps'
    satellite = 'satellite'

class InRecord(BaseModel):
    pass



