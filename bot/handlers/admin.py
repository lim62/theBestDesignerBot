from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode
from bot.states import AdminMainSG

admin_router = Router()

@admin_router.message(CommandStart())
async def admin_cmd_start(msg: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(AdminMainSG.menu, mode=StartMode.RESET_STACK)
