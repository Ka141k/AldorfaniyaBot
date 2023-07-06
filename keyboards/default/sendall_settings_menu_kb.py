from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sendall_settings_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

sendall_settings_btn = KeyboardButton('новости бота/реклама')
back_btn = KeyboardButton('Назад')

sendall_settings_menu.add(sendall_settings_btn, back_btn)