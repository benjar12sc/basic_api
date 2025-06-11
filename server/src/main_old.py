from typing import List, Union
from fastapi import Depends, FastAPI, HTTPException, Query

from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Year = Column(Integer)
    Month = Column(Integer)
    Supplier = Column(String)
    ItemCode = Column(String)
    ItemDescription = Column(String)
    ItemType = Column(String)
    RetailSales = Column(Float)
    RetailTransfers = Column(Float)
    WarehouseSales = Column(Float)


DATABASE_URL = "sqlite:///../data/sales.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "welcome"}


@app.get("/item/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    session = SessionLocal()
    sale = session.query(Sale).filter(Sale.id == item_id).first()
    session.close()
    if sale is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {
        "id": sale.id,
        "Year": sale.Year,
        "Month": sale.Month,
        "Supplier": sale.Supplier,
        "ItemCode": sale.ItemCode,
        "ItemDescription": sale.ItemDescription,
        "ItemType": sale.ItemType,
        "RetailSales": sale.RetailSales,
        "RetailTransfers": sale.RetailTransfers,
        "WarehouseSales": sale.WarehouseSales,
    }


@app.get("/items")
def read_items(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)) -> List[dict]:
    session = SessionLocal()
    sales = session.query(Sale).offset(skip).limit(limit).all()
    session.close()
    return [
        {
            "id": sale.id,
            "Year": sale.Year,
            "Month": sale.Month,
            "Supplier": sale.Supplier,
            "ItemCode": sale.ItemCode,
            "ItemDescription": sale.ItemDescription,
            "ItemType": sale.ItemType,
            "RetailSales": sale.RetailSales,
            "RetailTransfers": sale.RetailTransfers,
            "WarehouseSales": sale.WarehouseSales,
        }
        for sale in sales
    ]

@app.post("/item", response_model=dict)
def create_item(item: SaleCreate, db: Session = Depends(get_db)):
    sale = Sale(**item.dict())
    db.add(sale)
    db.commit()
    db.refresh(sale)
    return {
        "id": sale.id,
        "Year": sale.Year,
        "Month": sale.Month,
        "Supplier": sale.Supplier,
        "ItemCode": sale.ItemCode,
        "ItemDescription": sale.ItemDescription,
        "ItemType": sale.ItemType,
        "RetailSales": sale.RetailSales,
        "RetailTransfers": sale.RetailTransfers,
        "WarehouseSales": sale.WarehouseSales,
    }