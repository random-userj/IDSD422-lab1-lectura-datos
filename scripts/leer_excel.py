# leer_csv.py — Cargar el reporte CSV del ERP (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_csv.py

import pandas as pd

# Cargar la hoja ventas, y especificar el nombre de la hoja
ventas = pd.read_excel("data/ventas.xlsx", sheet_name="ventas")

# Imprimir las primeras filas, dimensiones y tipos de datos
print(ventas.head())
print("Dimensiones:", ventas.shape)
print("\nTipos por columna:")
print(ventas.dtypes)