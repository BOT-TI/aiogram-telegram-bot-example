# Aiogram 3.11.0 Telegram Bot Example

This repository contains a template for a Telegram bot built with Aiogram 3.11.0. The bot features a simple structure for handling updates and tasks.

**Note:** This template does not include logging or storage. For production use, consider adding logging and/or storage solutions and using environment variables for configuration.

## Table of Contents
- [Structure](#structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)

## Structure

Overview of the structure:

```plaintext
src/
│
├── utils/
│   ├── bot.py           
│   ├── config_loader.py
│   ├── dispatcher.py   
│   └── states.py        
│
├── handlers/
│   ├── start_menu/
│   │   ├── callbacks.py
│   │   ├── keyboard.py 
│   │   └── messages.py
│   └── task/
│       ├── callbacks.py
│       └── keyboard.py 
│
├── routers/
│   └── start.py         
│
├── config.json          
├── main.py              
├── readme.md            
└── requirements.txt     
└── .gitignore           
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

    - Open the `config.json` file and replace `"YOUR_BOT_TOKEN_HERE"` with your actual bot token:

      ```json
      {
          "bot": {
              "token": "YOUR_BOT_TOKEN_HERE"
          }
      }
      ```

### Running the Bot

To start the bot, use the following command:

```bash
python3 main.py
```