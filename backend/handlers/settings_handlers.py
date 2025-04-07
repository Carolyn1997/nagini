from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from menus import *


async def show_settings_menu(message: Message, state: FSMContext) -> None:
    await message.answer("Here is the Settings Menu, Choose Your Option!", reply_markup=settings_menu_keyboard)
