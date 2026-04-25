# cars.py

car_db = {
    "DACIA": {
        "Logan": [
            {"gen": "Logan 1", "motoare": "1.4 MPI, 1.6 MPI, 1.5 dCi", "rezervor": 50},
            {"gen": "Logan 2", "motoare": "0.9 TCe, 1.2 16V, 1.5 dCi", "rezervor": 50},
            {"gen": "Logan 3", "motoare": "1.0 SCe, 1.0 TCe (Eco-G)", "rezervor": 50}
        ],
        "Duster": [
            {"gen": "Toate", "motoare": "1.5 dCi, 1.6 16V, 1.3 TCe, 1.2 TCe", "rezervor": 50}
        ],
        "Sandero": [
            {"gen": "Toate", "motoare": "1.2 benzina, 0.9 TCe, 1.5 dCi", "rezervor": 50}
        ]
    },
    "BMW": {
        "Seria 3": [
            {"gen": "E46", "motoare": "316i, 318i, 320d, 323i, 325i (pana la 2.5)", "rezervor": 63},
            {"gen": "E90", "motoare": "318d, 320d, 325i, 330d, 335i", "rezervor": 60},
            {"gen": "F30", "motoare": "318d, 320d, 328i, 330d, 340i", "rezervor": 57}
        ],
        "Seria 1": [{"gen": "E81", "motoare": "116i, 118d, 120d, 123d", "rezervor": 53}],
        "X1": [
            {"gen": "E84", "motoare": "18d, 20d, 23d, 28i", "rezervor": 61},
            {"gen": "F48", "motoare": "18d, 20d, 25d, 18i, 20i", "rezervor": 51}
        ],
        "X3": [
            {"gen": "E83", "motoare": "2.0d, 3.0d, 2.5i", "rezervor": 67},
            {"gen": "F25", "motoare": "20d, 30d, 35d, 28i", "rezervor": 67},
            {"gen": "G01", "motoare": "20d, 30d, M40i", "rezervor": 68}
        ],
        "Seria 5": [
            {"gen": "E60", "motoare": "520d, 525d, 530d, 525i, 530i, 545i", "rezervor": 70},
            {"gen": "F10", "motoare": "520d, 525d, 530d, 535d, 528i, 550i", "rezervor": 70}
        ],
        "SUV": [
            {"gen": "X5 E53", "motoare": "3.0d, 3.0i, 4.4i", "rezervor": 93},
            {"gen": "X5 E70", "motoare": "3.0d, 3.5d, 4.8i", "rezervor": 85},
            {"gen": "X6 E71", "motoare": "30d, 35d, 40d, 50i", "rezervor": 85}
        ]
    },
    "AUDI": {
        "A4": [
            {"gen": "B5", "motoare": "1.6, 1.8T, 1.9 TDI", "rezervor": 62},
            {"gen": "B6/B7", "motoare": "1.9 TDI, 2.0 TDI, 2.5 TDI, 1.8T, 2.0 ALT", "rezervor": 70},
            {"gen": "B8", "motoare": "2.0 TDI, 2.7 TDI, 3.0 TDI, 1.8 TFSI", "rezervor": 65}
        ],
        "A6": [
            {"gen": "C6", "motoare": "2.0 TDI, 2.7 TDI, 3.0 TDI, 2.4 V6", "rezervor": 80},
            {"gen": "C7", "motoare": "2.0 TDI, 3.0 TDI (Biturbo), 2.0 TFSI", "rezervor": 73}
        ],
        "Q7": [
            {"gen": "4L (Gen 1)", "motoare": "3.0 TDI, 4.2 TDI, 6.0 V12 TDI", "rezervor": 100},
            {"gen": "Gen 2", "motoare": "3.0 TDI, 2.0 TFSI, SQ7", "rezervor": 85}
        ]
    },
    "VW": {
        "Passat": [
            {"gen": "B5/B5.5", "motoare": "1.9 TDI (AVF/AWX), 1.8T, 2.5 TDI", "rezervor": 62},
            {"gen": "B6", "motoare": "1.9 TDI, 2.0 TDI (BMP/BKP), 1.6 FSI", "rezervor": 70},
            {"gen": "B7", "motoare": "1.6 TDI, 2.0 TDI, 1.4 TSI", "rezervor": 70},
            {"gen": "CC", "motoare": "2.0 TDI, 1.8 TSI, 3.6 FSI", "rezervor": 70}
        ],
        "Golf": [
            {"gen": "Golf 4", "motoare": "1.4, 1.6, 1.9 TDI (ALH/ASZ/ARL)", "rezervor": 55},
            {"gen": "Golf 5", "motoare": "1.4, 1.6 FSI, 1.9 TDI, 2.0 TDI", "rezervor": 55},
            {"gen": "Golf 6", "motoare": "1.6 TDI, 2.0 TDI, 1.4 TSI", "rezervor": 55},
            {"gen": "Golf 7", "motoare": "1.6 TDI, 2.0 TDI, 1.2 TSI, 1.4 TSI", "rezervor": 50}
        ],
        "Touareg": [
            {"gen": "Touareg I", "motoare": "2.5 TDI, 3.0 TDI, 5.0 V10 TDI", "rezervor": 100},
            {"gen": "Touareg II", "motoare": "3.0 TDI, 4.2 TDI, 3.0 TSI", "rezervor": 85}
        ]
    },
    "RENAULT": {
        "Megane": [
            {"gen": "Megane 2", "motoare": "1.5 dCi, 1.6 16v, 1.9 dCi", "rezervor": 60},
            {"gen": "Megane 3", "motoare": "1.5 dCi, 1.6 dCi, 1.2 TCe, 1.4 TCe", "rezervor": 60}
        ],
        "Talisman": [
            {"gen": "Gen 1", "motoare": "1.5 dCi, 1.6 dCi, 2.0 dCi, 1.6 TCe", "rezervor": 51}
        ]
    }
}