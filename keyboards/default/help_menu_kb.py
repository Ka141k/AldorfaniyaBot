from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

help_menu = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

for_all_btn = KeyboardButton('Для всех')
support_btn = KeyboardButton('Тех поддержка')
back_btn = KeyboardButton('Назад')

help_menu.add(for_all_btn, support_btn, back_btn)