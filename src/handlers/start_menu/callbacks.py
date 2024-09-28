import asyncio
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from src.utils.states import ChildStates, ParentStates
from src.handlers.start_menu.keyboard import start_keyboard
from src.handlers.task.keyboard import stop_task_keyboard
from src.utils.dispatcher import dispatcher_instance

# Handles callback queries from the start menu
async def handle_start_menu_callbacks(callback: CallbackQuery, state: FSMContext):
    # Check if the callback data is 'CLICK'. If it is, call the handle_click function.
    if callback.data == 'CLICK':
        await handle_click()

    # Check if the callback data is 'TASK'. If it is, call the handle_task function.
    elif callback.data == 'TASK':
        await handle_task(callback, state)

async def handle_click():
    print("Hello from Telegram!")

async def handle_task(callback: CallbackQuery, state: FSMContext):
    # Number of iterations the task will perform
    iter = 15

    async def task():
        # Set the state to ChildStates.task for the duration of the loop. See ./start_menu/task/callbacks.py
        await state.set_state(ChildStates.task)
        
        # Get the reply markup
        keyboard = await stop_task_keyboard()

        # Iterate
        for i in range(iter):
            # Edit the message text for every loop
            await callback.message.edit_text(
                f'This text will be edited {iter - i} times and then start keyboard is returned.',
                reply_markup=keyboard # Set the reply markup
            )
            # Pause for 1 second
            await asyncio.sleep(10)

        # Once the loop is finished and not stopped, send the start keyboard
        await start_keyboard(callback=callback)
        
        # Reset the state to the ParentStates.start
        await state.set_state(ParentStates.start)

    # Add the task to the event loop
    await asyncio.create_task(coro=task(), name='example_task')