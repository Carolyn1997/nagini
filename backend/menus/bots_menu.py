from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_bots_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="GMGN Bot", callback_data="gmgn_bot")],
        [InlineKeyboardButton(text="AVE Bot", callback_data="ave_bot")],
        [InlineKeyboardButton(text="⬅️ 返回", callback_data="main_menu")]
    ])


def go_back_bots_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="bots_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard
