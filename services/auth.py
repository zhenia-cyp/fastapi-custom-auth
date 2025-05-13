from fastapi import Depends
from models import User
from repositories.users import UserRepository, get_user_repository
from utils.utils import verify_password
from auth.tokens import generate_jwt_token, verify_token, extract_email
from schema.schema import TokenType, SignInRequest, UserResponse
from utils.exceptions import CredentialsException


class AuthService:
    def __init__(self, user_repo: UserRepository = Depends(get_user_repository)):
        self.user_repo = user_repo


    async def authenticate(self, password, current_user: User) -> tuple[str, str]:
        if not verify_password(password, current_user.hashed_password):
            raise CredentialsException("Invalid email or password")
        access_token = generate_jwt_token({"sub": current_user.email}, TokenType.ACCESS)
        refresh_token = generate_jwt_token({"sub": current_user.email}, TokenType.REFRESH)
        return access_token, refresh_token


    async def get_user_from_token(self, token: str, token_type: TokenType) -> User:
        payload = verify_token(token, token_type)
        email = extract_email(payload)
        user = await self.user_repo.get_by_email(email)
        if not user:
            raise CredentialsException("User not found")
        return user


def get_auth_service(repo: UserRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(repo)

