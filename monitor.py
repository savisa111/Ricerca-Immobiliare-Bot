import requests

url = "https://www.immobiliare.it/search-list/?idContratto=1&idCategoria=20&prezzoMinimo=20000&prezzoMassimo=200000&noAste=1&__lang=it&pag=1"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("STATUS:", r.status_code)
print(r.text[:1000])
