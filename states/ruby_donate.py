from aiogram.dispatcher.filters.state import StatesGroup, State


class RubyDonate(StatesGroup):
    ruby_count = State()