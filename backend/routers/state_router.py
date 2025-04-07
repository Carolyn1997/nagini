from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from config import AI_API_KEY, RPC_URL
from wallet import Wallet
from swap import Swap
from tokenInfo import TokenInfo
from tradingAnalyzer import TradingAnalyzer
from states import Form
from menus import *
from database.db import *

state_router = Router()


# 处理设置滑点的消息
@state_router.message(Form.set_slippage)
async def set_slippage(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    userData = data.get("userData")
    slippage = message.text
    if slippage.isdigit():
        slippage = float(message.text)
        if int(slippage) > 100 & int(slippage) < 0:
            await message.answer("Slippage must be less than 100 and greater than 0", reply_markup=go_back_trade)
            await state.set_state(Form.set_slippage)
        else:
            await message.answer(f"Slippage had changed from {userData['slippage']} to {slippage}", reply_markup=swap_menu_keyboard)
            await update_user(user_id=userId, slippage=slippage)
            userData = await get_user(user_id=userId)
            print(userData)
            await state.update_data(userData=userData)
        await state.set_state(Form.swap_menu)
    else:
        await message.answer("Please enter a valid number", reply_markup=go_back_trade)
        await state.set_state(Form.set_slippage)


# 处理 default 私钥输入的消息
@state_router.message(Form.waiting_default_private_key)
async def process_default_private_key(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    await state.update_data(default_private_key=message.text)
    default_private_key = message.text
    # Save the private key to the database

    try:
        wallet = Wallet(RPC_URL, default_private_key)
        default_wallet_address = wallet.wallet.pubkey().__str__()

        if default_wallet_address:
            await update_user(user_id=userId,  default_wallet_address=default_wallet_address, default_private_key=default_private_key)
            userData = await get_user(user_id=userId)
            await state.update_data(userData=userData)
            accBalance = await wallet.get_token_balance(default_wallet_address)
            await message.answer(f"You default Wallet: { default_wallet_address} has been set Successfully\n Current Balance: {accBalance['balance']['float']} SOL", reply_markup=wallet_menu_keyboard)
        else:
            raise ValueError("Invalid private key")
    except Exception as e:
        await message.answer("Invalid Private Key. Please enter a correct one.")
        await state.set_state(Form.waiting_default_private_key)
        return
    await state.set_state(Form.wallet_menu)

# 处理 default 私钥输入的消息


@state_router.message(Form.waiting_sniper_private_key)
async def process_sniper_private_key(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    await state.update_data(sniper_private_key=message.text)
    sniper_private_key = message.text
    # Save the private key to the database

    try:
        wallet = Wallet(RPC_URL, sniper_private_key)
        sniper_wallet_address = wallet.wallet.pubkey().__str__()

        if sniper_wallet_address:
            await update_user(user_id=userId,  sniper_wallet_address=sniper_wallet_address, sniper_private_key=sniper_private_key)
            userData = await get_user(user_id=userId)
            await state.update_data(userData=userData)
            accBalance = await wallet.get_token_balance(sniper_wallet_address)
            await message.answer(f"You sniper Wallet: { sniper_wallet_address} has been set Successfully\n Current Balance: {accBalance['balance']['float']} SOL", reply_markup=wallet_menu_keyboard)
        else:
            raise ValueError("Invalid private key for sniper wallet")
    except Exception as e:
        await message.answer("Invalid Private Key. Please enter a correct one.")
        await state.set_state(Form.waiting_sniper_private_key)
        return
    await state.set_state(Form.wallet_menu)


# 处理添加 monitor wallet
@state_router.message(Form.waiting_for_follow_wallet)
async def process_follow_monitor_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    userData = data.get("userData")
    monitor_wallets = ""
    print(message.text)
    print(userData["monitor_wallet"])
    if userData["monitor_wallet"] == "":
        monitor_wallets = message.text + ";"
    else:
        monitor_wallets = userData['monitor_wallet'] + message.text + ";"
    print(monitor_wallets)
    await update_user(user_id=userId, monitor_wallet=monitor_wallets)
    userData['monitor_wallet'] = monitor_wallets
    await state.update_data(userData=userData)
    await message.answer(f"You have added wallet {message.text} succesfully!", reply_markup=copy_trade_menu_keyboard)
    await state.set_state(Form.copy_trade_menu)


# 处理删除 monitor wallet
@state_router.message(Form.waiting_for_unfollow_wallet)
async def process_unfollow_monitor_wallet(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    userId = data.get("userId")
    userData = data.get("userData")
    monitor_wallets = userData["monitor_wallet"].replace(
        message.text + ";", "")
    await update_user(user_id=userId, monitor_wallet=monitor_wallets)
    userData['monitor_wallet'] = monitor_wallets
    await state.update_data(userData=userData)
    await message.answer(f"You have removed wallet {message.text} succesfully!", reply_markup=copy_trade_menu_keyboard)
    await state.set_state(Form.copy_trade_menu)


# 处理代币交换信息
@state_router.message(Form.waiting_for_contrace_address)
async def contrace_swap_handler(message: Message, state: FSMContext) -> None:
    print("swap_handler")
    data = await state.get_data()
    userData = data.get("userData")
    token_address = message.text
    swapClient = Swap(RPC_URL, userData.get("default_private_key"))
    token_mint_addresss = await swapClient.get_token_mint_account(token_address)
    account_token_info = await swapClient.get_wallet_token_balance(token_address)
    print("token_mint_address: ", token_mint_addresss)
    print("account_token_: ", token_mint_addresss)
    # 此处获取 token info 存在 cloudscraper 阻碍
    token_info = await TokenInfo.get_token_info(token_address)
    await state.update_data(token_info=token_info)
    await state.update_data(token_address=token_address)
    await state.update_data(account_token_info=account_token_info)
    open_timestamp = token_info.get('open_timestamp', 0)
    if open_timestamp:
        open_date = datetime.fromtimestamp(open_timestamp).strftime('%Y-%m-%d')
    else:
        open_date = "Unknown"
    swapText = f"""You Currently have {account_token_info['balance']['float']} {token_info['symbol']} in your wallet.\n
        💵Token Info:
        |---Symbol: {token_info['symbol']}
        |---Name: {token_info['name']}
        |---Price: {TokenInfo.convert_price_to_string(token_info['price'])}
        ------------------------------------
        🔍Pool Info:
        |---24H Volume: {TokenInfo.convert_volume_to_string(token_info['volume_24h'])}
        |---Token FDV: {TokenInfo.convert_volume_to_string(int(token_info['fdv']))}
        |---Token Liquidity: {TokenInfo.convert_volume_to_string(int(token_info['liquidity']))}
        |---Holder Count: {token_info['holder_count']}
        ------------------------------------
        |---Token MAX Supply: {TokenInfo.convert_volume_to_string(token_info['max_supply'])}
        |---Token Open Date: {open_date}
        ------------------------------------
        🔗Links:
        |--- [GMGN](https://gmgn.ai/sol/token/{token_address}) | [DexScreener](https://dexscreener.com/solana/{token_address}) | [Birdeye](https://dexscreener.com/solana/{token_address}) | [Dextools](https://www.dextools.io/app/cn/ether/pair-explorer/{token_address})
        """
    # swapText = "等待替换为 gmgn 的合约详情数据，目前获取合约的请求被 cloudscraper 阻碍"
    # Use the correct context to reply

    await message.answer(f"{swapText}", reply_markup=swap_menu_keyboard, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
    await state.set_state(Form.buy_token)


# 处理代币信息查询，绘制策略箱体图
@state_router.message(Form.waiting_for_token_name)
async def process_token_search(message: Message, state: FSMContext) -> None:
    token = message.text
    # 增加代币合法性检查
    analyzer = TradingAnalyzer(AI_API_KEY, token, '1H', 500)
    png_file, analysis_result = analyzer.analyze(show_chart=True)
    image = FSInputFile(png_file)
    await message.answer_photo(photo=image, caption=analysis_result, reply_markup=main_menu_keyboard)
    await state.set_state(Form.start_menu)
