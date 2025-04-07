from .main_menu import make_main_menu_keyboard, go_back_main_btn
from .wallet_menu import make_wallet_menu, go_back_wallet_btn
from .trade_menu import make_trade_menu, go_back_trade_btn, make_copy_trade_menu, make_swap_menu
from .strategy_menu import make_strategy_menu, go_back_strategy_btn
from .bots_menu import make_bots_menu, go_back_bots_btn
from .lp_farming_menu import make_lp_farming_menu, go_back_lp_farming_btn
from .referral_menu import make_referral_menu, go_back_referral_btn
from .settings_menu import make_settings_menu, go_back_settings_btn

go_back_main = go_back_main_btn()
go_back_wallet = go_back_wallet_btn()
go_back_trade = go_back_trade_btn()
go_back_strategy = go_back_strategy_btn()
go_back_bots = go_back_bots_btn()
go_back_lp_farming = go_back_lp_farming_btn()
go_back_referral = go_back_referral_btn()
go_back_settings = go_back_settings_btn()

go_back_copy_trade = make_copy_trade_menu()
go_back_swap = make_swap_menu()

main_menu_keyboard = make_main_menu_keyboard()
wallet_menu_keyboard = make_wallet_menu()
trade_menu_keyboard = make_trade_menu()
strategy_menu_keyboard = make_strategy_menu()
bots_menu_keyboard = make_bots_menu()
lp_farming_menu_keyboard = make_lp_farming_menu()
referral_menu_keyboard = make_referral_menu()
settings_menu_keyboard = make_settings_menu()

copy_trade_menu_keyboard = make_copy_trade_menu()
swap_menu_keyboard = make_swap_menu()
