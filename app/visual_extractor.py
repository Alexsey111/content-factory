from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def extract_visual_elements(post_text: str):
    prompt = f"""
Извлеки из текста:

1. Короткий заголовок (3-6 слов)
2. 3-5 ключевых фраз (короткие, 2-4 слова)

Текст:
{post_text}

Формат ответа:

HEADLINE: ...
KEY_PHRASES: фраза1 / фраза2 / фраза3
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    content = response.choices[0].message.content

    headline = content.split("HEADLINE:")[1].split("\n")[0].strip()
    phrases = content.split("KEY_PHRASES:")[1].strip()

    return headline, phrases