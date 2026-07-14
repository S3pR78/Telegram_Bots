# Study Assistant Bot

A Telegram bot that helps students organize tasks, track deadlines, and manage their study routine.

## Project Goal

The goal of this project is to build a practical study assistant while learning how to develop Telegram bots with Python.

## Planned Features

* Add study tasks
* Display open tasks
* Mark tasks as completed
* Organize tasks by subject
* Set deadline reminders
* Show basic study statistics

## Planned Commands

```text
/start    Start the bot
/help     Show available commands
/addtask  Add a new task
/tasks    Show open tasks
/done     Mark a task as completed
```

## Technologies

* Python
* python-telegram-bot
* SQLite
* pytest

## Project Structure

```text
Study_Assistant_Bot/
├── src/
│   └── bot.py
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .bot-env
source .bot-env/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Create the environment file:

```bash
cp .env.example .env
```

Add your Telegram bot token to `.env`:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

Run the bot:

```bash
python src/bot.py
```

## Status

This project is currently under development.
