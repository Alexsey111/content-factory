import json
import os
from datetime import datetime

QUEUE_FILE = "storage/queue.json"


def load_queue():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_queue(queue):
    os.makedirs("storage", exist_ok=True)
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)


def add_to_queue(text, image_path, publish_at):
    queue = load_queue()

    queue.append({
        "text": text,
        "image_path": image_path,
        "publish_at": publish_at,
        "status": "pending"
    })

    save_queue(queue)


def get_pending_posts():
    queue = load_queue()
    now = datetime.now()

    ready = []
    for item in queue:
        if item["status"] == "pending":
            publish_time = datetime.fromisoformat(item["publish_at"])
            if publish_time <= now:
                ready.append(item)

    return ready


def mark_as_sent(item):
    queue = load_queue()

    for q in queue:
        if q == item:
            q["status"] = "sent"

    save_queue(queue)