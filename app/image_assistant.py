from openai import OpenAI
from app.config import OPENAI_API_KEY, MODEL_IMAGE
from app.visual_extractor import extract_visual_elements
from app.style_prompt import STYLE_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_image_from_post(post_text: str, output_path: str):
    headline, phrases = extract_visual_elements(post_text)

    prompt = f"""
{STYLE_PROMPT}

POST TOPIC:
{post_text[:500]}

HEADLINE:
"{headline}"

KEY PHRASES:
{phrases}
"""

    response = client.images.generate(
        model=MODEL_IMAGE,
        prompt=prompt,
        size="1024x1024"
    )

    import base64
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(response.data[0].b64_json))