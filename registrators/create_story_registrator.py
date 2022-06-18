from handlers.create_story_handlers import *

from aiogram import Dispatcher
from aiogram.dispatcher.filters import IDFilter

from config import ADMIN_ID

def register_create_story(dp: Dispatcher):
   dp.register_message_handler(create_story_title, IDFilter(user_id=ADMIN_ID), commands=['create_story'])
   dp.register_message_handler(create_story_file, state=CreateStates.wait_for_title)
   dp.register_message_handler(create_story_end, state=CreateStates.wait_for_file)