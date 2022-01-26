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


@dp.message_handler(Command("statistic"), AdminFilter())
async def post_statistic(message: types.Message):

    with open(keeping.keeper.filename.format("statistic"), "r") as file:
        info = json.load(file)

    counter = info["counter"]
    data = info["data"]

    await message.answer(text=f"Дата: {data}\nОпубликовано за сегодня: {counter}")
