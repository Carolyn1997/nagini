import requests

# 目标 URL
url = "https://gmgn.ai/api/v1/mutil_window_token_link_rug_vote/sol/HTze13N7z2wZNReEo8zkcQsPjAYBpoUUwx4DJL7Xpump"

# 发送 GET 请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 打印返回的 JSON 数据
    print(response.json())
else:
    # 打印错误信息
    print(f"请求失败，状态码: {response.status_code}")
    print(f"返回内容: {response.text}")