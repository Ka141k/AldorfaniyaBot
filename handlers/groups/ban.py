from aiogram.types import Message

from filters import IsGroup
from loader import dp
from utils.misc import rate_limit

# ban group command
@rate_limit(limit=3)
@dp.message_handler(IsGroup(), is_chat_admin=True, commands=['ban'], commands_prefix='!')
async def ban_cmd(message: Message):
	if not message.reply_to_message:
		await message.reply("ℹ Эта команда должна быть ответом на сообщение!")
		return

	await message.bot.delete_message(message.chat.id, message.message_id)
	await message.bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)


