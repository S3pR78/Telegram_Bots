import os

from dotenv import load_dotenv

load_dotenv()

Token = os.getenv("TELEGRAM_BOT_TOKEN")

if Token is None:
    print("Failed to load token. Please check your .env file.")
else:
    print("Token loaded successfully.")