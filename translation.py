# coding=utf-8

import requests

def translate(source, direction):
    url = "http://api.interpreter.caiyunai.com/v1/translator"

    # WARNING, this token is a test token for new developers,
    # and it should be replaced by your token
    token = "3975l6lr5pcbvidl6jl2"

    payload = {
        "source": source,
        "trans_type": direction,
        "request_id": "demo",
        "detect": True,
    }

    headers = {
        "content-type": "application/json",
        "x-authorization": "token " + token,
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()["target"]


if __name__ == "__main__":
    source = ["Lingocloud is the best translation service.", "彩云小译は最高の翻訳サービスです"]
    target = translate(source, "auto2zh")

    print(target)