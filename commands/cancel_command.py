from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.empty_keyboard import empty


async def cmd_cancel(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=empty())
