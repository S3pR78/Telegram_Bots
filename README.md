# Telegram Bots

A collection of Telegram bot projects built with Python.

This repository is used to learn Telegram bot development step by step and to build larger portfolio projects with clean structure, documentation, testing, and deployment.

## Projects

### Test Bot

A small learning project used to understand the basics of Telegram bot development.

Current topics include:

* Telegram commands
* Message handlers
* User input
* Simple games
* User-specific data with `context.user_data`

Path:

```text
Test_Bot/
```

### Study Assistant Bot

A portfolio project designed to help students organize tasks, deadlines, and study activities.

Planned features include:

* Adding study tasks
* Viewing open tasks
* Marking tasks as completed
* Organizing tasks by subject
* Setting deadline reminders
* Displaying study statistics

Path:

```text
Study_Assistant_Bot/
```

## Technologies

* Python
* python-telegram-bot
* SQLite
* pytest
* Git
* GitHub

## Repository Structure

```text
Telegram_Bots/
├── Test_Bot/
├── Study_Assistant_Bot/
├── .gitignore
└── README.md
```

## Security

Bot tokens and local environment files are not committed to this repository.

Each project uses a local `.env` file for private configuration.

Example:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

## Status

This repository is actively being developed.
