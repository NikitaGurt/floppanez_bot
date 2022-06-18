from aiogram.types import ReplyKeyboardMarkup
from os import listdir

from config import stories_path

def select_file_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for file in listdir(stories_path):
        keyboard.add(file)

    return keyboard