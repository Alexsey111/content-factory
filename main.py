from app.text_assistant import generate_post
from app.image_assistant import generate_image_from_post
from app.telegram_publisher import publish

def run():
    topic = "как избавиться от лишних уточнений в скобках"

    post = generate_post(topic)

    image_path = "output/post.png"
    generate_image_from_post(post, image_path)

    publish(post, image_path)


if __name__ == "__main__":
    run()