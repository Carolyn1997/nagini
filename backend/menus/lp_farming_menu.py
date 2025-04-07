from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_lp_farming_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="查看收益", callback_data="view_earnings")],
        [InlineKeyboardButton(text="添加流动性", callback_data="add_liquidity")],
        [InlineKeyboardButton(text="移除流动性", callback_data="remove_liquidity")],
        [InlineKeyboardButton(text="⬅️ 返回", callback_data="main_menu")]
    ])


def go_back_lp_farming_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="lp_farming_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard
