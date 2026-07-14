import os

from dotenv import load_dotenv

from telegram.ext import Application

load_dotenv()

Token = os.getenv("TELEGRAM_BOT_TOKEN")

if Token is None:
    print("Failed to load token. Please check your .env file.")
else:
    print("Token loaded successfully.")


application = Application.builder().token(Token).build()

if application is None:
    print("Failed to create application. Please check your token and try again.")
else:
    print("Application created successfully.")