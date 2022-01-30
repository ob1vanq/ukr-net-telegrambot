import asyncio
import logging
import time
import json
from datetime import datetime

from loader import bot
from data.config import CHANEL
from .keeping import keeper
from .parsing import parser
from .decorate import decorator

import os


async def post(*args, **kwargs):
    is_new, recent_id = keeper.chek_new(*args, **kwargs)
    if is_new:
        for id in recent_id:
            data = keeper.upload(*args).get(id)
            string = decorator.decorate(link=data.get("link"), news=data["news"],
                                        publisher=data["publisher"], title=args[0])
            await bot.send_message(chat_id=CHANEL, text=string, parse_mode="HTML")


async def run():
    logging.info("Функция парсинга активирована")

    if not os.listdir(os.path.abspath(os.curdir) + "/handlers/cache"):
        keeper.save("main", url=parser.main)

    while True:
        await post("main", url=parser.main)
        time.sleep(60)


