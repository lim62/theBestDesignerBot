from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Row, SwitchTo, Button
from aiogram_dialog.widgets.input import MessageInput
from bot.states import AdminMainSG
from bot.dialogs.admin_dialogs.admin_handlers import mailing_handler
from bot.dialogs.admin_dialogs.admin_getters import (menu_getter,
                                                     contacts_getter,
                                                     database_getter,
                                                     mailing_getter,
                                                     clean_contacts_getter,
                                                     clean_database_getter,
                                                     sure_to_mail_getter)

admin_main_dialog = Dialog(
    Window(
        Format('{text}'),
        Row(
            SwitchTo(text=Format('{contacts_text}'), id='change_contacts', state=AdminMainSG.contacts),
            SwitchTo(text=Format('{database_text}'), id='change_database', state=AdminMainSG.database)
        ),
        Row(
            SwitchTo(text=Format('{mailing_text}'), id='change_mailing', state=AdminMainSG.mailing)
        ),
        getter=menu_getter,
        state=AdminMainSG.menu
    ),
    Window(
        Format('{text}'),
        Row(
            SwitchTo(text=Format('{cancel_text}'), id='cancel_contacts', state=AdminMainSG.menu),
            SwitchTo(text=Format('{delete_text}'), id='delete_contacts', state=AdminMainSG.clean_contacts)
        ),
        getter=contacts_getter,
        state=AdminMainSG.contacts
    ),
    Window(
        Format('{text}'),
        Row(
            SwitchTo(text=Format('{cancel_text}'), id='cancel_database', state=AdminMainSG.menu),
            SwitchTo(text=Format('{delete_text}'), id='delete_database', state=AdminMainSG.clean_database)
        ),
        getter=database_getter,
        state=AdminMainSG.database
    ),
    Window(
        Format('{text}'),
        MessageInput(
            func=mailing_handler
        ),
        Row(
            SwitchTo(text=Format('{cancel_text}'), id='cancel_mailing', state=AdminMainSG.menu)
        ),
        getter=mailing_getter,
        state=AdminMainSG.mailing
    ),
    Window(
        Format('{text}'),
        Row(
            SwitchTo(text=Format('{cancel_text}'), id='cancel_delete_contacts', state=AdminMainSG.menu),
            Button(text=Format('{progress_text}'), id='progress_delete_contacts', on_click=None)
        ),
        getter=clean_contacts_getter,
        state=AdminMainSG.clean_contacts
    ),
    Window(
        Format('{text}'),
        Row(
            SwitchTo(text=Format('{cancel_text}'), id='cancel_delete_database', state=AdminMainSG.menu),
            Button(text=Format('{progress_text}'), id='progress_delete_database', on_click=None)
        ),
        getter=clean_database_getter,
        state=AdminMainSG.clean_database
    ),
    Window(
        Format('{text}'),
        Row(
            SwitchTo(text=Format('{cancel_text}'), id='cancel_doing_mailing', state=AdminMainSG.menu),
            Button(text=Format('{progress_text}'), id='progress_mailing', on_click=None)
        ),
        getter=sure_to_mail_getter,
        state=AdminMainSG.sure_to_mail
    )
)