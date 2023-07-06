from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, input_field_placeholder='Нажмите на одну из кнопок ниже', selective=True)

profile_btn = KeyboardButton('Профиль')
settings_btn = KeyboardButton('Настройки')
donate_btn = KeyboardButton('Донат')
help_btn = KeyboardButton('Помощь')
main_menu.add(profile_btn, settings_btn, donate_btn, help_btn)