from aiogram.types import Message, ReplyKeyboardRemove

from aiogram.dispatcher import FSMContext

from states.send_story_states import SendStates
from keyboards.send_story_keyboard import *

from os import listdir

from config import chats, stories_path

from functions import *

bot: Bot


def get_bot(bot_instance: Bot):
    global bot
    bot = bot_instance


async def send_story_chat(m: Message, state: FSMContext):
    try:
        await m.reply('Выберите чат для отправки: ', reply_markup=select_chat_keyboard())
        await SendStates.wait_for_chat.set()


    except Exception as e:
        await m.reply(f"Произошла ошибка!\n{e}")


async def send_story_file(m: Message, state: FSMContext):
    if m.text not in chats:
        await m.answer('Пожалуйста, выберите чат, используя клавиатуру ниже.')
        return

    await state.update_data({'chat': m.text})

    await SendStates.next()
    await m.answer('Теперь выберите файл с историей.', reply_markup=select_file_keyboard())


async def send_story_title(m: Message, state: FSMContext):
    if m.text not in listdir(stories_path):
        await m.answer('Пожалуйста, выберите файл, используя клавиатуру ниже.')
        return

    await state.update_data({'file': m.text})

    await SendStates.next()
    await m.answer('Теперь введите название истории.', reply_markup=ReplyKeyboardRemove())


async def send_story_send_count(m: Message, state: FSMContext):
    await state.update_data({'title': m.text})

    await SendStates.next()
    await m.answer('Теперь введите стартовое значение слов для отправки.')


async def send_story_end(m: Message, state: FSMContext):
    global bot
    await state.update_data({'send_count': int(m.text)})

    user_data = await state.get_data()

    chat = user_data['chat']
    file = user_data['file']
    title = user_data['title']
    send_count = user_data['send_count']

    file_content: str

    filename, ext = file.split('.')

    if ext == 'docx':
        file_content = get_file_content_docx(file)
    elif ext == 'txt':
        file_content = get_file_content(file)

    await send_story(bot, chat, file, title)


    await state.finish()


