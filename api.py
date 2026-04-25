"""
HOTFUEL - Backend FastAPI
Rulează cu: uvicorn api:app --host 0.0.0.0 --port 8000 --reload
"""
import os
import time
import threading
import concurrent.futures

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from scraper import scrape_station, parse_pret
from stations import STATIONS
from cars import car_db

app = FastAPI(title="HOTFUEL API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

prices_cache: dict = {}      
medii_oras: dict = {}        
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
        time.sleep(7200) 



threading.Thread(target=background_loop, daemon=True).start()


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


@app.get("/manifest.json")
def serve_manifest():
    return FileResponse("static/manifest.json", media_type="application/manifest+json")


@app.get("/sw.js")
def serve_sw():
    return FileResponse("static/sw.js", media_type="application/javascript")


@app.get("/", response_class=HTMLResponse)
def serve_index():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()


@app.get("/{path:path}", response_class=HTMLResponse)
def serve_spa(path: str):
    static_path = f"static/{path}"
    if os.path.exists(static_path) and os.path.isfile(static_path):
        return FileResponse(static_path)
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()
