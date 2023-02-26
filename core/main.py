from fastapi import FastAPI, Body
from pydantic import BaseModel

from core.chat_gpt import get_response

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


class Message(BaseModel):
    message: str


@app.post("/chat")
async def chat(query: Message):
    # print(query)
    message = query.message
    query.message = get_response(message)
    return query


@app.post("/check_data")
async def check_data(data: dict):
    print(f"In check_data, Data: {data}")
    query = data["queryResult"]["queryText"]
    res = {
        "fulfillmentText": get_response(query)
    }
    return res
