from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.handlers.start_menu.keyboard import start_keyboard
from src.utils.states import ParentStates

async def handle_start(message: Message, state: FSMContext) -> None:
    # Sets the user's state to `ParentStates.start`
    await state.set_state(ParentStates.start)

    # Send a message with the start menu keyboard
    await start_keyboard(message)