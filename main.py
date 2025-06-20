import json
from fastapi import FastAPI, Header, Query
from pydantic import BaseModel
from app.chatgpt import get_ai_response
from app.db_connect import add_product, get_products
app = FastAPI()


class BigText(BaseModel):
    text: str
    user_token: str


@app.post('/save_data')
def save_data(payload: BigText):
    text = payload.text
    user_token = payload.user_token
    for _ in range(5):
        try:
            macros_raw_data = json.loads(get_ai_response(text))
            for product in macros_raw_data:
                add_product(product, user_token)
            break
        except json.decoder.JSONDecodeError:
            print('Trying again...')


@app.get('/get_data')
def get_data(
        date: str = Query(...),
        user_token: str = Header(...)
    ):
    return get_products(date, user_token) #returns json
