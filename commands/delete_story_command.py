from aiogram.dispatcher import FSMContext
from aiogram.types import Message


from keyboards.empty_keyboard import empty

from keyboards.delete_story_keyboard import *
from states.delete_story_states import DeleteStoryStates


async def delete_story_start(m: Message, state: FSMContext):
    await m.reply("Выберите историю для удаления.", reply_markup=delete_story_keyboard())

    await DeleteStoryStates.wait_for_title.set()


async def delete_story_confirm(m: Message, state: FSMContext):
    title = m.text

    await state.update_data({"title": title})

    await m.answer(f"Вы точно хотите удалить историю {title}?", reply_markup=confirm_delete_story_keyboard())

    await DeleteStoryStates.wait_for_confirm.set()


async def delete_story_end(m: Message, state: FSMContext):
    if m.text == "Я согласен":
        user_data = await state.get_data()
        title = user_data["title"]

        db = Database()

        db.delete(title)

        await m.reply(f"История {title} успешно удалена!")
    else:
        await m.reply("Завершаю процесс удаления истории!", reply_markup=empty())
        await state.finish()

    await state.finish()




