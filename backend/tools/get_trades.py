import requests
import datetime

# Solana RPC 端点（可换成自己的）
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"

def solana_timestamp_to_beijing(timestamp):
    """ 将 Solana 时间戳转换为北京时间 """
    if timestamp is None:
        return "未知"
    dt_utc = datetime.datetime.utcfromtimestamp(timestamp)
    dt_beijing = dt_utc + datetime.timedelta(hours=8)
    return dt_beijing.strftime("%Y-%m-%d %H:%M:%S")

def get_transactions(address, limit=5):
    """ 获取地址最近的交易哈希 """
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSignaturesForAddress",
        "params": [address, {"limit": limit}]
    }
    response = requests.post(SOLANA_RPC_URL, json=payload)
    return response.json().get("result", [])

def get_transaction_details(tx_signature):
    """ 获取单个交易的详细信息 """
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTransaction",
        "params": [tx_signature, {"encoding": "jsonParsed"}]
    }
    response = requests.post(SOLANA_RPC_URL, json=payload)
    return response.json().get("result", {})

def parse_token_transfers(tx_details):
    """ 解析交易中的代币兑换信息 """
    if not tx_details:
        return None, None, []

    slot = tx_details.get("slot", "未知")
    block_time = tx_details.get("blockTime", None)
    beijing_time = solana_timestamp_to_beijing(block_time)

    token_transfers = []
    meta = tx_details.get("meta", {})

    def get_balance(bal):
        """ 处理可能为空的 uiAmount，避免 float(None) 报错 """
        return float(bal["uiTokenAmount"]["uiAmount"]) if bal["uiTokenAmount"]["uiAmount"] is not None else 0.0

    # 解析代币转移情况
    pre_balances = {bal["owner"]: (bal["mint"], get_balance(bal)) 
                    for bal in meta.get("preTokenBalances", [])}
    post_balances = {bal["owner"]: (bal["mint"], get_balance(bal)) 
                     for bal in meta.get("postTokenBalances", [])}

    for owner, (mint, post_balance) in post_balances.items():
        pre_balance = pre_balances.get(owner, (mint, 0))[1]
        delta = post_balance - pre_balance
        if delta != 0:
            token_transfers.append((owner, mint, delta))

    return slot, beijing_time, token_transfers

def main():
    address = "HCaee2MbWpEsxCGsCf8A5LXSURaRBBmMANavdpjM2Gq2"  # 替换为目标地址
    transactions = get_transactions(address, limit=5)

    for tx in transactions:
        tx_signature = tx["signature"]
        tx_details = get_transaction_details(tx_signature)
        slot, beijing_time, transfers = parse_token_transfers(tx_details)

        print(f"\n📌 交易哈希: {tx_signature}")
        print(f"⏳ 区块高度: {slot}")
        print(f"🕒 交易时间 (北京时间): {beijing_time}")
        print("🔄 代币兑换详情:")
        
        for owner, mint, amount in transfers:
            print(f"  - 钱包 {owner} 变动了 {amount} 枚代币 ({mint})")

if __name__ == "__main__":
    main()
