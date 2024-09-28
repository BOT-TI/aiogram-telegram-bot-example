import asyncio
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from src.utils.states import ParentStates
from src.handlers.start_menu.keyboard import start_keyboard

async def handle_task_callback(callback: CallbackQuery, state: FSMContext):
    # Check if the callback data is 'STOP'. If it is, call the handle_stop_task function.
    if callback.data == 'STOP':
        await handle_stop_task(callback, state)

async def handle_stop_task(callback: CallbackQuery, state: FSMContext):
    # Get the current event loop
    event_loop = asyncio.get_event_loop()
    
    # Retrieve all pending tasks from the event loop
    tasks = [task for task in asyncio.all_tasks(event_loop) if not task.done()]
    
    # Iterate over the pending tasks
    for task in tasks:
        # Check if the task's name matches 'example_task'.
        if task.get_name() == 'example_task':  # Task created in /src/handlers/start_menu/callbacks.py, line 49 | If there is multiple tasks running with the same name, cancels all of them.
            task.cancel()  # Cancel the task
    
    # Reset the state to 'start' after canceling the task
    await state.set_state(ParentStates.start)
    
    # Return the start menu keyboard
    await start_keyboard(callback=callback)