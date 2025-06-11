from typing import List, Optional

from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAL
from model.sale import Sale as SaleModel

class SaleDAL(BaseDAL[SaleModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, SaleModel)

    @DeprecationWarning
    async def get_sale(self, sale_id: int) -> Optional[SaleModel]:
        result = await self.session.execute(
            select(SaleModel).where(SaleModel.id == sale_id)
        )
        return result.scalar_one_or_none()

    @DeprecationWarning
    async def get_sales(self, skip: int = 0, limit: int = 10) -> List[SaleModel]:
        result = await self.session.execute(
            select(SaleModel).offset(skip).limit(limit)
        )
        return result.scalars().all()

    @DeprecationWarning
    async def create_sale(self, sale: SaleModel) -> None:
        self.session.add(sale)
        await self.session.flush()

    @DeprecationWarning
    async def update_sale(self, sale_id: int, updated_data: dict) -> Optional[SaleModel]:
        stmt = update(SaleModel).where(SaleModel.id == sale_id).values(**updated_data)
        await self.session.execute(stmt)
        await self.session.commit()
        return await self.get_sale(sale_id)

    async def delete_sale(self, sale_id: int) -> None:
        stmt = select(SaleModel).where(SaleModel.id == sale_id)
        result = await self.session.execute(stmt)
        sale = result.scalar_one_or_none()
        if sale:
            await self.session.delete(sale)
            await self.session.commit()
        else:
            raise ValueError(f"Sale with id {sale_id} does not exist.")