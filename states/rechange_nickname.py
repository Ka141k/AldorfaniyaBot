from aiogram.dispatcher.filters.state import StatesGroup, State


class ReNickname(StatesGroup):
    new_nickname = State()