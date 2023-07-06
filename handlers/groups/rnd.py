from aiogram.types import Message

from filters import IsGroup
from loader import dp
from utils.misc import rate_limit

from random import randint

# rnd group command
@rate_limit(limit=3)
@dp.message_handler(IsGroup(), commands=['rnd'], commands_prefix='!')
async def rnd_cmd(message: Message):
	await message.reply(f'<i><a href="tg://user?id={message.from_user.id}">{message.from_user.id}</a> загадал(-а) число <code>{randint(0, 101)}</code> из 100</i> ')