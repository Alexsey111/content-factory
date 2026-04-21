import time
from app.queue_manager import get_pending_posts, mark_as_sent
from app.telegram_publisher import publish


def run():
    print("[WORKER] started")

    while True:
        posts = get_pending_posts()

        for post in posts:
            print("[DEBUG] processing:", post["text"][:30])

            success = publish(post["text"], post["image_path"])

            if success:
                mark_as_sent(post)
                print("[DONE] marked as sent")
            else:
                print("[SKIP] not marked as sent")

        time.sleep(30)


if __name__ == "__main__":
    run()