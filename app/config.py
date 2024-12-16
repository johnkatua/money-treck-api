from pydantic import BaseModel, EmailStr


class Settings(BaseModel):
    pass


settings = Settings()