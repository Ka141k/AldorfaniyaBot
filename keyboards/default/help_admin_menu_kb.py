from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

help_admin_menu = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

for_all_btn = KeyboardButton('Для всех')
for_admins_btn = KeyboardButton('Для админов')
support_btn = KeyboardButton('Тех поддержка')
back_btn = KeyboardButton('Назад')

help_admin_menu.add(for_all_btn, for_admins_btn, support_btn, back_btn)