import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv('ChatGPTApi'))
prompt = os.getenv('prompt')

def get_ai_response(products): #noqa: D103
    response = client.responses.create(
        model = "gpt-4.1-nano",
        input = prompt + products,
    )
    return response.output_text
