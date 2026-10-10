import os
import requests

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

messaggio = """
🏠 Ricerca Immobiliare Bot

✅ GitHub funziona
✅ Telegram funziona
✅ Il bot è operativo

Prossimo step:
monitoraggio Immobiliare.it
"""

url = f"https://api.telegram.org/bot{token}/sendMessage"

requests.post(
    url,
    json={
        "chat_id": chat_id,
        "text": messaggio
    }
)

print("Messaggio inviato")
