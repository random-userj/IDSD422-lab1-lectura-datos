# leer_csv.py — Cargar el reporte CSV del ERP (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_csv.py

import pandas as pd

ventas = pd.read_csv("data/ventas.csv")
print(ventas.head())
# imprimir las dimensiones
print("Dimensiones:" , ventas.shape)
print("\n Tipos por columna")
print(ventas.dtypes)