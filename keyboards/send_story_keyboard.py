from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from os import listdir

from config import chats, stories_path



def select_chat_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for chat in chats:
        keyboard.add(chat)

    return keyboard

def select_file_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for file in listdir(stories_path):
        keyboard.add(file)

    return keyboard

def select_send_count_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('0')
