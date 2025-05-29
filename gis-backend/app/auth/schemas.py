from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class RoleEnum(str, Enum):
    admin = "Admin"
    surveyor = "Surveyor"
    qc = "QC"

class LoginRequest(BaseModel):
    email: EmailStr
    password: str  # Plaintext for now (demo only)

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserInfo(BaseModel):
    sub: str
    role: Optional[RoleEnum] = None
