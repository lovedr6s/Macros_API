import os
from datetime import date as dt_date

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Product

load_dotenv()

engine = create_engine(os.getenv('DATABASE'))
session = sessionmaker(bind=engine)

def add_product(product_data, user_token):
    """Save product and it's macros.

    Args:
        product_data (json): json data with product and it's macros
        user_token (str): user's token

    """
    db = session()
    try:
        new_product = Product(
            name=product_data['name'],
            kcal=product_data['kcal'],
            carbs=product_data['carbs'],
            proteins=product_data['proteins'],
            fats=product_data['fats'],
            date=dt_date.today(),
            user=user_token,
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
    finally:
        db.close()


def get_products(date, user_token):
    """Get products from db.

    Args:
        date (date): chooses from what date u will get products
        user_token (str): user's token

    Returns:
        dict: Macroses

    """
    db = session()
    try:
        products = db.query(Product).filter(
            Product.user == user_token,
            Product.date == date,
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
                "user": product.user,
            }
            for product in products
        ]
    finally:
        db.close()
