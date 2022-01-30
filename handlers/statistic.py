import json

from aiogram import types
from aiogram.dispatcher.filters import Command
from handlers import keeping
from data.config import ADMINS
from loader import dp

from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        member = str(message.from_user.id)
        return member in ADMINS


@dp.message_handler()
async def post_statistic(message: types.Message):
    await message.answer(
        text="<i>Бот працює на базі інтернет порталу www.ukr.net\n\nАвтор проекту: @engineer_spock"
    )
