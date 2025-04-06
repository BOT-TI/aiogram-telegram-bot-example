import unittest
from unittest.mock import MagicMock, AsyncMock, patch
from src.utils.states import ParentStates
from src.utils.dispatcher import dispatcher_instance
from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from src.routers.start import handle_start, start_router
from src.handlers.start_menu.callbacks import handle_start_menu_callbacks

class Test(unittest.IsolatedAsyncioTestCase):

    # SetUp
    async def asyncSetUp(self):
        self.bot = MagicMock(spec=Bot)
        self.dp = MagicMock(spec=dispatcher_instance)
        self.dp.include_router(start_router)
        await self.dp.start_polling(self.bot)
        self.user = MagicMock(spec=types.User)
        self.user.username = 'test_user'
        self.user.id = 123
        self.user.language_code = 'FI'

    @patch("src.handlers.start_menu.messages.start_keyboard", new_callable=AsyncMock)
    @patch("src.handlers.start_menu.messages.get_user_by_id", new_callable=AsyncMock)
    @patch("src.handlers.start_menu.messages.insert_user", new_callable=AsyncMock)
    async def test_start_handler(self, mock_insert_user, mock_get_user_by_id, mock_start_keyboard):
        mock_get_user_by_id.return_value = None
        message = MagicMock(spec=types.Message)
        message.chat = MagicMock(spec=types.Chat)
        message.text = "/start"
        
        message.from_user = self.user
        message.answer = AsyncMock()

        state = AsyncMock(spec=FSMContext)
        _handle_start = await handle_start(message, state)
        mock_get_user_by_id.assert_called_once_with(self.user.id)
        state.set_state.assert_called_once_with(ParentStates.start)
        mock_insert_user.assert_called_once_with(self.user.id, self.user.username, self.user.language_code)
        mock_start_keyboard.assert_called_once_with(message)
        assert _handle_start is None

    @patch("src.handlers.start_menu.callbacks.handle_click", new_callable=AsyncMock)
    async def test_click_callback(self, mock_handle_click):
        
        callback = MagicMock(spec=types.CallbackQuery)
        callback.chat = MagicMock(spec=types.Chat)
        callback.data = 'CLICK'
        state = AsyncMock(spec=FSMContext)
        func = await handle_start_menu_callbacks(callback, state)
        mock_handle_click.assert_called_once()
        assert func is None

    @patch("src.handlers.start_menu.callbacks.handle_task", new_callable=AsyncMock)
    async def test_task_callback(self, mock_handle_task):
        callback = MagicMock(spec=types.CallbackQuery)
        callback.chat = MagicMock(spec=types.Chat)
        callback.data = 'TASK'
        callback.from_user = self.user
        callback.from_user.id = 123
        callback.message = MagicMock(spec=types.Message)
        callback.message.edit_text = AsyncMock(spec=types.Message)
        callback.message.answer = AsyncMock()
        state = AsyncMock(spec=FSMContext)
        func = await handle_start_menu_callbacks(callback, state)
        mock_handle_task.assert_called_with(callback, state)
        assert func is None

    @patch("src.handlers.start_menu.callbacks.handle_db_click", new_callable=AsyncMock)
    async def test_db_click_callback(self, mock_handle_db_click):
        callback = MagicMock(spec=types.CallbackQuery)
        callback.chat = MagicMock(spec=types.Chat)
        callback.data = 'DB'
        callback.from_user = self.user
        callback.from_user.id = 123
        callback.message = MagicMock(spec=types.Message)
        callback.message.edit_text = AsyncMock(spec=types.Message)
        callback.message.answer = AsyncMock()
        state = AsyncMock(spec=FSMContext)
        func = await handle_start_menu_callbacks(callback, state)
        mock_handle_db_click.assert_called_with(callback, state)
        assert func is None

if __name__ == '__main__':
    unittest.main()
