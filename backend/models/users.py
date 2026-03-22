from sqlmodel import SQLModel, Field
import uuid
from pydantic import EmailStr


class UserInDB(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(index=True, unique=True)
    hashed_password: str
