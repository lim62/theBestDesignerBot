from aiogram.fsm.state import State, StatesGroup

class AdminMainSG(StatesGroup):
    menu = State()
    contacts = State()
    database = State()
    mailing = State()
    clean_contacts = State()
    sure_to_mail = State()