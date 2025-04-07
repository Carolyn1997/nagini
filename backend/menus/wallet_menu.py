from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_wallet_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="默认钱包 (Default Wallet)",
                              callback_data="show_default_wallet")],
        [InlineKeyboardButton(text="设置默认钱包", callback_data="set_default_wallet"), InlineKeyboardButton(
            text="重置默认钱包", callback_data="reset_default_wallet")],
        [InlineKeyboardButton(text="狙击钱包 (Sniper Wallet)",
                              callback_data="show_sniper_wallet")],
        [InlineKeyboardButton(text="设置狙击钱包", callback_data="set_sniper_wallet"), InlineKeyboardButton(
            text="重置狙击钱包", callback_data="reset_sniper_wallet")],
        [InlineKeyboardButton(text="余额 (Balance)", callback_data="balance"), InlineKeyboardButton(
            text="存款 (Deposit)", callback_data="deposit")],
        [InlineKeyboardButton(text="提款 (Withdraw)", callback_data="withdraw"),
         InlineKeyboardButton(text="⬅️ 返回", callback_data="main_menu")]
    ])


def go_back_wallet_btn() -> None:
    go_back_btn = InlineKeyboardButton(
        text="Go Back", callback_data="wallet_menu")
    go_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_back_btn]])
    return go_back_keyboard
