# Aiogram 3.11.0 Telegram Bot Example

This repository contains a template for a Telegram bot built with Aiogram 3.11.0. The bot features a simple structure for handling updates and tasks.

**Note:** This template does not include logging or storage. For production use, consider adding logging and/or storage solutions and using environment variables for configuration.

## Table of Contents
- [Structure](#structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Running tests](#running-tests)

## Structure

Overview of the structure:

```plaintext
src/
│
├── db/
│   ├── tables/
│   │   ├── users.py
│   │   └── __init__.py
│
├── handlers/
│   ├── start_menu/
│   │   ├── callbacks.py
│   │   ├── keyboard.py
│   │   └── messages.py
│   ├── task/
│   │   ├── callbacks.py
│   │   ├── keyboard.py
│   │   └── __init__.py
│   └── __init__.py
│
├── routers/
│   ├── start.py
│   └── __init__.py
│
├── utils/
│   ├── bot.py
│   ├── dispatcher.py
│   ├── states.py
│   └── __init__.py
│
├── tests/
│   └── tests.py
│
├── .github/workflows/
│   └── ci.yml
│
├── .env
├── .gitignore
├── main.py
├── readme.md
└── requirements.txt
```

### Prerequisites

- Python 3.x
- Telegram bot token (obtainable from [BotFather](https://t.me/BotFather) on Telegram)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/BOT-TI/aiogram-telegram-bot-example.git
    cd aiogram-telegram-bot-example
    ```

2. **Create a new virtual environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```
    - **Linux/Mac**:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required libraries**:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Set up your bot token**:

    - Create a new .env file in the source folder and add bot token:

      ```plaintext
      BOT_TOKEN = token_here
      ```

### Running the Bot

To start the bot, use the following command:

```bash
python main.py
```

## Running tests

To run tests, use the following command:

```bash
pytest ./tests/tests.py
```