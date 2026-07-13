from pydantic import BaseModel, EmailStr, Field
import uuid

class AdminCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

class AdminLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

class Token(BaseModel):
    access_token: str
    token_type: str

class AdminResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr

    class Config:
        from_attributes = True