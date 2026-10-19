# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** 19/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Tras el análisis de los reportes semanales de ventas del ERP de sucursales, la API de fidelización y el consolidado de Finanzas. Se confirmó tanto en Python como en R que las 3 fuentes contienen los mismos registros. El  equipo de BI recomienda automatizar el flujo de carga semanal con cualquiera de las 3 fuentes e impulsar estrategias para impulsar el ticket promedio en la región Costa.
## 1. ¿Los tres formatos contienen la misma información?

*Carga los tres archivos (CSV, JSON y Excel) en Python y en R, y compara dimensiones y estructura. Completa la tabla:*

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales | 5 | 4 | Python: pd.read_csv("data/ventas.csv") / R: read_csv("data/ventas.csv") |
| JSON | API de fidelización | 5 | 4 | Python: json.load(f) + pd.json_normalize(datos) / R: fromJSON("data/ventas.json") |
| Excel | Consolidado de finanzas | 5 | 4 | Python: json.load(f) + pd.json_normalize(datos) / R: fromJSON("data/ventas.json") |

*Responde: ¿la estructura interna del archivo (texto plano, anidada, binaria) cambia el contenido?*
No, cambia el contenido. A pesar de que cada archivo contenga su formato en específico, si los datos son los mismo no cambia en nada el contenido importado corrrectamente a una estructura tabular. 

## 2. Tipos de datos y calidad

*Inspecciona los tipos que infiere cada lenguaje. Completa la tabla y comenta si los tipos son los esperados para cada variable:*

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` | int64 | dbl (num) / int | Cuantitativa discrteta/continua (monto de ventas en dolares; tipo numérico correcto)|
| `clientes` | int64 | dbl (num) / int | Cuantitativa discreta (conteo de clientes atendidos); tipo numérico correcto|
| `sucursal` | object | chr | Categórica nominal (nombre de la sucursal); tipo texto correcto|
| `region` | object | chr | Cualitativa nominal (zona geográfica); tipo texto correcto|

*¿Qué habría indicado un dato sucio si, por ejemplo, `ventas` llegara como texto?*
Si ventas en este caso era un número, presentaba inconsistencias podría aparecer como N/A, pueden aparecer el signo de $ antes de los números o las comas mal configuradas. Lo cual haría imposible poder hacer las operaciones para el análisis.

## 3. Particularidades técnicas encontradas

*Anota qué encontraste al leer cada formato (una nota por formato): ¿el JSON llegó como tabla? ¿hubo que indicar una hoja en el Excel? ¿cómo se expresan las categóricas en cada lenguaje?*
CSV (ventas.csv): Fue la lectura más directa porque ya posee estructura rectangular de filas y columnas; en Python (pd.read_csv) y en R (read_csv) se cargó en un solo paso sin parámetros adicionales.

JSON (ventas.json): No llegó como tabla directa en Python; json.load() devolvió una lista de diccionarios (list de dict), por lo que fue necesario "aplanarla" con pd.json_normalize(datos) para que cada clave pasara a ser una columna del DataFrame. En cambio, en R la función fromJSON() de jsonlite simplificó los objetos directamente a un data.frame.

Excel (ventas.xlsx): Al ser un libro que puede contener varias pestañas, fue necesario indicar explícitamente la hoja "ventas" mediante sheet_name="ventas" en Python y sheet="ventas" en R para no depender de que sea la primera pestaña por defecto.

Expresión de variables categóricas: Tanto en Python (object) como en R (chr), las variables categóricas (sucursal y region) se representan inicialmente como cadenas de texto (strings), permitiendo agrupar por etiquetas con groupby() en Python o aggregate() en R.

## 4. Indicadores para la reunión del lunes

*Calcula los indicadores con los datos consolidados y completa la tabla:*

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal | $12,008.00 (Total acumulado: $60,040) |
| Ticket promedio (ventas ÷ clientes) | $38.29 (promedio entre sucursales) / $38.07 (global: $60,040 ÷ 1,577 clientes) |
| Sucursal con mayor venta | Guayaquil Centro ($15,200 con 410 clientes) |
| Sucursal con menor venta | Cuenca ($8,540 con 210 clientes, pero con el ticket más alto: $40.67) |
| Región con mayor venta total | Sierra ($30,860 en 3 sucursales, frente a $29,180 de Costa en 2 sucursales) |

## 5. Conclusiones y recomendación
1. *Consistencia verificada entre sistemas:* Los tres archivos (ventas.csv, ventas.json y ventas.xlsx) contienen exactamente la misma información (5 filas y 4 columnas, $60,040 en ventas y 1,577 clientes) con tipos de datos limpios y listos para el análisis.

2. *Desempeño por sucursal y ticket:* Guayaquil Centro lidera la facturación individual ($15,200) y Cuenca registra la menor venta total ($8,540); sin embargo, Cuenca presenta el mayor ticket promedio por cliente ($40.67) frente al promedio general ($38.29 por sucursal / $38.07 global).

3. *Liderazgo regional y recomendación:* Aunque las dos tiendas de mayor venta individual están en la Costa ($29,180 acumulados), la región Sierra genera la mayor venta total ($30,860) al sumar tres sucursales. Se recomienda a la gerencia automatizar el reporte semanal conectando directamente el flujo de BI al CSV o JSON sin reprocesos manuales, recordando que este corte de 5 sucursales describe únicamente la semana 39 y no proyecta tendencias futuras.
