from aiogram.types import ReplyKeyboardMarkup

from database.database import Database


def delete_story_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    db = Database()

    for story in db.find_all():
        keyboard.add(story[1])


    return keyboard

def confirm_delete_story_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Я согласен")
    keyboard.add("Я не согласен")

    return keyboard
