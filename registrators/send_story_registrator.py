from handlers.send_story_handlers import *

from aiogram import Dispatcher, Bot
from aiogram.dispatcher.filters import IDFilter

from config import ADMIN_ID

def register_send_story(dp: Dispatcher, bot: Bot):
    get_bot(bot)
    dp.register_message_handler(send_story_chat, IDFilter(user_id=ADMIN_ID), commands=['send_story'], state='*')
    dp.register_message_handler(send_story_file, state=SendStates.wait_for_chat)
    dp.register_message_handler(send_story_title, state=SendStates.wait_for_file)
    dp.register_message_handler(send_story_send_count, state=SendStates.wait_for_title)
    dp.register_message_handler(send_story_end, state=SendStates.wait_for_send_count)
