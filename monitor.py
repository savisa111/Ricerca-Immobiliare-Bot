from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import os
import requests

# DATI TEST
comune = "Occhiobello"
prezzo = 73000
mq = 450

# VICENZA
VICENZA = (45.5455, 11.5354)

# GEOLOCALIZZAZIONE
geolocator = Nominatim(user_agent="ricerca_immobiliare")

location = geolocator.geocode(f"{comune}, Italia")

if location:

    distanza = geodesic(
        VICENZA,
        (location.latitude, location.longitude)
    ).km

    prezzo_mq = prezzo / mq

    # PRIORITA'
    if distanza <= 100:
        priorita = "🟢 Alta"

    elif distanza <= 180:
        priorita = "🟠 Media"

    else:
        priorita = "🔴 Bassa"

    messaggio = f"""
🔥 NUOVA OPPORTUNITÀ

📍 {comune}
📏 {distanza:.1f} km da Vicenza

💰 Prezzo: {prezzo:,.0f} €
📐 Superficie: {mq} mq

💵 €/mq: {prezzo_mq:.0f} €

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
