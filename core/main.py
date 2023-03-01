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
async def chat(data: dict, tokens=2000):
    """
    for conversational in Actions on Google
    https://workaholix.atlassian.net/browse/HC-8

    :param tokens:
    :param data: json body received
    :return:
    """
    print(f"{tokens=}")
    # print(query)
    # todo: check if tokens int
    tokens = int(tokens)
    print(f"{tokens=}, {data=}")
    session = data["session"]
    query = data["intent"]["query"]
    message = get_response(query, max_tokens=tokens)
    res = {
        "session": session,
        "prompt": {
            "override": False,
            "firstSimple": {
                "speech": f"Rishabh says, {message}",
                "text": f"{message}"
            }
        }
    }
    print(f"Returned message: {message}")
    return res


@app.post("/check_data")
async def check_data(data: dict):
    # For Diagonflow
    print(f"In check_data, Data: {data}")
    query = data["queryResult"]["queryText"]
    res_message = get_response(query)
    res = {
        "fulfillmentText": res_message
    }
    print(f"Response msg: {res_message}")
    return res
