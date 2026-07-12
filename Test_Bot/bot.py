import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application , CommandHandler
load_dotenv()

token = os.getenv("TELEGRAM_BOT_TOKEN")


application = Application.builder().token(token).build()

if token:
    print("Token loaded successfully.")
else:
    print("Failed to load token. Please check your .env file.")

if application:
    print("Application created successfully.")
else:
    print("Failed to create application. Please check your token and try again.")


async def start(update: Update, context):
    print("Start command received.")


application.add_handler(CommandHandler("start", start))

