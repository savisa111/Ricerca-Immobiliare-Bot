from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import os
import requests

comune = "Occhiobello"
prezzo = 73000
mq = 450

VICENZA = (45.5455, 11.5354)

geolocator = Nominatim(user_agent="ricerca_immobiliare")

location = geolocator.geocode(f"{comune}, Italia")

if location:

    distanza = geodesic(
        VICENZA,
        (location.latitude, location.longitude)
    ).km

    prezzo_mq = prezzo / mq

    score = 0

    if prezzo < 100000:
        score += 3

    if mq > 250:
        score += 3

    if distanza <= 100:
        score += 2

    if prezzo_mq < 300:
        score += 2

    if score >= 8:
        priorita = "🟢 ALTA"
    elif score >= 5:
        priorita = "🟠 MEDIA"
    else:
        priorita = "🔴 BASSA"

    messaggio = f"""
🔥 NUOVA OPPORTUNITÀ

📍 {comune}
📏 {distanza:.0f} km da Vicenza

💰 Prezzo: {prezzo:,.0f} €
📐 Superficie: {mq} mq

💵 €/mq: {prezzo_mq:.0f} €

⭐ Score: {score}/10

{priorita}
"""

    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": messaggio
        }
    )

print("Messaggio inviato")
