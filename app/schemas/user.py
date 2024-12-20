from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


class UserBaseSchema(BaseModel):
    name: str = Field(..., title="User's Full Name")
    email: EmailStr = Field(..., title="User's Email Address")
    role: str = Field(default="Customer", title="User's Role")
    photo: str | None = Field(default=None, title="URL of the User's Profile Photo")
    created_at: datetime | None = Field(
        default=None, title="Timestamp of User Creation"
    )
    updated_at: datetime | None = Field(default=None, title="Timestamp of Last Update")

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: str = Field(..., min_length=8)
    password_confirm: str
    verified: bool = False
