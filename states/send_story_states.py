from aiogram.dispatcher.filters.state import State, StatesGroup

class SendStates(StatesGroup):
    wait_for_chat = State()
    wait_for_file = State()
    wait_for_title = State()
    wait_for_send_count = State()