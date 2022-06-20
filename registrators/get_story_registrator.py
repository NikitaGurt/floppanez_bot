from aiogram import Dispatcher
from aiogram.dispatcher.filters import IDFilter

from commands.get_story_command import *
from config import ADMIN_ID


def register_get_story(dp: Dispatcher):
    dp.register_message_handler(get_story_start, IDFilter(user_id=ADMIN_ID), commands=['get_story'], state='*')
    dp.register_message_handler(get_story_end, state=GetStoryStates.wait_for_title)
