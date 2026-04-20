import os
import pandas as pd

from app.llm import generate_text, parse_output
from app.image_gen import generate_image
from app.config import OUTPUT_DIR


def process_csv(file_path: str):
    df = pd.read_csv(file_path)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for i, row in df.iterrows():
        print(f"[INFO] Processing row {i+1}")

        try:
            result = generate_text(row)
            image_prompt, post_text = parse_output(result)

            row_dir = os.path.join(OUTPUT_DIR, str(i))
            os.makedirs(row_dir, exist_ok=True)

            image_path = os.path.join(row_dir, "image.png")
            text_path = os.path.join(row_dir, "post.txt")

            generate_image(image_prompt, image_path)

            with open(text_path, "w", encoding="utf-8") as f:
                f.write(post_text)

        except Exception as e:
            print(f"[ERROR] Row {i+1}: {e}")