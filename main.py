import asyncio
from src.routers.start import start_router
from src.utils.bot import bot_instance
from src.utils.dispatcher import dispatcher_instance

async def run():
    # Include the start router to the dispatcher /src/routers/start.py
    dispatcher_instance.include_router(start_router)

    try:
        # Start polling
        # 'handle_as_tasks' runs updates in separate tasks, 'allowed_updates' specifies what kinds of updates
        await dispatcher_instance.start_polling(bot_instance, handle_as_tasks=True, allowed_updates=['message', 'callback_query'])

    except KeyboardInterrupt:
        print("Bot stopped")

if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("Bot stopped")