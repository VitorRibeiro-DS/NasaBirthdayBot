import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")
updates = requests.get(f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/getUpdates")
updates = updates.json()
updates["result"][-1]
print(updates)
requests.post(
        url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage",
        data={"chat_id": updates["result"][-1]["message"]["chat"]["id"], "text": "Olá tudo bem?"}
    ).json()