"""
HOTFUEL - Backend FastAPI
Rulează cu: uvicorn api:app --host 0.0.0.0 --port 8000 --reload
Accesează de pe iPhone: http://IP_PC_TÂU:8000
"""

import os
import time
import threading
import concurrent.futures
from typing import Optional

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Importăm modulele existente (neschimbate!)
from scraper import scrape_station, parse_pret
from stations import STATIONS
from database import get_user, save_user, init_db
from cars import car_db

# ======================================================================
# Inițializare
# ======================================================================

app = FastAPI(title="HOTFUEL API", version="2.0")

# CORS - necesar pentru PWA
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Asigurăm că baza de date există
init_db()

# ======================================================================
# Cache Global Prețuri
# ======================================================================

prices_cache: dict = {}       # { station_id: { benzina: "7.85", ... } }
medii_oras: dict = {}         # { benzina: 7.82, motorina: 7.10, ... }
is_scraping: bool = False
last_scrape_time: float = 0
scrape_progress: dict = {"done": 0, "total": len(STATIONS)}


def compute_averages() -> None:
    """Calculează media prețurilor pentru fiecare tip de carburant."""
    global medii_oras
    for tip in ["benzina", "benzina_premium", "motorina", "motorina_premium", "gpl"]:
        valori = [
            parse_pret(prices_cache.get(s["id"], {}).get(tip))
            for s in STATIONS
        ]
        valori = [v for v in valori if v is not None]
        if valori:
            medii_oras[tip] = round(sum(valori) / len(valori), 3)


def scrape_all() -> None:
    """Scraping paralel pentru toate stațiile."""
    global is_scraping, last_scrape_time, scrape_progress

    is_scraping = True
    scrape_progress = {"done": 0, "total": len(STATIONS)}

    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        futures = {executor.submit(scrape_station, s["id"]): s for s in STATIONS}
        for future in concurrent.futures.as_completed(futures):
            station = futures[future]
            try:
                prices = future.result()
                prices_cache[station["id"]] = prices
            except Exception as e:
                print(f"[Scraper] Eroare {station['id']}: {e}")
            finally:
                scrape_progress["done"] += 1

    compute_averages()
    last_scrape_time = time.time()
    is_scraping = False
    print(f"[HOTFUEL] Scraping finalizat — {len(prices_cache)} stații actualizate")


def background_loop() -> None:
    """Scraping automat la fiecare 2 ore."""
    while True:
        print("[HOTFUEL] Pornesc scraping automat...")
        scrape_all()
        time.sleep(7200)  # 2 ore


# Pornim scraping-ul la start
threading.Thread(target=background_loop, daemon=True).start()


# ======================================================================
# API Endpoints
# ======================================================================

@app.get("/api/stations")
def get_stations():
    """Returnează toate stațiile cu prețurile curente."""
    stations_with_prices = []
    for s in STATIONS:
        prices = prices_cache.get(s["id"], {})
        stations_with_prices.append({**s, "prices": prices})

    return {
        "stations": stations_with_prices,
        "is_loading": is_scraping,
        "progress": scrape_progress,
        "last_update": last_scrape_time,
    }


@app.post("/api/refresh")
def refresh_prices():
    """Forțează un nou scraping."""
    global is_scraping
    if not is_scraping:
        threading.Thread(target=scrape_all, daemon=True).start()
        return {"status": "started"}
    return {"status": "already_running"}


@app.get("/api/averages")
def get_averages():
    """Returnează mediile prețurilor pe oraș."""
    return medii_oras


@app.get("/api/cars")
def get_cars():
    """Returnează baza de date cu mașini."""
    return car_db


@app.get("/api/user/{email}")
def api_get_user(email: str):
    """Returnează datele unui utilizator după email."""
    user = get_user(email)
    if not user:
        raise HTTPException(status_code=404, detail="Utilizator negăsit")
    return user


@app.post("/api/user")
async def api_save_user(request: Request):
    """Salvează sau actualizează datele unui utilizator."""
    data = await request.json()
    required = ["email", "nume", "masina", "carburant", "capacitate"]
    for field in required:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"Câmp lipsă: {field}")

    save_user(
        data["email"],
        data["nume"],
        data["masina"],
        data["carburant"],
        float(data["capacitate"])
    )
    return {"status": "ok"}


@app.get("/api/status")
def get_status():
    """Status general al serverului."""
    return {
        "status": "online",
        "stations_count": len(STATIONS),
        "prices_loaded": len(prices_cache),
        "is_scraping": is_scraping,
        "last_scrape": last_scrape_time,
    }


# ======================================================================
# Servire Fișiere Statice (PWA)
# ======================================================================

# Fișiere speciale PWA
@app.get("/manifest.json")
def serve_manifest():
    return FileResponse("static/manifest.json", media_type="application/manifest+json")


@app.get("/sw.js")
def serve_sw():
    return FileResponse("static/sw.js", media_type="application/javascript")


# Interfața principală
@app.get("/", response_class=HTMLResponse)
def serve_index():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()


# Catch-all pentru PWA routing
@app.get("/{path:path}", response_class=HTMLResponse)
def serve_spa(path: str):
    # Dacă e fișier static, îl servim
    static_path = f"static/{path}"
    if os.path.exists(static_path) and os.path.isfile(static_path):
        return FileResponse(static_path)
    # Altfel, servim index.html (pentru PWA routing)
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()


# ======================================================================
# Entry Point
# ======================================================================

if __name__ == "__main__":
    import uvicorn
    import socket

    # Afișăm IP-ul local pentru accesul de pe iPhone
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print("\n" + "=" * 55)
    print("  🔥 HOTFUEL Server pornit!")
    print("=" * 55)
    print(f"  PC:     http://localhost:8000")
    print(f"  iPhone: http://{local_ip}:8000")
    print("  (Asigură-te că iPhone-ul e pe același WiFi!)")
    print("=" * 55 + "\n")

    uvicorn.run(app, host="0.0.0.0", port=8000)