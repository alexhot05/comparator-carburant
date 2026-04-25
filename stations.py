# ======================================================================
#  STATIONS.PY — Lista completă a benzinăriilor din Craiova
#  Sursa datelor: peko.ro  |  Ultima actualizare: aprilie 2026
#
#  Fiecare stație conține:
#    id     — slug-ul din URL-ul peko.ro (folosit de scraper)
#    retea  — rețeaua (PETROM, OMV, MOL, LUKOIL, ROMPETROL)
#    name   — numele afișat în aplicație
#    addr   — adresa stradală
#    lat    — latitudine (din Google Maps / Waze, via peko.ro)
#    lng    — longitudine
#    fuels  — carburanții disponibili: benzina, motorina, gpl
# ======================================================================

BASE_URL = "https://peko.ro/benzinarii/dj/craiova/"

STATIONS = [

    # ------------------------------------------------------------------
    #  MOL  (5 stații)
    # ------------------------------------------------------------------
    {
        "id":    "mol-craiova-1-brestei",
        "retea": "MOL",
        "name":  "MOL Craiova 1 - Brestei",
        "addr":  "Str. Brestei",
        "lat":   44.32335,  "lng": 23.77684,
        "fuels": ["benzina", "motorina", "gpl"],
    },
    {
        "id":    "mol-craiova-2-decebal",
        "retea": "MOL",
        "name":  "MOL Craiova 2 - Decebal",
        "addr":  "Bd. Decebal",
        "lat":   44.32248,  "lng": 23.83012,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "mol-craiova-3-calea-severinului-titulescu",
        "retea": "MOL",
        "name":  "MOL Craiova 3 - Severinului (Titulescu)",
        "addr":  "Calea Severinului",
        "lat":   44.33920,  "lng": 23.76351,
        "fuels": ["benzina", "motorina", "gpl"],
    },
    {
        "id":    "mol-craiova-5-decebal",
        "retea": "MOL",
        "name":  "MOL Craiova 5 - Decebal",
        "addr":  "Str. Decebal",
        "lat":   44.32260,  "lng": 23.83009,
        "fuels": ["benzina", "motorina", "gpl"],
    },
    {
        "id":    "mol-craiova-romanescu",
        "retea": "MOL",
        "name":  "MOL Craiova - Romanescu",
        "addr":  "Calea Unirii",
        "lat":   44.30121,  "lng": 23.79855,
        "fuels": ["benzina", "motorina"],
    },

    # ------------------------------------------------------------------
    #  OMV  (4 stații)
    # ------------------------------------------------------------------
    {
        "id":    "omv-1-craiova-omv",
        "retea": "OMV",
        "name":  "OMV 1 Craiova",
        "addr":  "Calea Severinului",
        "lat":   44.33775,  "lng": 23.76577,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "omv-2-craiova-omv",
        "retea": "OMV",
        "name":  "OMV 2 Craiova",
        "addr":  "Calea Bucuresti",
        "lat":   44.31270,  "lng": 23.85847,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "omv-51-craiova",
        "retea": "OMV",
        "name":  "OMV 51 Craiova",
        "addr":  "Calea Severinului",
        "lat":   44.32835,  "lng": 23.77630,
        "fuels": ["benzina", "motorina", "gpl"],
    },
    {
        "id":    "omv-52-craiova",
        "retea": "OMV",
        "name":  "OMV 52 Craiova",
        "addr":  "Calea Bucuresti",
        "lat":   44.31399,  "lng": 23.83081,
        "fuels": ["benzina", "motorina", "gpl"],
    },

    # ------------------------------------------------------------------
    #  ROMPETROL  (4 stații)
    # ------------------------------------------------------------------
    {
        "id":    "rompetrol-craiova-1-decebal",
        "retea": "ROMPETROL",
        "name":  "Rompetrol Craiova 1 (Decebal)",
        "addr":  "Bd. Decebal nr. 85",
        "lat":   44.317699, "lng": 23.833839,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "rompetrol-craiova-2-caracal",
        "retea": "ROMPETROL",
        "name":  "Rompetrol Craiova 2 (Caracal)",
        "addr":  "Str. Caracal nr. 146",
        "lat":   44.304165, "lng": 23.813103,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "rompetrol-craiova-3-imparatul-traian",
        "retea": "ROMPETROL",
        "name":  "Rompetrol Craiova 3 (Imp. Traian)",
        "addr":  "Str. Imparatul Traian nr. 211",
        "lat":   44.310154, "lng": 23.819698,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "rompetrol-craiova-5-simnic",
        "retea": "ROMPETROL",
        "name":  "Rompetrol Craiova 5 - Simnic",
        "addr":  "Aleea 4 Simnic nr. 6",
        "lat":   44.314696, "lng": 23.761863,
        "fuels": ["benzina", "motorina", "gpl"],
    },

    # ------------------------------------------------------------------
    #  PETROM  (10 stații)
    # ------------------------------------------------------------------
    {
        "id":    "petrom-4-craiova",
        "retea": "PETROM",
        "name":  "Petrom 4 Craiova",
        "addr":  "Str. Stefan Cel Mare nr. 2A",
        "lat":   44.32195,  "lng": 23.79654,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "petrom-5-craiova",
        "retea": "PETROM",
        "name":  "Petrom 5 Craiova",
        "addr":  "Str. Caracal nr. 115B",
        "lat":   44.30721,  "lng": 23.80553,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "petrom-7-craiova",
        "retea": "PETROM",
        "name":  "Petrom 7 Craiova",
        "addr":  "Str. Ana Ipatescu",
        "lat":   44.30700,  "lng": 23.80546,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "petrom-23-craiova",
        "retea": "PETROM",
        "name":  "Petrom 23 Craiova",
        "addr":  "Str. Brestei",
        "lat":   44.32921,  "lng": 23.76076,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "petrom-27-craiova",
        "retea": "PETROM",
        "name":  "Petrom 27 Craiova",
        "addr":  "Calea Severinului nr. 31",
        "lat":   44.34840,  "lng": 23.75640,
        "fuels": ["benzina", "motorina", "gpl"],
    },
    {
        "id":    "petrom-28-craiova",
        "retea": "PETROM",
        "name":  "Petrom 28 Craiova",
        "addr":  "B-dul Decebal nr. 10",
        "lat":   44.32657,  "lng": 23.81955,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "petrom-29-craiova",
        "retea": "PETROM",
        "name":  "Petrom 29 Craiova",
        "addr":  "Str. Nicolae Romanescu nr. 112C",
        "lat":   44.29120,  "lng": 23.79893,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "petrom-30-craiova",
        "retea": "PETROM",
        "name":  "Petrom 30 Craiova",
        "addr":  "Str. Caracal nr. 162A",
        "lat":   44.29950,  "lng": 23.82793,
        "fuels": ["benzina", "motorina", "gpl"],
    },
    {
        "id":    "petrom-mpp-craiova-caracal",
        "retea": "PETROM",
        "name":  "Petrom MPP Caracal",
        "addr":  "Str. Caracal",
        "lat":   44.29899,  "lng": 23.83149,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "petrom-sala-polivalenta-craiova",
        "retea": "PETROM",
        "name":  "Petrom Sala Polivalenta",
        "addr":  "B-dul Stirbei-Voda nr. 30A",
        "lat":   44.31311,  "lng": 23.78833,
        "fuels": ["benzina", "motorina"],
    },

    # ------------------------------------------------------------------
    #  LUKOIL  (5 stații)
    # ------------------------------------------------------------------
    {
        "id":    "lukoil-craiova-1",
        "retea": "LUKOIL",
        "name":  "Lukoil Craiova 1 - Dacia",
        "addr":  "B-dul Dacia",
        "lat":   44.335998, "lng": 23.793962,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "lukoil-craiova-2",
        "retea": "LUKOIL",
        "name":  "Lukoil Craiova 2 - Severinului",
        "addr":  "Calea Severinului",
        "lat":   44.32931,  "lng": 23.77610,
        "fuels": ["benzina", "motorina"],
    },
    {
        "id":    "lukoil-craiova-3",
        "retea": "LUKOIL",
        "name":  "Lukoil Craiova 3 - George Enescu",
        "addr":  "Str. George Enescu",
        "lat":   44.33167,  "lng": 23.78225,
        "fuels": ["benzina", "motorina", "gpl"],
    },
    {
        "id":    "lukoil-craiova-4",
        "retea": "LUKOIL",
        "name":  "Lukoil Craiova 4 - Râului",
        "addr":  "Str. Râului",
        "lat":   44.324228, "lng": 23.771088,
        "fuels": ["benzina", "motorina", "gpl"],
    },
    {
        "id":    "lukoil-craiova-5",
        "retea": "LUKOIL",
        "name":  "Lukoil Craiova 5 - Bariera Vâlcii",
        "addr":  "Str. Bariera Vâlcii",
        "lat":   44.347738, "lng": 23.819973,
        "fuels": ["benzina", "motorina"],
    },

]