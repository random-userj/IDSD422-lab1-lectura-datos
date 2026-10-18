# leer_json.py — Cargar el reporte JSON de la API (Python)
# Ejecuta desde la raíz del repositorio:
#   python scripts/leer_json.py

import json
import pandas as pd

# Cargar data/ventas.json con json.load (devuelve una lista de diccionarios)
with open("data/ventas.json", encoding="utf-8") as f:
    datos = json.load(f)

# Aplanar la estructura en un DataFrame tabular
ventas = pd.json_normalize(datos)

# Imprimir las primeras filas, dimensiones y tipos de datos
print(ventas.head())
print("Dimensiones:", ventas.shape)
print("\nTipos por columna:")
print(ventas.dtypes)