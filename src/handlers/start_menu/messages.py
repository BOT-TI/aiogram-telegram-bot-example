from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.handlers.start_menu.keyboard import start_keyboard
from src.db.tables.users import insert_user, get_user_by_id
from src.utils.states import ParentStates

# /start command callback
async def handle_start(message: Message, state: FSMContext) -> None:
    if message.text == '/start':
        user_exist = await get_user_by_id(message.from_user.id)
        if not user_exist:
            await insert_user(message.from_user.id, message.from_user.username, message.from_user.language_code)
        await state.set_state(ParentStates.start)

        # Send a message with the start menu keyboard
        await start_keyboard(message)