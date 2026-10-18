# inspeccion.R — Inspección y cálculo de indicadores (R)
# Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# install.packages("readr")
library(readr)

ventas <- read_csv("data/ventas.csv")
ventas$ticket <- ventas$ventas / ventas$clientes
head(ventas)

# Venta promedio y ticket promedio
cat("Venta promedio por sucursal:", mean(ventas$ventas), "\n")
cat("Ticket promedio:", mean(ventas$ticket), "\n")

# Sucursal con mayor y menor ventas
cat("Sucursal con mayor ventas:", ventas$sucursal[which.max(ventas$ventas)], "\n")
cat("Sucursal con menor ventas:", ventas$sucursal[which.min(ventas$ventas)], "\n")

# Región con mayor venta total
ventas_region <- aggregate(ventas ~ region, data = ventas, sum)
print(ventas_region)
cat("Region con mayor venta total:", ventas_region$region[which.max(ventas_region$ventas)], "\n")