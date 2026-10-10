from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import os
import requests

VICENZA = (45.5455, 11.5354)

geolocator = Nominatim(user_agent="ricerca_immobiliare")

location = geolocator.geocode("Occhiobello, Italia")

if location:

    distanza = geodesic(
        VICENZA,
        (location.latitude, location.longitude)
    ).km

    messaggio = f"""
🏠 TEST IMMOBILE

📍 Occhiobello

📏 Distanza da Vicenza:
{distanza:.1f} km

💰 Prezzo: 73.000 €

📐 Superficie: 450 mq

💵 €/mq: 162
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

print("ok")
