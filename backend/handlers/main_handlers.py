from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from menus import *
from states import Form


async def show_main_menu(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.start_menu)
    await message.answer("Hi there! Welcome to FortuneX's Solana Trading Bot!", reply_markup=main_menu_keyboard)


async def ask_token(message: Message, state: FSMContext) -> None:
    await message.answer("Please enter token name(such as: SOL-USDT)!", reply_markup=go_back_main)
    await state.set_state(Form.waiting_for_token_name)
