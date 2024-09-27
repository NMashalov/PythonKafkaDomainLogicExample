from pydantic_settings import BaseSettings, SettingsConfigDict



class ProduceSettings(BaseSettings):
    bootstrap_servers: str
    username: str
    password: str
    topic: str
    sasl_mechanism: str
    security_protocol: str

    model_config = SettingsConfigDict(env_file='.env',)
