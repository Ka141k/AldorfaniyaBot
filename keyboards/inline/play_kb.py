from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

play_menu = InlineKeyboardMarkup(row_width=1)

play_btn = InlineKeyboardButton(text='Играть', url='https://t.me/+FmNYcf9-IKwwNTQy')
play_menu.insert(play_btn)