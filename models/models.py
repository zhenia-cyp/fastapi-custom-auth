from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base
from sqlalchemy import MetaData


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=False)


    def __str__(self) -> str:
        return f"User(id={self.id}, email='{self.email}', is_active={self.is_active})"


    def __repr__(self) -> str:
        return f"User(id={self.id}, email='{self.email}', is_active={self.is_active})"