from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from filters import IsGroup
from loader import dp, bot, yes_counter, no_counter, pressed_users
from utils.misc import rate_limit

from asyncio import sleep

# mute_pls group command
@rate_limit(limit=3)
@dp.message_handler(IsGroup(), commands=['mute-pls'], commands_prefix='!')
async def mute_pls_cmd(message: Message):
	if not message.reply_to_message:
		await message.reply("ℹ Эта команда должна быть ответом на сообщение!")
		return
	
	markup = InlineKeyboardMarkup(row_width=2)
	markup.add(InlineKeyboardButton(text='Да', callback_data='mutepls_yes'), InlineKeyboardButton(text='Нет', callback_data='mutepls_no'))
	await message.reply(f'Стоит ли лешить дара речи у @{message.from_user.username}?', reply_markup=markup)

	await sleep(300)
	await bot.send_message(message.chat.id, f'И так @{message.reply_to_message.from_user.username}, {yes_counter} проголосовали чтоб те отрезали язык, а {no_counter} проголосовали противоположно.')

	if yes_counter > no_counter:
		await bot.send_message(message.from_user.id, 'Видемо ты не нравишся им и мне придётся забрать у тебя язык на 10 мигов (это минуты)')
	elif yes_counter < no_counter:
		await bot.send_message(message.from_user.id, 'Я тебя не трону, живи пока)')
	else:
		await bot.send_message(message.from_user.id, 'Голоса равны, поэтому я за мир во всём мире :D')


@dp.callback_query_handler(text_contains=['mutepls_'])
async def mutepls_call(call: CallbackQuery):
	global yes_counter, no_counter

	if call.data[8:] == 'yes':
		if call.from_user.id not in pressed_users:
			pressed_users.append(call.from_user.id)
			yes_counter += 1
	
	elif call.data[8:] == 'no':
		if call.from_user.id not in pressed_users:
			pressed_users.append(call.from_user.id)
			no_counter += 1

