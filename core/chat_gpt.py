import os
import openai
from openai.error import Timeout

secret = os.environ.get("OPENAI_KEY", "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")
open_ai_key = "open_ai_key"
os.environ[open_ai_key] = secret
openai.api_key = os.environ[open_ai_key]
default_timeout = 4  # seconds


def get_response(prompt, model="text-davinci-003", max_tokens=150):
    """

    """
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=0.5,
            max_tokens=max_tokens,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["You:"],
            timeout=default_timeout,
            request_timeout=default_timeout
        )
        message = response.choices[0]['text']
    except Timeout:
        message = "took longer to think than google has patience for, please try again, maybe with a query " \
                  "with a potentially faster/smaller answer? Or try our mobile app ;)"

    # response = openai.Completion.create(
    #     model=model,
    #     prompt=prompt,
    #     temperature=0.9,
    #     max_tokens=max_tokens,
    #     top_p=1,
    #     frequency_penalty=0.0,
    #     presence_penalty=0.6,
    #     stop=[" Human:", " AI:"]
    # )

    # print(response.choices[0]['text'])
    return message

#
# while True:
# ques = input()
# print(get_response(ques))
