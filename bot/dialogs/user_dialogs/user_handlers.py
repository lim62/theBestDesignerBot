from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput
from fluentogram import TranslatorRunner

async def name_handler(
    msg: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    await dialog_manager.next()

async def age_handler(
    msg: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    await dialog_manager.next()

async def story_handler(
    msg: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    await dialog_manager.next()

async def design_handler(
    msg: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str
) -> None:
    await dialog_manager.next()

async def no_text(
    msg: Message,
    widget: MessageInput,
    dialog_manager: DialogManager
) -> None:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    await msg.answer(i18n.user.no.text())