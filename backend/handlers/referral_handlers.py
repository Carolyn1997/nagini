from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from config import TG_URL
from menus import *
from database.db import *


async def show_referral_menu(message: Message, state: FSMContext) -> None:
    await message.answer("Here is the Referral Menu, Choose Your Option!", reply_markup=referral_menu_keyboard)


async def referral_link(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    ref_link = f"{TG_URL}?start=ref_{user_id}"
    await message.edit_text(f'🔗 你的推荐链接：\n{ref_link}', reply_markup=referral_menu_keyboard, parse_mode=None)


async def referral_rewards(message: Message, state: FSMContext) -> None:
    await message.edit_text("Referral rewards is comming soon ...", reply_markup=referral_menu_keyboard)


async def referral_history(message: Message, state: FSMContext) -> None:
    userId = message.from_user.id
    ref_list = await get_my_referrals(userId)
    if ref_list:
        await message.edit_text(f'📊 你的推荐用户ID: {ref_list}', reply_markup=referral_menu_keyboard)
    else:
        await message.edit_text(f'❌ 你还没有推荐任何用户。', reply_markup=referral_menu_keyboard)
