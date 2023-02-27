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


# Todo: put into separate classes different implementations for diagonflow and conversational
@app.post("/chat")
async def chat(data: dict):
    """
    for conversational in Actions on Google
    https://workaholix.atlassian.net/browse/HC-8

    :param data: json body received
    :return:
    """

    # print(query)
    print(f"data in chat: {data}")
    query = data["intent"]["query"]
    message = get_response(query)
    res = {
        "candidates": [
            {
                "first_simple": {
                    "variants": [
                        {
                            "speech": f"Test reply from Home chat backend for: {query}",
                            "text": f"{message}"
                        }
                    ]
                }
            }
        ]
    }
    return res


@app.post("/check_data")
async def check_data(data: dict):
    print(f"In check_data, Data: {data}")
    query = data["queryResult"]["queryText"]
    res_message = get_response(query)
    res = {
        "fulfillmentText": res_message
    }
    print(f"Response msg: {res_message}")
    return res
