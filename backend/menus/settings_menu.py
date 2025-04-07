from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_settings_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="账户设置", callback_data="account_settings")],
        [InlineKeyboardButton(text="安全设置", callback_data="security_settings")],
        [InlineKeyboardButton(
            text="通知设置", callback_data="notification_settings")],
        [InlineKeyboardButton(text="⬅️ 返回", callback_data="main_menu")]
    ])


def go_back_settings_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="settings_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard
