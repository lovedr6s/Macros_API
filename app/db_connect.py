import os
from datetime import date as dt_date
from dotenv import load_dotenv
from app.database import Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(os.getenv('DATABASE'))
session = sessionmaker(bind=engine)

def add_product(product_data, user_id):
    db = session()
    try:
        new_product = Product(
            name=product_data['name'],
            kcal=product_data['kcal'],
            carbs=product_data['carbs'],
            proteins=product_data['proteins'],
            fats=product_data['fats'],
            date=dt_date.today(),
            user=user_id
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
    finally:
        db.close()


def get_products(date, user_id):
    db = session()
    try:
        products = db.query(Product).filter(
            Product.user == user_id,
            Product.date == date
        ).all()
        return [
            {
                "id": product.id,
                "name": product.name,
                "kcal": product.kcal,
                "carbs": product.carbs,
                "proteins": product.proteins,
                "fats": product.fats,
                "date": str(product.date),
                "user": product.user
            }
            for product in products
        ]
    finally:
        db.close()