from aiogram.types import Message, ChatPermissions

from filters import IsGroup
from loader import dp
from utils.misc import rate_limit

from datetime import datetime, timedelta

# mute group command
@rate_limit(limit=3)
@dp.message_handler(IsGroup(), is_chat_admin=True, commands=['mute'], commands_prefix='!')
async def mute_cmd(message: Message):
	if not message.reply_to_message:
		await message.reply("ℹ Эта команда должна быть ответом на сообщение!")
		return

	command_args = message.text.split(' ')
	print(len(command_args))
	
	if len(command_args) < 2:
		until_date = datetime.now() + timedelta(minutes=1)

		await message.bot.delete_message(message.chat.id, message.message_id)
		await message.bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date, )
	
	elif len(command_args) == 2:
		until_date = datetime.now() + timedelta(seconds=int(command_args[1]))

		await message.bot.delete_message(message.chat.id, message.message_id)
		await message.bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date)