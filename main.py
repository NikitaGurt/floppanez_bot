import logging
from asyncio import run, set_event_loop_policy, WindowsSelectorEventLoopPolicy

from aiogram import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from registrators.cancel_command_registrator import register_cancel_command
from registrators.create_story_registrator import register_create_story
from registrators.get_story_registrator import register_get_story
from registrators.send_story_registrator import register_send_story
from registrators.delete_story_registrator import register_delete_story

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
    register_get_story(dp)
    register_cancel_command(dp)
    register_delete_story(dp)


    await dp.start_polling()



if __name__ == '__main__':
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    run(main())

