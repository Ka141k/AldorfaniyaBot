from aiogram.types import Message

from filters import IsPrivate
from loader import dp, db, bot
from utils.misc import rate_limit
from keyboards.default import main_menu

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), commands=['start'])
async def start_cmd(message: Message):
	the_keeper_nickname = db.get_nickname(5879046152) # Получаем никнейм Хранителя
	# the_builder_nickname = db.get_nickname(913656911) # Получаем никнейм Строителя
	registered_users = db.get_registered_users() # Получаем количество зарегестрированнных пользователей
	group_members = await bot.get_chat_member_count(-1001467007211) # Получаем количество участников в группе

	await message.answer(f'Привет, <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>\n'
						 'Добро пожаловать в Алдорфанию, в мир созданый кубами!\n'
						 f'Текуший Хранитель: <a href="tg://user?id=5879046152">{the_keeper_nickname}</a>\n'
						 f'Строители: <a href="tg://user?id=913656911">Кай</a>\n'
						 f'Зарегистрировано: {registered_users}\n'
						 f'Участники: {group_members}', reply_markup=main_menu)
	
	if not db.user_exists(message.from_user.id):
		all_users = db.get_users()
		all_users += 1
		db.add_user(message.from_user.id, all_users)
	else:
		pass