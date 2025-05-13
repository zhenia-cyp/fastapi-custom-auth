from fastapi import Depends

from models import User
from schema.schema import RegisterUserSchema, UserResponse
from repositories.users import UserRepository, get_user_repository
from utils.utils import get_hash_password


class UserService:
    def __init__(self, user_repo: UserRepository = Depends(get_user_repository)):
        self.user_repo = user_repo

    async def create(self, user: RegisterUserSchema) -> UserResponse | None:
        existing_user = await self.user_repo.get_by_email(user.email)
        if existing_user:
            return None
        hashed_password = get_hash_password(user.password)
        user_dict = user.model_dump(exclude={"password"})
        user_dict["hashed_password"] = hashed_password
        new_user = await self.user_repo.create(user_dict)
        if new_user:
            return UserResponse.model_validate(new_user)
        return None


    async def get_by_email(self, email: str) -> User | None:
        return await self.user_repo.get_by_email(email)


async def get_user_service(repo: UserRepository = Depends(get_user_repository)):
    return UserService(repo)