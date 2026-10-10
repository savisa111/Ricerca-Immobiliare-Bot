import os
import requests

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

msg = "🏠 Ricerca Immobiliare Bot operativo!\n\nPrimo test completato con successo."

url = f"https://api.telegram.org/bot{token}/sendMessage"

requests.post(
    url,
    json={
        "chat_id": chat_id,
        "text": msg
    }
)

print("Messaggio inviato")
