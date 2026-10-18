# leer_csv.R — Cargar el reporte CSV del ERP (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/leer_csv.R

install.packages("readr")
library(readr)
ventas <- read_csv("data/ventas.csv")
head(ventas)
dim(ventas)
str(ventas)


