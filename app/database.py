from sqlalchemy import Column, Date, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base): #noqa: D101
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    kcal = Column(Float)
    carbs = Column(Float)
    proteins = Column(Float)
    fats = Column(Float)
    date = Column(Date)
    user = Column(String)
