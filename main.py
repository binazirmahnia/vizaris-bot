from bot_handlers import build_application
from config import TELEGRAM_BOT_TOKEN
from logger import setup_logger
import sys

setup_logger()

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("Missing TELEGRAM_BOT_TOKEN")
        sys.exit(1)

    app = build_application()
    print("🚀 Vizaris PRO SaaS running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
