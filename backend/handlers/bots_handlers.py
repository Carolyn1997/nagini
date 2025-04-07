from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from menus import *
from states import Form


async def show_bots_menu(message: Message, state: FSMContext) -> None:
    await message.answer("Here is the Bots Menu, Choose Your Option!", reply_markup=bots_menu_keyboard)
