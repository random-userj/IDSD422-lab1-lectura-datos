# inspeccion.py — Inspección y cálculo de indicadores (Python)
# Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

import pandas as pd

ventas = pd.read_csv("data/ventas.csv")
ventas["ticket"] = ventas["ventas"] / ventas["clientes"]
print(ventas.head())

# Venta promedio y ticket promedio
print("Venta promedio por sucursal:", ventas["ventas"].mean())
print("Ticket promedio:", ventas["ticket"].mean())

# Sucursal con mayor y menor ventas
print("Sucursal con mayor ventas:", ventas.loc[ventas["ventas"].idxmax(), "sucursal"])
print("Sucursal con menor ventas:", ventas.loc[ventas["ventas"].idxmin(), "sucursal"])

# Región con mayor venta total
ventas_region = ventas.groupby("region")["ventas"].sum()
print("\nVentas por region:")
print(ventas_region)
print("Region con mayor venta total:", ventas_region.idxmax())