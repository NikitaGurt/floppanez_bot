from aiogram.types import Message, ReplyKeyboardRemove

from aiogram.dispatcher import FSMContext

from states.create_story_states import CreateStates
from keyboards.create_story_keyboard import *

from database.models.story import Story
from database.database import Database

async def create_story_title(m: Message):
    await m.reply("Bыберите файл с историей.", reply_markup=select_file_keyboard())
    await CreateStates.next()

async def create_story_file(m: Message, state: FSMContext):
    if m.text not in listdir(stories_path):
        await m.answer('Пожалуйста, выберите файл, используя клавиатуру ниже.')
        return

    await state.update_data({'file': m.text})

    await CreateStates.wait_for_file.set()
    await m.answer('Теперь введите название истории.', reply_markup=ReplyKeyboardRemove())

async def create_story_end(m: Message, state: FSMContext):
    await state.update_data({'title': m.text})

    user_data = await state.get_data()

    file = user_data['file']
    title = user_data['title']

    new_story = Story(title, file)
    new_story.save()

