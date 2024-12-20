from datetime import datetime
from pydantic import BaseModel

class UserBaseSchema(BaseModel):
  name: str
  email: str
  photo: str
  role: str = 'Customer'
  created_at: datetime | None = None
  updated_at: datetime | None = None

  class Config:
    orm_mode = True