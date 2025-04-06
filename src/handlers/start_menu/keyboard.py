from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message

async def start_keyboard(message: Message = None, callback: CallbackQuery = None) -> None:
    # If a message object is provided
    if message:
        username = message.from_user.username
    # If a callback object is provided
    elif callback:
        username = callback.from_user.username
    
    # Text to be displayed in the message
    text = (
        f"Hi @{username}! \n\n"
        f'You can edit this message from /src/handlers/start_menu/keyboard.py file'
    )
    # Keyboard buttons
    buttons = [
        [InlineKeyboardButton(text='Click me', callback_data='CLICK')],
        [InlineKeyboardButton(text='Simple task', callback_data='TASK')],
        [InlineKeyboardButton(text='Check database', callback_data='DB')]
    ]
    # Reply markup with the defined buttons
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    if message:
        # If a message object is provided, send a new message with the specified text and keyboard
        await message.answer(
            text=text,  # The text content of the message
            reply_markup=keyboard  # The reply markup (keyboard) to attach to the message
        )
        
    elif callback:
        # If a callback query object is provided, edit the existing message with the specified text and keyboard
        await callback.message.answer(
            text=text,  # The updated text content of the message
            reply_markup=keyboard  # The updated reply markup (keyboard) to attach to the message
        )