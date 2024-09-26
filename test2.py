# 先導入後面會用到的套件
import requests  # 請求工具
from bs4 import BeautifulSoup  # 解析工具
import time  # 用來暫停程式

# 要爬的股票
stock = ["1101", "2330", "1102"]

# 迴圈依序爬股價
for i in range(len(stock)):

    # 現在處理的股票
    stockid = stock[i]

    # 網址塞入股票編號
    url = "https://tw.stock.yahoo.com/quote/" + stockid + ".TW"

    # 發送請求
    r = requests.get(url)

    # 解析回應的 HTML
    soup = BeautifulSoup(r.text, 'html.parser')

    # 定位股價，考慮三種不同的 HTML class 狀況
    price = soup.find('span', class_=[
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
    ]).getText()

    # 回報的訊息 (可自訂)
    message = f"股票 {stockid} 即時股價為 {price}"

    # 用 telegram bot 回報股價
    # bot token
    token = "7695488308:AAECzmn15adc1aulmuB34KW0lqPdHbNtua0"

    # 使用者 id
    chat_id = "8075224586"

    # bot 送訊息
    telegram_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(telegram_url)

    # 每次都停 3 秒
    time.sleep(3)