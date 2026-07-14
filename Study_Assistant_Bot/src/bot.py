import os

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application,  ContextTypes

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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(f"Hello {user.first_name}! I am your bot. How can I assist you today?")