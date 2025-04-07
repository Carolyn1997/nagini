import math
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from database.db import *
from swap import Swap
from config import RPC_URL
from menus import *
from states import Form


async def show_trade_menu(message: Message, state: FSMContext) -> None:
    await message.answer("Here is the Trade Menu, Choose Your Option!", reply_markup=trade_menu_keyboard)


async def show_swap_menu(message: Message, state: FSMContext) -> None:
    await message.answer("Here is the Swap Menu, Choose Your Option!", reply_markup=swap_menu_keyboard)


async def show_copy_trade_menu(message: Message, state: FSMContext) -> None:
    await message.answer("Here is the Copy Trade Menu, Choose Your Option!", reply_markup=copy_trade_menu_keyboard)


async def swap_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    userData = await get_user(user_id=userId)
    if userData.get("default_private_key") == "":
        await message.edit_text("Please set your wallet first", reply_markup=go_back_trade)
    else:
        await message.edit_text("Please Enter The Contract Address of the Token You Want to Buy")
        # 假设这是等待输入购买代币地址的状态
        await state.set_state(Form.waiting_for_contrace_address)


async def search_positon(message: Message, state: FSMContext) -> None:
    await message.answer("Print position is comming soon!")


async def limit_orders(message: Message, state: FSMContext) -> None:
    await message.answer("limit orders is comming soon!")


async def set_slippage(message: Message, state: FSMContext) -> None:
    await message.edit_text("Please enter your slippage tolerance? Enter a number \nFor Example 5%, Please Enter 5", reply_markup=go_back_trade)
    await state.set_state(Form.set_slippage)  # 假设这是等待滑点输入的状态


async def start_transaction(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    userData = await get_user(user_id=userId)
    token_address = data.get("token_address")
    swapData = data.get("swapData")
    if userData.get("default_private_key") is None or token_address is None:
        await message.answer("Please set your default wallet first", reply_markup=wallet_menu_keyboard)
    else:
        await message.edit_text(f"Starting Transaction for {swapData.get('amount')} {data.get('token_info')['symbol']} {swapData.get('action')}ing.......\nPlease Wait....")
        swapClient = Swap(RPC_URL, userData.get("default_private_key"))
        token_address = data.get("token_address")
        if swapData.get("action") == "buy":
            print("Buying")
            amount = float(swapData.get("amount"))
            slippage = userData.get("slippage")
            tansactionStatus, transactionId = await swapClient.swap_token(
                input_mint="So11111111111111111111111111111111111111112",
                output_mint=token_address,
                amount=amount,
                slippage_bps=slippage
            )
        elif swapData.get("action") == "sell":
            print("Selling")
            product = (float(swapData.get("amount")) * data.get("account_token_info")
                       ["balance"]["float"])  # rounding down to near 2 decimal places
            slippage = userData.get("slippage")
            rounded_down_product = math.floor(product * 100) / 100.0
            tansactionStatus, transactionId = await swapClient.swap_token(
                input_mint=token_address,
                output_mint="So11111111111111111111111111111111111111112",
                amount=float(rounded_down_product),
                slippage_bps=slippage
            )
        else:
            await message.answer("Invalid Action")
            await state.set_state(Form.start_menu)

        if tansactionStatus:
            await message.answer(f"TX ID:{transactionId}\nTransaction sent: [View on Solana Explorer](https://explorer.solana.com/tx/{transactionId})\n--------------\nNow Checking for Transaction Status", parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True, reply_markup=main_menu_keyboard)
            swap_status, swap_msg = await swapClient.swap_status(transactionId)
            if swap_status:
                await message.answer(f"Transaction SUCCESS! | [View on Solana Explorer](https://explorer.solana.com/tx/{transactionId})", parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
            else:
                await message.answer(f"Check Transaction Status FAILED! Please Retry. {swap_msg}", reply_markup=main_menu_keyboard)
        else:
            await message.answer(f"Transaction failed: {transactionId}", reply_markup=main_menu_keyboard)

    await state.set_state(Form.start_menu)


async def show_follow_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    userData = data.get("userData")
    print(userData, type(userData))
    follow_wallets = userData['monitor_wallet']
    if follow_wallets:
        wallets_str = follow_wallets.replace(";", "\n")
        await message.answer(f"Here are the wallets you're following:\n{wallets_str}", reply_markup=copy_trade_menu_keyboard)
    else:
        await message.answer("You are not following any wallets yet.", reply_markup=go_back_copy_trade)


async def add_follow_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    userData = data.get("userData")
    print(userData, type(userData))
    await message.answer(f"You have followed Wallet Address:{userData['monitor_wallet']} \n\nPlease enter the wallet you want to follow?", reply_markup=go_back_trade)
    await state.set_state(Form.waiting_for_follow_wallet)  # 等待输入加入监控的钱包地址


async def remove_follow_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    userData = data.get("userData")
    print(userData, type(userData))
    if userData["monitor_wallet"]:
        await message.answer(f"You have followed Wallet Address:{userData['monitor_wallet']} \n\nPlease enter the wallet you want to unfollow?", reply_markup=go_back_trade)
        # 等待输入取消监控的钱包地址
        await state.set_state(Form.waiting_for_unfollow_wallet)
    else:
        await message.edit_text(f"You have not follow any Wallet Address!", reply_markup=go_back_trade)
