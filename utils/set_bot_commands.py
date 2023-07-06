from aiogram import types


# Функция настройки команд бота | Setting bot commands function
async def set_default_commands(dp):
	await dp.bot.set_my_commands([
		types.BotCommand('start', 'Запустить бота')
	])