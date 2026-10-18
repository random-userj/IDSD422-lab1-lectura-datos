# leer_json.R - Cargar el reporte JSON de la API (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raiz del repositorio:
#   Rscript scripts/leer_json.R

install.packages("jsonlite")
library(jsonlite)
ventas <- fromJSON("data/ventas.json")
head(ventas)
dim(ventas)
str(ventas)

