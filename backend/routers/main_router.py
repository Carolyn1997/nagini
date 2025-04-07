from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from states import Form
from menus import *
from database.db import *

main_router = Router()

ALL_USERS_DATA = get_all_users()


@main_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.start_menu)
    userId = message.from_user.id
    userData = await get_user(user_id=userId)
    args = message.text.split()[1:]  # 获取 /start 后面的参数
    print(userData, type(userData))

    if userData:
        get_user_data = await get_user(user_id=userId)
        ALL_USERS_DATA[userId] = get_user_data  # 将用户数据存储在字典中
        await message.answer("Welcome back! Choose Your Option!", reply_markup=main_menu_keyboard)
    else:
        if args and args[0].startswith('ref_'):
            referrer_id = int(args[0].split('_')[1])
            # 添加推荐关系
            await insert_referral(referrer_id, userId)
            await message.answer(f'🎉 你通过推荐链接加入！推荐者ID: {referrer_id}')
        else:
            await message.answer('👋 欢迎使用本 Bot！')
        await insert_user(user_id=userId, default_wallet_address="", default_private_key="",
                          sniper_wallet_address="", sniper_private_key="",
                          trades="", slippage=10, monitor_wallet="")
        # 创建新用户，将用户数据存储在字典中
        ALL_USERS_DATA[userId] = await get_user(user_id=userId)
        await message.answer("Hi there! Welcome to FortuneX's Solana Trading Bot!", reply_markup=main_menu_keyboard)
    await state.update_data(userId=userId)
    await state.update_data(userData=userData)
