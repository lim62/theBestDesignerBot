from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from bot.states import AdminMainSG

async def mailing_handler(
    msg: Message,
    widget: MessageInput,
    dialog_manager: DialogManager
) -> None:
    await dialog_manager.switch_to(AdminMainSG.sure_to_mail)