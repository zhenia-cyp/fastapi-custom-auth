from typing import Dict
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_async_session
from models.models import User
from repositories.base import BaseRepository


class UserRepository(BaseRepository):

  async def get_by_email(self, email: str) -> User | None:
        try:
            stmt = select(User).filter_by(email=email)
            result = await self.session.execute(stmt)
            return result.scalar_one()
        except SQLAlchemyError:
            return None


  async def create(self, data: Dict) -> User | None:
    try:
        new_user = User(**data)
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user
    except SQLAlchemyError:
        await self.session.rollback()
        return None


async def get_user_repository(session: AsyncSession = Depends(get_async_session)) -> UserRepository:
    return UserRepository(session)