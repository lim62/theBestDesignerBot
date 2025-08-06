from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode
from bot.states import UserMainSG

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(msg: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(UserMainSG.name, mode=StartMode.RESET_STACK)