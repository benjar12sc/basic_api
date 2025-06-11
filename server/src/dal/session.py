from typing import List, Optional

from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAL
from model.session import Session as SessionModel

class SessionDAL(BaseDAL[SessionModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, SessionModel)

    async def delete_sessions(self, user_id: int) -> None:
        result = await self.session.execute(
            select(self.model).where(self.model.user_id == user_id)
        )
        sessions = result.scalars().all()
        for session in sessions:
            await self.session.delete(session)
        await self.session.commit()