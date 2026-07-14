import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application , CommandHandler , MessageHandler, filters

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
    user = update.effective_user
    await update.message.reply_text(f"Hello {user.first_name}! I am your bot. How can I assist you today?")

async def bye(update: Update, context):
    user = update.effective_user
    await update.message.reply_text(f"Goodbye {user.first_name}! Have a great day!")

async def answer_message(update: Update, context):
    user = update.effective_user
    message = update.message.text
    await update.message.reply_text(f"{user.first_name}, you said: {message}")


application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("bye", bye))
application.add_handler(MessageHandler(filters.TEXT, answer_message))

application.run_polling()

