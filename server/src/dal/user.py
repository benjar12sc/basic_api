from sqlalchemy import Column, Integer, String, Boolean, select
from sqlalchemy.ext.asyncio import AsyncSession
from config import Base

from .base import BaseDAL
from model.user import User as UserModel

class UserDAL(BaseDAL[UserModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, UserModel)

    async def create_user(self, username: str, email: str, password: str, is_active: bool = True, is_superuser: bool = False) -> UserModel:
        new_user = UserModel(username=username, email=email, is_active=is_active, is_superuser=is_superuser)
        new_user.set_password(password)
        self.session.add(new_user)
        await self.session.commit()
        return new_user

    @DeprecationWarning
    async def get_user_by_id(self, user_id: int) -> UserModel:
        return await self.session.get(UserModel, user_id)

    async def get_user_by_username(self, username: str) -> UserModel:
        return await self.session.execute(
            select(UserModel).where(UserModel.username == username)
        ).scalar_one_or_none()

    @DeprecationWarning
    async def update_user(self, user: UserModel) -> UserModel:
        self.session.add(user)
        await self.session.commit()
        return user

    @DeprecationWarning
    async def delete_user(self, user_id: int) -> None:
        user = await self.get_user_by_id(user_id)
        if user:
            await self.session.delete(user)
            await self.session.commit()
        else:
            raise ValueError(f"User with id {user_id} does not exist.")