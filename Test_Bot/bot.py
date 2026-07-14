import os
import random

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
    
    if  not message.isdigit():
        await update.message.reply_text("Please send a number to play the game.")
        return
    
    secret_number = context.user_data['secret_number']
    message = int(message)

    if secret_number is None:
        await update.message.reply_text('you have to inizialize the game first with /game')
        return
    
    if(message == secret_number):
        await update.message.reply_text(f"{user.first_name} won the game the number was {secret_number}")
        return

    if( message < secret_number):
        await update.message.reply_text("my number is bigger")
    else:
        await update.message.reply_text("my number is smaller")
    


async def game(update: Update, context):
    secret_number = random.randint(1, 10)
    user = update.effective_user
    context.user_data['secret_number'] = secret_number
    await update.message.reply_text(f"{user.first_name}, let's play a game! i choose number between 1 and 10. can you guess it?")
    print(f"Secret number for {user.first_name}: {secret_number}")  # For debugging purposes


application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("bye", bye))
application.add_handler(CommandHandler("game", game))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer_message))

application.run_polling()

