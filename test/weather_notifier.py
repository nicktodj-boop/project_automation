import requests

#  設定 Discord Webhook 網址
webhook_url = "https://discord.com/api/webhooks/1486788062800379985/Iy2yasXbywINbY0CMQAwR0YiEK54YaZ8dWhZlVHUG25Q56y_GyrOkkfXjyDN3d3Ux9O4"  # <-- 請務必換成您的網址

#  使用 Open-Meteo (設定為台北的經緯度)
weather_url = "https://api.open-meteo.com/v1/forecast?latitude=25.0478&longitude=121.5319&current_weather=true"

# 發送請求
weather_response = requests.get(weather_url)

if weather_response.status_code == 200:
    data = weather_response.json()

    #  萃取資料
    current_temp = data['current_weather']['temperature']
    weather_code = data['current_weather']['weathercode']

    #  Open-Meteo 回傳的是數字代碼，做個簡單的轉換
    if weather_code <= 3:
        weather_desc = "晴朗多雲"
    elif weather_code <= 69:
        weather_desc = "有雨，記得帶傘 "
    else:
        weather_desc = "天氣不佳"

    # 5. 編輯與發送 Discord 訊息
    report = f" 【自動化天氣播報】\n 城市：台北\n 狀況：{weather_desc}\n 溫度：{current_temp} °C"

    message_data = {
        "content": report
    }
    discord_response = requests.post(webhook_url, json=message_data)

    # 6. 檢查推播狀態
    if discord_response.status_code == 204:
        print("請去 Discord查看天氣報告。")
    else:
        print(f" Discord 推播失敗，狀態碼：{discord_response.status_code}")

else:
    print(" 無法獲取天氣資料，狀態碼：", weather_response.status_code)