from pydantic import BaseModel


class Settings(BaseModel): # pylint: disable=too-few-public-methods
    DATABASE_URL: str

    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    MONGO_DB: str

    class Config: # pylint: disable=too-few-public-methods
        env_file = "./.env"


settings = Settings()
