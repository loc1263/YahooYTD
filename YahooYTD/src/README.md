# YahooYTD

Análisis de Rentabilidad Año a la Fecha (YTD) de Acciones y Criptomonedas usando Yahoo Finance y Python

## Descripción
Permite analizar la rentabilidad YTD (Year-To-Date) de una lista de acciones y criptomonedas, descargando los precios históricos desde Yahoo Finance y mostrando un resumen tabular de los resultados.

## Características
- Descarga de datos históricos para múltiples símbolos usando yfinance.
- Cálculo automático de la rentabilidad YTD desde el inicio del año hasta el día anterior a la fecha actual.
- Soporte para acciones, ETFs y criptomonedas.
- Presentación de resultados en tabla alineada y resumen estadístico del portafolio.
- Pesos del portafolio calculados automáticamente para todos los activos.

## Requisitos
- Python 3.8+
- Paquetes: yfinance, pandas, numpy

Instala los requisitos con:
```bash
pip install yfinance pandas numpy
```

## Uso
1. Clona el repositorio y navega a la carpeta del proyecto.
2. Activa tu entorno virtual si lo usas.
3. Ejecuta el script principal:
```bash
python src/main.py
```

Puedes modificar la lista de símbolos en el archivo `main.py` para analizar los activos que desees.

## Estructura del Proyecto
```
YahooYTD/
├── .gitignore
├── src/
│   └── main.py
├── README.md
└── ...
```

## Ejemplo de salida
```
Análisis de Rentabilidad Año a la Fecha (2025-01-01 - 2025-08-08)
======================================================================

SÍMBOLO         EMPRESA                         PRECIO INICIAL   PRECIO ACTUAL     RENTABILIDAD YTD
--------------------------------------------------------------------------------------------------------------
CHILE.SN        Banco de Chile                          104.81          137.50               31.19%
VAPORES.SN      Compañía Sud Americana de V...           54.95           49.15              -10.55%
LTM.SN          LATAM Airlines Group S.A.                13.73           20.97               52.74%
CFMDIVO.SN      Fondo Mutuo ETF It Now S&P/...         1332.22         1594.90               19.72%
ANDINA-B.SN     Embotelladora Andina S.A.              2902.22         3750.00               29.21%
SQM-B.SN        Sociedad Química y Minera d...        36290.00        37400.00                3.06%
IXN             iShares Global Tech ETF                  84.35           96.57               14.49%
AIA             iShares Asia 50 ETF                      66.71           84.69               26.95%
QQQ             Invesco QQQ Trust                       508.90          569.24               11.86%
IAU             iShares Gold Trust                       50.19           64.08               27.67%
BTC-USD         Bitcoin USD                           94419.76       114141.45               20.89%
ETH-USD         Ethereum USD                           3353.50         3683.92                9.85%
DOGE-USD        Dogecoin USD                              0.32            0.21              -36.71%

RESUMEN TOTALIZADOR
======================================================================

Rentabilidad promedio simple: +15.41%
Rentabilidad ponderada del portafolio: +15.41%

ESTADÍSTICAS ADICIONALES:
Mejor rentabilidad: +52.74% (LTM.SN)
Peor rentabilidad: -36.71% (DOGE-USD)
Desviación estándar: 21.04%

Nota: Datos obtenidos de Yahoo Finance hasta 2025-08-08
```

## Licencia
MIT