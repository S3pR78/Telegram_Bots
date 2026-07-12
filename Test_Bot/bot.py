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
    await update.message.reply_text("Hello! I am your bot. How can I assist you today?")

async def bye(update: Update, context):
    await update.message.reply_text("Goodbye! Have a great day!")


application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("bye", bye))

application.run_polling()

