import asyncio
from src.db import initialize_database
from src.routers.start import start_router
from src.utils.bot import bot_instance
from src.utils.dispatcher import dispatcher_instance

async def run():
    # Initialize database
    await initialize_database()
    # Include the start router to the dispatcher /src/routers/start.py
    dispatcher_instance.include_router(start_router)
    await dispatcher_instance.start_polling(bot_instance, handle_as_tasks=True, allowed_updates=['message', 'callback_query'])

if __name__ == "__main__":
    
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("Bot stopped")