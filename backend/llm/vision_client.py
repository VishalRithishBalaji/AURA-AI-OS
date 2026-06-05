import base64
import requests


async def ask_vision(
    image_path: str,
    prompt: str
):

    with open(
        image_path,
        "rb"
    ) as f:

        image_data = base64.b64encode(
            f.read()
        ).decode()

    response = requests.post(

        "http://localhost:11434/api/generate",

        json={

            "model": "llava",

            "prompt": prompt,

            "images": [
                image_data
            ],

            "stream": False
        }
    )

    data = response.json()

    print("\n===================")
    print("VISION RAW RESPONSE")
    print("===================")
    print(data)

    if "response" in data:
        return data["response"]

    if "message" in data:
        return data["message"]["content"]

    return str(data)