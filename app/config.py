import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_TEXT = "gpt-4.1-mini"
MODEL_IMAGE = "gpt-image-1"

IMAGE_SIZE = "1024x1024"
OUTPUT_DIR = "output"