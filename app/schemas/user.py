from datetime import datetime
from pydantic import BaseModel, Field

class UserBaseSchema(BaseModel):
  name: str
  email: str
  photo: str
  role: str = 'Customer'
  created_at: datetime | None = None
  updated_at: datetime | None = None

  class Config:
    orm_mode = True

class CreateUserSchema(UserBaseSchema):
  password: str = Field(..., min_length=8)
  password_confirm: str
  verified: bool = False