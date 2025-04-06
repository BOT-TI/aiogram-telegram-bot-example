import aiosqlite

async def insert_user(user_id: int, user_name: str, location: str):
    async with aiosqlite.connect("database.db") as db:
        await db.execute(
            "INSERT INTO users (user_id, user_name, language) VALUES (?, ?, ?)",
            (user_id, user_name, location)
        )
        await db.commit()

async def get_user_by_id(user_id: int):
    async with aiosqlite.connect("database.db") as db:
        async with db.execute("SELECT id, user_id, user_name, language FROM users WHERE user_id = ?", (user_id,)) as cursor:
            user = await cursor.fetchone()
            return user