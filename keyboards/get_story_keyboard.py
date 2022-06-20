from aiogram.types import ReplyKeyboardMarkup

from database.database import Database


def get_story_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    db = Database()

    for story in db.find_all():
        keyboard.add(story[1])

    keyboard.add("Все истории")
    return keyboard
