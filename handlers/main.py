import asyncio
import logging
import time

from loader import bot
from data.config import CHANEL
from .keeping import keeper
from .parsing import parser
from .decorate import decorator

import schedule
import threading
import os


def statistic(recent_id: list, delete: bool = False):
    import json
    from datetime import datetime
    counter = 0

    if not delete:
        with open(keeper.filename.format("statistic"), "r", encoding="utf-8") as file:
            info = json.load(file)
        counter = int(info["counter"]) + len(recent_id)

    with open(keeper.filename.format("statistic"), "w", encoding="utf-8") as file:
        json.dump(dict(counter=counter, data=str(datetime.now().strftime("%A, %d-%m-%y | %H:%M:%S"))), file, indent=4)


async def post(*args, **kwargs):
    is_new, recent_id = keeper.chek_new(*args, **kwargs)
    if is_new:
        statistic(recent_id)
        for id in recent_id:
            data = keeper.upload(*args).get(id)
            string = decorator.decorate(link=data.get("link"), news=data["news"],
                                        publisher=data["publisher"], title=args[0])
            await bot.send_message(chat_id=CHANEL, text=string, parse_mode="HTML")


async def run():
    logging.info("Функция парсинга активирована")
    while True:
        await post("main", url=parser.main)
        schedule.run_pending()
        time.sleep(60)


def main():
    if not os.listdir(os.path.abspath(os.curdir) + "/handlers/cash"):
        keeper.save("main", url=parser.main)

    schedule.every().day.at("00:01").do(statistic, recent_id=[], delete=True)

    loop = asyncio.new_event_loop()
    threading.Thread(daemon=True, target=loop.run_forever).start()

    async def sleep_and_run():
        await run()
    asyncio.run_coroutine_threadsafe(sleep_and_run(), loop)


if __name__ == "__main__":
    main()



