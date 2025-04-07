from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_strategy_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Strategy 1", callback_data="strategy1")],
        [InlineKeyboardButton(text="Strategy 2", callback_data="strategy2")],
        [InlineKeyboardButton(text="⬅️ 返回", callback_data="main_menu")]
    ])


def go_back_strategy_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="strategy_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard
