from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter


# Кастомный фильтр, для группового чата
class IsGroup(BoundFilter):
	async def check(self, message: Message):
		group_types = ['group', 'supergroup']
		return message.chat.type in group_types