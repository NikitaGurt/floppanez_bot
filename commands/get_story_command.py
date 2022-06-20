from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from database.database import Database
from keyboards.empty_keyboard import empty
from keyboards.get_story_keyboard import get_story_keyboard
from states.get_story_states import GetStoryStates


async def get_story_start(m: Message, state: FSMContext):
    await m.reply("Пожалуйста, выберите название истории.", reply_markup=get_story_keyboard())

    await GetStoryStates.wait_for_title.set()


async def get_story_end(m: Message, state: FSMContext):
    story_title = m.text

    db = Database()

    stories = ["\n"]

    if story_title != 'Все истории':
        story = db.find(story_title)
        stories.append(f"<b>ID</b>: {story[0]}\n"
                     f"<b>TITLE</b>: {story[1]}\n"
                     f"<b>FILE</b>: {story[2]}\n")

    else:
        stories_array = db.find_all()
        for story in stories_array:
            stories.append(f"<b>ID</b>: {story[0]}\n"
                         f"<b>TITLE</b>: {story[1]}\n"
                         f"<b>FILE</b>: {story[2]}\n"
                         f"<b>SEND COUNT</b>: {story[3]}\n"
                            "---------------\n")



    await m.answer("\n".join(stories), reply_markup=empty())

    await state.finish()
