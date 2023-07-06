from aiogram import executor

from utils.set_bot_commands import set_default_commands
from loader import dp
import filters, middlewares

async def on_startup(dp):
	
	filters.setup(dp)
	middlewares.setup(dp)

	await set_default_commands(dp)

	print('Бот запущен!)')


if __name__ == '__main__':
	from handlers import dp
	
	executor.start_polling(dp, skip_updates = True, on_startup=on_startup)
