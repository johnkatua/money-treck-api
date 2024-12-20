from pydantic import BaseModel, EmailStr


class Settings(BaseModel):
    DATABASE_URL: str

    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    MONGO_DB: str

    class Config:
        env_file = "./.env"


settings = Settings()
