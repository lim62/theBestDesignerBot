from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

async def menu_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    return {
        'text': i18n.admin.menu(),
        'contacts_text': i18n.button.contacts(),
        'database_text': i18n.button.database(),
        'mailing_text': i18n.button.mailing()
    }

async def contacts_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    return {
        'text': i18n.admin.contacts(),
        'delete_text': i18n.button.clear(),
        'cancel_text': i18n.button.cancel()
    }

async def database_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    return {
        'text': i18n.admin.database(),
        'delete_text': i18n.button.clear(),
        'cancel_text': i18n.button.cancel()
    }

async def mailing_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    return {
        'text': i18n.admin.mailing(),
        'cancel_text': i18n.button.cancel()
    }

async def clean_contacts_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    return {
        'text': i18n.admin.clean.contacts(),
        'cancel_text': i18n.button.no(),
        'progress_text': i18n.button.yes()
    }

async def clean_database_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    return {
        'text': i18n.admin.clean.database(),
        'cancel_text': i18n.button.no(),
        'progress_text': i18n.button.yes()
    }

async def sure_to_mail_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    return {
        'text': i18n.admin.sure.to.mail(),
        'cancel_text': i18n.button.no(),
        'progress_text': i18n.button.yes()
    }