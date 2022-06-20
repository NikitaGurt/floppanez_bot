from aiogram.dispatcher.filters.state import State, StatesGroup


class DeleteStoryStates(StatesGroup):
    wait_for_title = State()
    wait_for_confirm = State()
