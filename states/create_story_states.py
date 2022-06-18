from aiogram.dispatcher.filters.state import State, StatesGroup

class CreateStates(StatesGroup):
    wait_for_title = State()
    wait_for_file = State()