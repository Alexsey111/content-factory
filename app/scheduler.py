import schedule
import time
from app.telegram_publisher import publish


def schedule_post(text, image_path, delay_minutes=60):
    schedule.every(delay_minutes).minutes.do(publish, text, image_path)

    while True:
        schedule.run_pending()
        time.sleep(1)