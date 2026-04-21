import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def publish(text, image_path):
    print("[DEBUG] sending to telegram...")
    try:
        with open(image_path, "rb") as img:
            bot.send_photo(
                chat_id=CHAT_ID,
                photo=img,
                caption=text[:1000]
            )

        print("[TELEGRAM] sent OK")
        return True

    except Exception as e:
        print("[TELEGRAM ERROR]", e)
        return False