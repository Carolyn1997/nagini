from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers import *

menu_router = Router()


@menu_router.message(Command("show_wallet_menu"))
async def command_show_wallet_menu(message: Message, state: FSMContext) -> None:
    await show_wallet_menu(message, state)


@menu_router.message(Command("show_trade_menu"))
async def command_show_trade_menu(message: Message, state: FSMContext) -> None:
    await show_trade_menu(message, state)


@menu_router.message(Command("show_strategy_menu"))
async def command_show_strategy_menu(message: Message, state: FSMContext) -> None:
    await show_strategy_menu(message, state)


@menu_router.message(Command("show_bots_menu"))
async def command_show_bots_menu(message: Message, state: FSMContext) -> None:
    await show_bots_menu(message, state)


@menu_router.message(Command("show_lp_farming_menu"))
async def command_show_lp_farming_menu(message: Message, state: FSMContext) -> None:
    await show_lp_farming_menu(message, state)


@menu_router.message(Command("show_referral_menu"))
async def command_show_referral_menu(message: Message, state: FSMContext) -> None:
    await show_referral_menu(message, state)


@menu_router.message(Command("show_settings_menu"))
async def command_show_settings_menu(message: Message, state: FSMContext) -> None:
    await show_settings_menu(message, state)


@menu_router.callback_query()
async def callback_query_handler(message: Message, state: FSMContext) -> None:
    button_message = message.data
    message = message.message
    if button_message == "main_menu":  # 展示主菜单
        await show_main_menu(message, state)

    if button_message == "wallet_menu":  # 展示钱包
        await show_wallet_menu(message, state)
    elif button_message == "show_default_wallet":
        await show_default_wallet(message, state)
    elif button_message == "set_default_wallet":
        await set_default_wallet(message, state)
    elif button_message == "reset_default_wallet":
        await reset_default_wallet(message, state)
    elif button_message == "show_sniper_wallet":
        await show_sniper_wallet(message, state)
    elif button_message == "set_sniper_wallet":
        await set_sniper_wallet(message, state)
    elif button_message == "reset_sniper_wallet":
        await reset_sniper_wallet(message, state)

    if button_message == "trade_menu":  # 展示交易菜单
        await show_trade_menu(message, state)
    elif button_message == "swap_handler":
        await swap_handler(message, state)
    elif button_message == "search_positon":
        await search_positon(message, state)
    elif button_message == "limit_orders":
        await limit_orders(message, state)
    elif button_message == "swap_menu":
        await show_swap_menu(message, state)
    elif button_message == "copy_trade_menu":
        await show_copy_trade_menu(message, state)
    elif button_message == "set_slippage":
        await set_slippage(message, state)
    elif button_message.startswith("buy_"):
        swapData = {
            "amount": float(button_message.split("_")[1]),
            "action": "buy"
        }
        print(swapData)
        await state.update_data(swapData=swapData)
        await start_transaction(message, state)
    elif button_message.startswith("sell_"):
        swapData = {
            "amount": float(button_message.split("_")[1]),
            "action": "sell"
        }
        print(swapData)
        await state.update_data(swapData=swapData)
        await start_transaction(message, state)
    elif button_message == "show_follow_wallet":
        await show_follow_wallet(message, state)
    elif button_message == "add_follow_wallet":
        await add_follow_wallet(message, state)
    elif button_message == "remove_follow_wallet":
        await remove_follow_wallet(message, state)

    if button_message == "strategy_menu":  # 展示策略菜单
        await show_strategy_menu(message, state)
    elif button_message == "bots_menu":  # 展示交易机器人菜单
        await show_bots_menu(message, state)
    elif button_message == "lp_farming_menu":  # 展示流动性挖矿菜单
        await show_lp_farming_menu(message, state)
    elif button_message == "referral_menu":  # 展示推荐菜单
        await show_referral_menu(message, state)
    elif button_message == "referral_link":
        await referral_link(message, state)
    elif button_message == "referral_rewards":
        await referral_rewards(message, state)
    elif button_message == "referral_history":
        await referral_history(message, state)
    elif button_message == "settings_menu":  # 展示设置菜单
        await show_settings_menu(message, state)
    elif button_message == "ask_token":  # AI 代币投资建议查询
        await ask_token(message, state)  # 查询代币信息绘制箱体图

    # elif button_message == "set_wallet":
    #     await set_wallet(message, state) #set wallet wait for private key
    # elif button_message == "show_wallet":
    #     await show_wallet_data(message, state) #show wallet data
    # elif button_message == "reset_wallet":
    #     await reset_wallet(message, state) #reset wallet data
    # elif button_message == "main_menu":
    #     await main_menu(message, state) #show main menu
    # elif button_message == "swap_menu":
    #     await swap_menu(message, state) #show swap menu
    # elif button_message == "copy_trade_menu":
    #     await copy_trade_menu(message, state) #show copy trade menu
    # elif button_message == "transaction_menu":
    #     await transaction_menu(message, state) #show transaction menu
    # elif button_message == "ask_token":
    #     await ask_token(message, state) # 查询代币信息绘制箱体图
    # elif button_message == "help_menu":
    #     await help_menu(message, state) #show help menu
    # elif button_message == "set_slippage":
    #     #call set_slippage function
    #     await set_slippage(message, state)
    # elif button_message.startswith("buy_"):
    #     swapData = {
    #         "amount": float(button_message.split("_")[1]),
    #         "action": "buy"
    #     }
    #     print(swapData)
    #     await state.update_data(swapData=swapData)
    #     await start_transaction(message, state)
    # elif button_message.startswith("sell_"):
    #     #call sell function
    #     swapData = {
    #         "amount": float(button_message.split("_")[1]),
    #         "action": "sell"
    #     }
    #     print(swapData)
    #     await state.update_data(swapData=swapData)
    #     await start_transaction(message, state)
    # elif button_message == "view_follow_wallet":
    #     await view_follow_wallet(message, state)
    # elif button_message == "add_follow_wallet":
    #     await add_follow_wallet(message, state)
    # elif button_message == "remove_follow_wallet":
    #     await remove_follow_wallet(message, state)
    # elif button_message == "view_last_transaction":
    #     #call view_last_transaction function
    #     await message.edit_text("Here is the Last Transaction are: -> transaction data", reply_markup=transaction_menu_keyboard)
    # elif button_message == "view_last_10_transaction":
    #     #call view_last_10_transaction function
    #     await message.edit_text("Here is the Last 10 Transaction are: -> transaction data", reply_markup=transaction_menu_keyboard)
    # else:
    #     await message.edit_text(f"Unknown callback data: {button_message}")
