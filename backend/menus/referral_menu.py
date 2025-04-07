from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_referral_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="推荐链接", callback_data="referral_link")],
        [InlineKeyboardButton(text="推荐奖励", callback_data="referral_rewards")],
        [InlineKeyboardButton(text="历史记录", callback_data="referral_history")],
        [InlineKeyboardButton(text="⬅️ 返回", callback_data="main_menu")]
    ])


def go_back_referral_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="referral_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard
