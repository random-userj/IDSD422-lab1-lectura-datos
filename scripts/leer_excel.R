# leer_excel.R - Cargar el consolidado Excel de finanzas (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raiz del...
#   Rscript scripts/leer_excel.R
install.packages("readxl")
library(readxl)
ventas <- read_excel("data/ventas.xlsx", sheet="ventas")
head(ventas)
dim(ventas)
str(ventas)
