from aiogram.types import Message

from filters import IsGroup
from loader import dp, db, bot
from utils.misc import rate_limit

@rate_limit(limit=3)
@dp.message_handler(IsGroup(), commands=['transaction'], commands_prefix='!')
async def transaction_cmd(message: Message):
	if not message.reply_to_message:
		await message.reply("ℹ Эта команда должна быть ответом на сообщение!")
		return

	await message.reply('transaction')