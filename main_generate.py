import os
from datetime import datetime, timedelta

from app.text_assistant import generate_post
from app.image_assistant import generate_image_from_post
from app.queue_manager import add_to_queue

OUTPUT_DIR = "output"


def run():
    with open("data/topics.txt", "r", encoding="utf-8") as f:
        topics = [t.strip() for t in f.readlines() if t.strip()]

    for i, topic in enumerate(topics):
        print(f"[GEN] {topic}")

        post = generate_post(topic)

        os.makedirs(OUTPUT_DIR, exist_ok=True)
        image_path = f"{OUTPUT_DIR}/post_{i}.png"

        generate_image_from_post(post, image_path)

        publish_time = datetime.now() + timedelta(minutes=2 * i)

        add_to_queue(
            text=post,
            image_path=image_path,
            publish_at=publish_time.isoformat()
        )

        print(f"[QUEUE] scheduled at {publish_time}")


if __name__ == "__main__":
    run()