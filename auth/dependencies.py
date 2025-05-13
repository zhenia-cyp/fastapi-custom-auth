from fastapi import Depends
from schema.schema import TokenType
from services.auth import AuthService, get_auth_service
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.get_user_from_token(token, TokenType.ACCESS)