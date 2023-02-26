import os
import openai

# secret = "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"
# secret = "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"
secret = "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"
open_ai_key = "open_ai_key"
os.environ[open_ai_key] = secret
openai.api_key = os.environ[open_ai_key]


def get_response(prompt, model="text-davinci-003", max_tokens=150):
    """

    """
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
    #     temperature=0.5,
    #     max_tokens=60,
    #     top_p=1.0,
    #     frequency_penalty=0.5,
    #     presence_penalty=0.0,
    #     stop=["You:"]
    # )

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0.9,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    message = response.choices[0]['text']
    # print(response.choices[0]['text'])
    return message

#
# while True:
# ques = input()
# print(get_response(ques))
