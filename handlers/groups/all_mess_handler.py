from aiogram.types import Message

from loader import dp, iconic_symbols
from filters import IsGroup

# all messages handler
@dp.message_handler(IsGroup())
async def all_mess_handler(message: Message):
	for symbol in iconic_symbols:	
		if symbol in message.text:
			pass

# poll messages handler
@dp.message_handler(IsGroup(), content_types=['poll'])
async def poll_mess_handler(message: Message):
	print(message)

# all messages handler
@dp.edited_message_handler(IsGroup())
async def all_edited_mess_handler(message: Message):
	print(message)
	await message.reply('Ааа... ля ты крыска, сообщения редактируешь, да?)')


