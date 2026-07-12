import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TELEGRAM_BOT_TOKEN")

if token:
    print("Token loaded successfully.")
else:
    print("Failed to load token. Please check your .env file.")