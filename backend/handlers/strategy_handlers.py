from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from menus import *
from states import Form


async def show_strategy_menu(message: Message, state: FSMContext) -> None:
    await message.answer("Here is the Strategy Menu, Choose Your Option!", reply_markup=strategy_menu_keyboard)
