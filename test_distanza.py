from geopy.geocoders import Nominatim
from geopy.distance import geodesic

VICENZA = (45.5455, 11.5354)

geolocator = Nominatim(user_agent="ricerca_immobiliare")

location = geolocator.geocode("Occhiobello, Italia")

if location:
    distanza = geodesic(
        VICENZA,
        (location.latitude, location.longitude)
    ).km

    print(f"Distanza: {distanza:.1f} km")
else:
    print("Comune non trovato")
