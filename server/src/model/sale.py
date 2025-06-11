from sqlalchemy import Column, Integer, String, Float
from config import Base

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