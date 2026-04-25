import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

from stations import BASE_URL

# Sesiune globală pentru performanță (connection pooling)
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
})

# ======================================================================
#  Mapare tipuri carburant din tabelul peko.ro → cheile din aplicație
# ======================================================================
FUEL_MAP = {
    "benzina standard": "benzina",
    "benzina premium": "benzina_premium",
    "motorina standard": "motorina",
    "motorina premium": "motorina_premium",
    "gpl": "gpl",
}


def parse_pret(text):
    """Extrage valoarea numerică dintr-un șir de forma '9.23 Lei'."""
    if not text or text.strip() in ("", "-"):
        return None
    try:
        clean = text.lower().replace("lei", "").replace(",", ".").strip()
        num = re.sub(r'[^\d.]', '', clean)
        return float(num) if num else None
    except Exception:
        return None


def scrape_station(station_id):
    """
    Accesează pagina stației pe peko.ro și extrage prețurile din tabel.
    """
    url = station_id if station_id.startswith("http") else BASE_URL + station_id

    try:
        response = session.get(url, timeout=8)
        if response.status_code != 200:
            return {}

        soup = BeautifulSoup(response.text, 'html.parser')

        # Ora curentă pe post de "plasă de siguranță"
        prices = {"data": datetime.now().strftime("%H:%M")}

        # Țintim exact tabelul cu prețuri
        table = soup.find('table', class_='table-zebra')
        if not table:
            return prices

        for row in table.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) < 3:
                continue

            # Extragem și curățăm tipul de carburant
            tip = cols[0].get_text(separator=" ", strip=True).lower()
            pret = cols[2].get_text(separator=" ", strip=True)

            # Normalizare completă (scoatem diacriticele și reducem spațiile)
            tip = (tip.replace("ă", "a").replace("â", "a")
                   .replace("î", "i").replace("ș", "s").replace("ț", "t"))
            tip = re.sub(r'\s+', ' ', tip).strip()

            cheie = FUEL_MAP.get(tip)
            if cheie and cheie not in prices:
                valoare = parse_pret(pret)
                if valoare:
                    prices[cheie] = str(valoare)

                    # Luăm data reală de actualizare (ex: "14 ore în urmă")
                    if len(cols) >= 4:
                        data_peko = cols[3].get_text(strip=True)
                        if data_peko:
                            prices["data"] = data_peko

        return prices

    except Exception as e:
        print(f"⚠️ Eroare la scraper pentru id-ul {station_id}: {e}")
        return {}