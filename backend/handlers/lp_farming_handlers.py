from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from menus import *
from states import Form


async def show_lp_farming_menu(message: Message, state: FSMContext) -> None:
    await message.answer("Here is the LP Farming Menu, Choose Your Option!", reply_markup=lp_farming_menu_keyboard)
