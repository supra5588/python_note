# You need use oio
# Open terminal
# enter pip3 install requests


import requests  # 導入requests 可獲取網址內容 與網頁互動

text = requests.get("https://app.easycamp.com.tw")

print(text.content)
