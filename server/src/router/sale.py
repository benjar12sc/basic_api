from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from config import async_session
from dal.sale import SaleDAL
from model.sale import Sale as SaleModel
from pydantic import BaseModel

# Pydantic schemas
# TODO: Move these to a separate file
class SaleBase(BaseModel):
    Year: int
    Month: int
    Supplier: str
    ItemCode: str
    ItemDescription: str
    ItemType: str
    RetailSales: float

class SaleCreate(SaleBase):
    pass

class SaleRead(SaleBase):
    id: int
    model_config = {"from_attributes": True}

router = APIRouter()

@router.get(
    "/sales",
    response_model=List[SaleRead],
    summary="List sales",
    description="Get a paginated list of sales records. Supports skip and limit for pagination."
)
async def get_sales(skip: int = Query(0, ge=0, description="Number of records to skip for pagination"), limit: int = Query(10, ge=1, le=100, description="Maximum number of records to return")):
    """
    Retrieve a paginated list of sales records.
    """
    async with async_session() as session:
        async with session.begin():
            sale_dal = SaleDAL(session)
            sales = await sale_dal.get_all(skip=skip, limit=limit)
            return [SaleRead.model_validate(sale) for sale in sales]

@router.get(
    "/sale/{sale_id}",
    response_model=SaleRead,
    summary="Get sale by ID",
    description="Retrieve a single sale record by its unique ID."
)
async def get_sale(sale_id: int):
    """
    Retrieve a single sale record by its ID.
    """
    async with async_session() as session:
        async with session.begin():
            sale_dal = SaleDAL(session)
            sale = await sale_dal.get(sale_id)
            if not sale:
                raise HTTPException(status_code=404, detail="Sale not found")
            return SaleRead.model_validate(sale)

@router.post(
    "/sale",
    response_model=SaleRead,
    summary="Create a sale",
    description="Create a new sale record."
)
async def create_sale(sale: SaleCreate):
    """
    Create a new sale record.
    """
    async with async_session() as session:
        async with session.begin():
            sale_obj = SaleModel(**sale.dict())
            sale_dal = SaleDAL(session)
            created = await sale_dal.create(sale_obj)
            return SaleRead.model_validate(created)

@router.put(
    "/sale/{sale_id}",
    response_model=SaleRead,
    summary="Update a sale",
    description="Update an existing sale record by its ID."
)
async def update_sale(sale_id: int, updated_data: dict):
    """
    Update an existing sale record by its ID.
    """
    async with async_session() as session:
        async with session.begin():
            sale_dal = SaleDAL(session)
            updated = await sale_dal.update(sale_id, updated_data)
            if not updated:
                raise HTTPException(status_code=404, detail="Sale not found")
            return SaleRead.model_validate(updated)

@router.delete(
    "/sale/{sale_id}",
    summary="Delete a sale",
    description="Delete a sale record by its ID."
)
async def delete_sale(sale_id: int):
    """
    Delete a sale record by its ID.
    """
    async with async_session() as session:
        async with session.begin():
            sale_dal = SaleDAL(session)
            await sale_dal.delete(sale_id)
            return {"detail": "Sale deleted"}