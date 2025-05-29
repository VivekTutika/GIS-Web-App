from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from enum import Enum

class RoleEnum(str, Enum):
    surveyor = "Surveyor"
    qc = "QC"
    admin = "Admin"

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserInfo(BaseModel):
    id: str
    email: EmailStr
    role: Optional[RoleEnum] = None
    name: Optional[str] = None
