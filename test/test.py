import requests

# 嘗試向 GitHub 的 API 發送一個請求
response = requests.get('https://api.github.com')
print(f"成功連線！狀態碼：{response.status_code}")