import logging

from aiogram import *

from asyncio import run

from registrators.send_story_registrator import register_send_story

from registrators.create_story_registrator import register_create_story

from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot("1929642997:AAENEi8tjasTw6PzcuKhVp7i1FwdE_R6xMw", parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    logger.error('Starting bot')

    register_send_story(dp, bot)
    register_create_story(dp)

    await dp.start_polling()



if __name__ == '__main__':
    run(main())

