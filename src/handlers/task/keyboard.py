from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def stop_task_keyboard():
    # Keyboard button
    button = [
        [InlineKeyboardButton(text='Stop Task', callback_data='STOP')]
    ]
    # Return markup with the button
    return InlineKeyboardMarkup(inline_keyboard=button)