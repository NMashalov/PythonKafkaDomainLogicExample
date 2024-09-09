from pydantic import BaseModel


class ProduceSettings(BaseModel):
    bootstrap_servers: list[str]
    topic: str
