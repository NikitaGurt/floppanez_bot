from aiogram.dispatcher.filters.state import State, StatesGroup


class GetStoryStates(StatesGroup):
    wait_for_title = State()
