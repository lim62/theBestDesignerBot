from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from sqlalchemy.ext.asyncio import AsyncSession
from bot.states import AdminMainSG
from bot.database.requests import select_user, update_user

async def mailing_handler(
    msg: Message,
    widget: MessageInput,
    dialog_manager: DialogManager
) -> None:
    await dialog_manager.switch_to(AdminMainSG.sure_to_mail)

async def delete_handler(
    call: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
) -> None:
    session: AsyncSession = dialog_manager.middleware_data.get('session')
    result = await select_user(session)
    for user in result:
        await update_user(session, user.telegram_id)