from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter


# Кастомный фильтр, для приватного чата
class IsPrivate(BoundFilter):
	async def check(self, message: Message):
		return message.chat.type == 'private'