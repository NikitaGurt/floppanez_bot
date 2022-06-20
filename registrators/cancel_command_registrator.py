from aiogram import Dispatcher
from aiogram.dispatcher.filters import IDFilter

from commands.cancel_command import *
from config import ADMIN_ID


def register_cancel_command(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, IDFilter(user_id=ADMIN_ID), commands=['cancel'], state='*')
