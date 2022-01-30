import logging

from aiogram import executor

from handlers.main import main
from loader import dp
import handlers
from utils.notify_admins import on_startup_notify

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    main()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


