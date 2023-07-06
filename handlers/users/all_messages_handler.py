from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, LabeledPrice, PreCheckoutQuery, ContentType
from aiogram.dispatcher import FSMContext

from loader import dp, db, bot
from filters import IsPrivate
from keyboards.inline import play_menu
import keyboards.default as nav
from states import ReNickname, ReAvatar, RubyDonate
from data import PAYMENTS_TOKEN

# all messages handler
@dp.message_handler(IsPrivate())
async def all_messages_handler(message: Message):
	match message.text:
		case 'Регистрация':
			if db.get_signup(message.from_user.id) == 'setnickname':
				await message.answer('Наш мир тебя заинтересовал? Круть!\nКак мне к тебе обращайться?')
			else:
				await message.answer('Вы уже зарегистрированы!\nМожете возвращаться обратно в группу.')
		case 'Профиль':
			if message.from_user.id == 5879046152:
				await message.answer('Всё информация:\n'
									f'Псевдоним: {db.get_nickname(message.from_user.id)}\n'
									f'Айди: {db.get_player_id(message.from_user.id)}\n'
									f'Роль: Хранитель\n'
									f'Рубины: {db.get_player_ruby(message.from_user.id)}\n'
									f'Карма: {db.get_player_karma(message.from_user.id)}\n')
			elif message.from_user.id == 913656911:
				await message.answer('Всё информация:\n'
									f'Псевдоним: {db.get_nickname(message.from_user.id)}\n'
									f'Айди: {db.get_player_id(message.from_user.id)}\n'
									f'Роль: Строитель\n'
									f'Рубины: {db.get_player_ruby(message.from_user.id)}\n'
									f'Карма: {db.get_player_karma(message.from_user.id)}\n')
			else:	
				await message.answer('Всё информация:\n'
									f'Псевдоним: {db.get_nickname(message.from_user.id)}\n'
									f'Айди: {db.get_player_id(message.from_user.id)}\n'
									f'Роль: Участник\n'
									f'Рубины: {db.get_player_ruby(message.from_user.id)}\n'
									f'Карма: {db.get_player_karma(message.from_user.id)}\n')
		case 'Настройки':
			await message.answer('Меню натроек', reply_markup=nav.settings_menu)
		case 'Донат':
			# markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
			# markup.insert(KeyboardButton('Отмена'))

			await message.answer('<b>Покупка рубинов</b>\n\nДля покупки рубинов напишите сюда: @Kai41k') # , reply_markup=markup
			# await RubyDonate.ruby_count.set()
		case 'Помощь':
			kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
			kb.add(KeyboardButton('Команды'), KeyboardButton('Назад'))

			await message.answer('Помощь по боту', reply_markup=kb)
		case 'Команды':
			if message.from_user.id == 913656911 or message.from_user.id == 5879046152:
				await message.answer('Помощь по командам бота для админов', reply_markup=nav.help_admin_menu)
			else:
				await message.answer('Помощь по командам бота', reply_markup=nav.help_menu)
		case 'Для всех':
			await message.answer('<b>Помощь по командам бота</b>\n'
								 '<i>*Ответ на сообщение*</i> <code>!mute_pls</code> - начинает опрос на мут\n'
								 '<code>!rnd</code> - загадывает случайное число от 1 до 100, пример: <i><code>{player-name}</code> загадал(-а) число <code>{случайное число от 1 до 100}</code> из 100.</i>')
		case 'Для админов':
			await message.answer('<b>Помощь по командам админов бота</b>\n'
								 '<i>*Ответ на сообщение*</i> <code>!mute</code> <code>{time (sec)}</code>\n'
								 '<i>*Ответ на сообщение*</i> <code>!kick</code>\n'
								 '<i>*Ответ на сообщение*</i> <code>!ban</code>')
		case 'Тех поддержка':
			await message.answer(f'Тех. поддержка: @AldorfaniyaSupportBot')

		case 'Изменить псевдоним (100 рубинов)':
			if int(db.get_player_ruby(message.from_user.id)) >= 100:
				await message.answer('Введите новый псевдоним:')
				await ReNickname.new_nickname.set()

			else:
				await message.answer('Недостаточно рубинов, для совершения данного действия!')
		case 'Аккаунт':
			await message.answer('Настройки аккаунта', reply_markup=nav.account_settings_menu)
		case 'Добавить/Сменить аву':
			await message.answer('Пришлите аву:')
			await ReAvatar.new_avatar.set()
		case 'Удалить аккаунт':
			await message.answer('Ты действительно этого хочешь!?( 😳😢', reply_markup=nav.delete_account_answers_menu)
		case 'Да, я подтверждаю удаление своего аккаунта':
			db.delete_account(message.from_user.id)
			await message.answer('Ваш аккаунт удалён успешно!)', reply_markup=nav.main_menu)
		case 'Нет, Я не собираюсь этого делать.':
			await message.answer('Хорошо)', reply_markup=nav.account_settings_menu)
		case 'Назад':
			await message.answer('Вы вернулись в главное меню!)', reply_markup=nav.main_menu)
		case 'Рассылка':
			await message.answer('Настройки рассылки', reply_markup=nav.sendall_settings_menu)
		case 'новости бота/реклама':
			await message.answer('Выберите действие!', reply_markup=nav.sendall_switch_menu)
		case 'Включить':
			await message.answer('Рассылка включена', reply_markup=nav.main_menu)
		case 'Выключить':
			await message.answer('Рассылка отключена', reply_markup=nav.main_menu)
		case _:
			if db.get_signup(message.from_user.id) == "setnickname":
				if len(message.text) > 20:
					await message.answer('Никнейм не должен превышать 20 символов')
				elif "@" in message.text or '/' in message.text:
					await message.answer('Вы ввели запрещённый символ в нике')
				else:
					db.set_nickname(message.from_user.id, message.text)
					db.set_signup(message.from_user.id, "done")
					
					await message.answer('Регистрация прошла успешно!\nМожете возвращаться обратно в группу.', reply_markup=nav.play_menu)
					
					with open('rules.docx', 'rb') as file:
						await bot.send_document(message.from_user.id, file, caption='Но перед началом, не забудьте ознакомиться с правилами', reply_markup=nav.main_menu)

# rechange nickname state handler
@dp.message_handler(state=ReNickname.new_nickname)
async def reset_nickname(message: Message, state: FSMContext):
	if message.text == 'Отмена':
		await state.finish()
		await message.answer('Действие отменено', reply_markup=nav.account_settings_menu)
	else:
		await state.update_data(new_nickname=message.text)

		new_ruby = db.get_player_ruby(user_id=message.from_user.id)
		new_ruby = new_ruby - 100
		db.set_player_ruby(message.from_user.id, new_ruby)
		db.set_nickname(message.from_user.id, message.text)

		await message.answer('Вы успешно изменили псевдоним!)', reply_markup=nav.account_settings_menu)
		await state.finish()


@dp.message_handler(content_types=['photo','document'], state=ReAvatar.new_avatar)
async def reset_avatar(message: Message, state: FSMContext):
	if message.text == 'Отмена':
		await state.finish()
		await message.answer('Действие отменено', reply_markup=nav.account_settings_menu)
	else:
		await state.update_data(new_avatar=message.photo[0].file_id)
		
		db.set_player_avatar(message.from_user.id, message.photo[0].file_id)
		await message.answer('Вы успешно применили аву!)', reply_markup=nav.account_settings_menu)
		
		await state.finish()

		await message.answer('test')