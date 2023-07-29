from pydantic import BaseSettings


class Settings(BaseSettings):
    AUTH_TOKEN: str
    NUMBER_FROM: str
    NUMBER_TO: str


settings = Settings()
