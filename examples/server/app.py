from datetime import datetime

import fastapi
from pydantic import BaseModel

app = fastapi.FastAPI()

class Subscription(BaseModel):
    username: str
    monthly_fee: float
    start_date: datetime


@app.webhooks.post("new-subscription")
def new_subscription(body: Subscription):
    return None

@app.get("subscribe")
def new_subscription(result:):
    return None



