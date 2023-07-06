from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

delete_account_answers_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

agree_btn = KeyboardButton('Да, я подтверждаю удаление своего аккаунта')
disagree_btn = KeyboardButton('Нет, Я не собираюсь этого делать.')

delete_account_answers_menu.add(agree_btn, disagree_btn)