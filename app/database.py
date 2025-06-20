from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    kcal = Column(Float)
    carbs = Column(Float)
    proteins = Column(Float)
    fats = Column(Float)
    date = Column(Date)
    user = Column(String)