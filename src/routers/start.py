from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from src.utils.states import ParentStates, ChildStates
from src.handlers.start_menu.messages import handle_start
from src.handlers.start_menu.callbacks import handle_start_menu_callbacks
from src.handlers.task.callbacks import handle_task_callback

# router for handling commands and callbacks
start_router = Router()

## /start command handler
# When user sends /start command, this function is triggered
# The state parameter is used to manage the FSM for the user session
@start_router.message(CommandStart()) # Decorator for the router
async def start(message: Message, state: FSMContext):
    await handle_start(message, state) # -> /src/handlers/start_menu/messages.py

# Handles callback queries when the user is in the `ParentStates.start`
@start_router.callback_query(ParentStates.start)
async def start_menu_callbacks(callback: CallbackQuery, state: FSMContext):
    await handle_start_menu_callbacks(callback, state) # -> /src/handlers/start_menu/callbacks.py

# Handles callback queries when the user is in the `ChildStates.task`
@start_router.callback_query(ChildStates.task)
async def task_callbacks(callback: CallbackQuery, state: FSMContext):
    await handle_task_callback(callback, state) # -> /src/handlers/task/callbacks.py