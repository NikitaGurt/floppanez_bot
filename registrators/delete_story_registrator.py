from aiogram import Dispatcher
from aiogram.dispatcher.filters import IDFilter

from commands.delete_story_command import *
from config import ADMIN_ID


def register_delete_story(dp: Dispatcher):
    dp.register_message_handler(delete_story_start, IDFilter(user_id=ADMIN_ID), commands=['delete_story'], state='*')
    dp.register_message_handler(delete_story_confirm, state=DeleteStoryStates.wait_for_title)
    dp.register_message_handler(delete_story_end, state=DeleteStoryStates.wait_for_confirm)
