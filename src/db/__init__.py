import aiosqlite

async def initialize_database():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("PRAGMA journal_mode = WAL;")
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id BIGINT NOT NULL,
                user_name TEXT,
                language TEXT
            );
        """)
        await db.commit()