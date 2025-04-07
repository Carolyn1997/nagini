from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    start_menu = State()                  # 一级：开始菜单状态    use

    wallet_menu = State()                 # 二级：钱包菜单状态
    show_wallets = State()                # 显示钱包信息状态
    set_wallet = State()                  # 设置钱包状态
    waiting_default_private_key = State()     # 等待输入私钥状态  use
    waiting_sniper_private_key = State()     # 等待输入私钥状态   use
    waiting_for_contrace_address = State()   # 等待合约地址状态   use

    trade_menu = State()                  # 二级：交易菜单状态

    strategy_menu = State()               # 二级：策略菜单状态

    bots_menu = State()                   # 二级：机器人菜单状态

    lp_farming_menu = State()             # 二级：流动性挖矿菜单状态

    referral_menu = State()               # 二级：推荐菜单状态

    setting_menu = State()                # 二级：设置菜单状态

    copy_trade_menu = State()             # 跟单交易菜单状态
    add_follow_wallet = State()
    waiting_for_follow_wallet = State()
    waiting_for_unfollow_wallet = State()
    transaction_menu = State()            # 交易记录菜单状态
    help_menu = State()                   # 帮助菜单状态
    swap_menu = State()                   # 代币交换菜单状态
    set_slippage = State()                # 设置滑点状态
    buy_token = State()                   # 购买代币状态
    start_transaction = State()           # 开始交易状态
    waiting_for_token_name = State()      # 代币信息查询
