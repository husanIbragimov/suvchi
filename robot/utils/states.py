from aiogram.fsm.state import State, StatesGroup

class UserState(StatesGroup):
    full_name = State()
    lang = State()
    phone_number = State()
    code = State()