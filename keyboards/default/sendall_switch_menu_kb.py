from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sendall_switch_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

on_settings_btn = KeyboardButton('Включить')
off_settings_btn = KeyboardButton('Выключить')
back_btn = KeyboardButton('Назад')

sendall_switch_menu.add(on_settings_btn, off_settings_btn, back_btn)