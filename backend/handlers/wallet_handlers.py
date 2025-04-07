from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from menus import *
from database.db import *
from states import Form


async def show_wallet_menu(message: Message, state: FSMContext) -> None:
    await message.answer("Here is the Wallet Menu, Choose Your Option!", reply_markup=wallet_menu_keyboard)


async def show_default_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userData = data.get("userData")
    print(userData)
    if userData.get("default_wallet_address") == "":
        await message.edit_text("You have not set your default wallet yet!", reply_markup=go_back_wallet)
        await state.set_state(Form.wallet_menu)
    else:
        await message.edit_text(f"Default wallet Address: {userData['default_wallet_address']}\nPrivate Key: {userData['default_private_key']}\n", reply_markup=go_back_wallet)


async def set_default_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userData = data.get("userData")
    if userData.get("default_wallet_address"):
        await message.edit_text(f"You have already set your default wallet address!\nWallet Address:{userData['default_wallet_address']}", reply_markup=go_back_wallet)
    else:
        await message.edit_text("Please enter your default private key?", reply_markup=go_back_wallet)
        # 假设这是等待私钥输入的状态
        await state.set_state(Form.waiting_default_private_key)


async def reset_default_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    userData = data.get("userData")
    if userData.get("default_wallet_address"):
        await update_user(user_id=userId, default_wallet_address="", default_private_key="")
        await message.answer(f"You have reset your default wallet data! \n Please Update The Bot with Your New Wallet\nYour Previous Wallet Detail:\nDefault wallet_address:{userData['default_wallet_address']}\ndefault_private_key:{userData['default_private_key']}")
        userData = await get_user(user_id=userId)
        await state.update_data(userData=userData)
    else:
        await message.edit_text("You have not set your default wallet yet!", reply_markup=go_back_wallet)
    await state.clear()
    await state.set_state(Form.wallet_menu)


async def show_sniper_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userData = data.get("userData")
    if userData.get("sniper_wallet_address") == "":
        await message.edit_text("You have not set your sniper wallet yet!", reply_markup=go_back_wallet)
        await state.set_state(Form.wallet_menu)
    else:
        await message.edit_text(f"Sniper wallet Address: {userData['sniper_wallet_address']}\nSniper private Key: {userData['sniper_private_key']}\n", reply_markup=go_back_wallet)


async def set_sniper_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userData = data.get("userData")
    if userData.get("sniper_wallet_address"):
        await message.edit_text(f"You have already set your sniper wallet address!\nSniper wallet Address:{userData['sniper_wallet_address']}", reply_markup=go_back_wallet)
    else:
        await message.edit_text("Please enter your sniper private key?", reply_markup=go_back_wallet)
        await state.set_state(Form.waiting_sniper_private_key)  # 假设这是等待私钥输入的状态


async def reset_sniper_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    userData = data.get("userData")
    if userData.get("sniper_wallet_address"):
        await update_user(user_id=userId, sniper_wallet_address="", sniper_private_key="")
        await message.answer(f"You have reset your sniper wallet data! \n Please Update The Bot with Your New Wallet\nYour Previous Wallet Detail:\nSniper wallet_address:{userData['sniper_wallet_address']}\nSniper private_key:{userData['sniper_private_key']}")
        userData = await get_user(user_id=userId)
        await state.update_data(userData=userData)
    else:
        await message.edit_text("You have not set your sniper wallet yet!", reply_markup=go_back_wallet)
    await state.clear()
    await state.set_state(Form.wallet_menu)
