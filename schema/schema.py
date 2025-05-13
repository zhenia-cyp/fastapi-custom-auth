from enum import Enum
from pydantic import BaseModel


class TokenType(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"


class TokenPayload(BaseModel):
    sub: str
    exp: float
    iat: float
    type: str


class RegisterUserSchema(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class SignInRequest(BaseModel):
    email: str
    password: str