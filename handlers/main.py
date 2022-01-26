from loader import bot
from data.config import CHANEL
from .keeping import keeper
from .parsing import parser
from .decorate import decorator

import schedule
import os


def statistic(recent_id):
    import json
    from datetime import datetime

    with open(keeper.filename.format("statistic"), "r") as file:
        info = json.load(file)
    counter = info["counter"] + len(recent_id)

    with open(keeper.filename.format("statistic"), "w") as file:
        json.dump(dict(counter=counter, data=datetime.now()), file, indent=4)


async def post(*args, **kwargs):
    is_new, recent_id = keeper.chek_new(*args, **kwargs)
    if is_new:
        statistic(recent_id)
        for id in recent_id:
            data = keeper.upload(*args).get(id)
            string = decorator.decorate(link=data.get("link"), news=data["news"],
                                        publisher=data["publisher"], title=args[0])
            await bot.send_message(chat_id=CHANEL, text=string, parse_mode="HTML" )


async def main():

    if not os.listdir(os.path.abspath(os.curdir) + "/handlers/cash"):
        keeper.save("main", url=parser.main)
        keeper.save("politics", url=parser.politics)
        keeper.save("economics", url=parser.economics)

    # schedule.every(2).minutes.do(post, "politics", url=parser.politics)
    # schedule.every(10).minutes.do(post, "economics", url=parser.economics)
    schedule.every(1).minutes.do(post, "main", url=parser.main)

    while True:
        await schedule.run_pending()


if __name__ == "__main__":
    main()



