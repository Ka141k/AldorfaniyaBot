from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Test')

register_btn = KeyboardButton('Регистрация')
register_menu.insert(register_btn)