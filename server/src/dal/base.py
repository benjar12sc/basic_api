from typing import Generic, TypeVar, Type, List, Optional
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T')

class BaseDAL(Generic[T]):
    def __init__(self, session: AsyncSession, model: Type[T]):
        self.session = session
        self.model = model

    async def get(self, obj_id: int) -> Optional[T]:
        result = await self.session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10) -> List[T]:
        result = await self.session.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def create(self, obj: T) -> T:
        self.session.add(obj)
        return obj

    async def update(self, obj_id: int, updated_data: dict) -> Optional[T]:
        await self.session.execute(
            update(self.model).where(self.model.id == obj_id).values(**updated_data)
        )
        return await self.get(obj_id)

    async def delete(self, obj_id: int) -> None:
        result = await self.session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        obj = result.scalar_one_or_none()
        if obj:
            await self.session.delete(obj)
        else:
            raise ValueError(f"{self.model.__name__} with id {obj_id} does not exist.")
