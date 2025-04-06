import asyncio
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from src.utils.states import ChildStates, ParentStates
from src.handlers.start_menu.keyboard import start_keyboard
from src.handlers.task.keyboard import stop_task_keyboard
from src.db.tables.users import get_user_by_id

# Handles callback queries from the start menu
async def handle_start_menu_callbacks(callback: CallbackQuery, state: FSMContext)-> None:
    # Check if the callback data is 'CLICK'.
    if callback.data == 'CLICK':
        await handle_click()

    # Check if the callback data is 'TASK'.
    elif callback.data == 'TASK':
        await handle_task(callback, state)

    elif callback.data == 'DB':
        await handle_db_click(callback, state)

async def handle_db_click(callback: CallbackQuery, state: FSMContext) -> None:
    user_info = await get_user_by_id(callback.from_user.id)
    if user_info:
        id, user_id, username, lang = user_info[0], user_info[1], user_info[2], user_info[3]

    text = (
        f'User found from database!\n\n'
        f'Id {id}\n'
        f'Username: {username}\n'
        f'Telegram Userid: <code>{user_id}</code>\n'
        f'Language: {lang}'
    )
    await callback.message.answer(text=text, parse_mode='HTML')
    await start_keyboard(callback=callback)
    await state.set_state(ParentStates.start)

async def handle_click():
    print("Hello from Telegram!")

async def handle_task(callback: CallbackQuery, state: FSMContext) -> None:
    # Number of iterations the task will perform
    iter = 15

    async def task():
        # Set the state to ChildStates.task for the duration of the loop. See ./start_menu/task/callbacks.py
        await state.set_state(ChildStates.task)
        # Get the reply keyboard
        keyboard = await stop_task_keyboard()

        # Iterate
        for i in range(iter):
            # Edit the message text for every loop
            await callback.message.edit_text(
                f'This text will be edited {iter - i} times and then start keyboard is returned.',
                reply_markup=keyboard # Set the reply keyboard
            )
            await asyncio.sleep(1)

        # Once the loop is finished, send the start keyboard
        await start_keyboard(callback=callback)
        
        # Reset the state to the ParentStates.start
        await state.set_state(ParentStates.start)

    # Add the task to the event loop
    await asyncio.create_task(coro=task(), name='example_task')