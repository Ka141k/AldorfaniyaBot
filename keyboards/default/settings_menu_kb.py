from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

settings_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

account_settings_btn = KeyboardButton('Аккаунт')
send_all_messages_settings_btn = KeyboardButton('Рассылка')
back_btn = KeyboardButton('Назад')

settings_menu.add(account_settings_btn, send_all_messages_settings_btn, back_btn)