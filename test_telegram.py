from app.telegram_publisher import publish

print("Запуск тестового поста...")
publish("Тестовый пост 🚀", "output/0/image.png")
print("Пост отправлен!")
