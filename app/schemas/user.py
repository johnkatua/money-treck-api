from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


class UserBaseSchema(BaseModel):
    name: str = Field(..., title="User's Full Name")
    email: EmailStr = Field(..., title="User's Email Address")
    role: str = Field(default="Customer", title="User's Role")
    photo: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: str = Field(..., min_length=8)
    password_confirm: str
    verified: bool = False
