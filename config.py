import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

BOT_NAME = "Vizaris"
VERSION = "3.0 PRO"
ENV = os.getenv("ENV", "production")
