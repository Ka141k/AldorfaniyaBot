from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

account_settings_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

account_settings_btn = KeyboardButton('Изменить псевдоним (100 рубинов)')
add_rechange_avatar_btn = KeyboardButton('Добавить/Сменить аву')
delete_account_btn = KeyboardButton('Удалить аккаунт')
back_btn = KeyboardButton('Назад')

account_settings_menu.add(account_settings_btn, add_rechange_avatar_btn, delete_account_btn, back_btn)