from aiogram.dispatcher.filters.state import State,StatesGroup

class Kafe(StatesGroup):
    categor = State()
    product = State()
    amount = State()
    