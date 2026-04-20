import base64
from openai import OpenAI
from app.config import OPENAI_API_KEY, MODEL_IMAGE, IMAGE_SIZE

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_image(prompt: str, output_path: str):
    response = client.images.generate(
        model=MODEL_IMAGE,
        prompt=prompt,
        size=IMAGE_SIZE
    )

    image_base64 = response.data[0].b64_json

    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_base64))