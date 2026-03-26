import requests

# 1. 貼上您剛剛在 Discord 複製的 Webhook 網址
webhook_url = "https://discord.com/api/webhooks/1486788062800379985/Iy2yasXbywINbY0CMQAwR0YiEK54YaZ8dWhZlVHUG25Q56y_GyrOkkfXjyDN3d3Ux9O4"

# 2. 設定要發送的訊息內容 (Discord 規定訊息內容的標籤必須是 'content')
message_data = {
    "content": "測試"
}

# 3. 發送 POST 請求給 Discord
response = requests.post(webhook_url, json=message_data)

# 4. 檢查是否發送成功 ( 成功接收會回傳 204 狀態碼)
if response.status_code == 204:
    print("訊息發送成功")
else:
    print(f"發送失敗，狀態碼：{response.status_code}")