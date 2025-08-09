import yfinance as yf
import pandas as pd
from datetime import datetime, date, timedelta
import numpy as np

# Lista de acciones a analizar
symbols = ['CHILE.SN', 'VAPORES.SN', 'LTM.SN', 'CFMDIVO.SN', 'ANDINA-B.SN','SQM-B.SN','IXN','AIA','QQQ','IAU','BTC-USD','ETH-USD','DOGE-USD']

# Fecha de inicio del año actual
start_of_year = date(datetime.now().year, 1, 1)
today = date.today()


print(f"Análisis de Rentabilidad Año a la Fecha ({start_of_year} - {today})")
print("=" * 70)

# Diccionario para almacenar resultados
results = {}
num_symbols = len(symbols)
portfolio_weights = [1/num_symbols] * num_symbols  # Pesos iguales para todos los símbolos

# Descargar datos históricos de todos los símbolos en una sola llamada
hist_all = yf.download(symbols, start=start_of_year, end=today, progress=False, auto_adjust=True, group_by='ticker')

for i, symbol in enumerate(symbols):
    try:
        # Extraer precios de cierre para el símbolo
        if (len(symbols) == 1) or (symbol not in hist_all.columns.get_level_values(0)):
            # Caso especial: solo un símbolo o símbolo no encontrado
            close_prices = hist_all['Close'].dropna() if 'Close' in hist_all.columns else pd.Series(dtype=float)
        else:
            close_prices = hist_all[symbol]['Close'].dropna() if ('Close' in hist_all[symbol]) else pd.Series(dtype=float)

        if close_prices.empty:
            print(f"\nError: No se encontraron precios de cierre válidos para {symbol}")
            print(f"DataFrame descargado para {symbol}:")
            print(hist_all[symbol] if symbol in hist_all.columns.get_level_values(0) else hist_all)
            continue

        # Precio al inicio del año (primer precio disponible)
        start_price = close_prices.iloc[0].item()

        # Precio actual (último precio disponible)
        current_price = close_prices.iloc[-1].item()

        # Calcular rentabilidad YTD
        ytd_return = ((current_price - start_price) / start_price) * 100

        # Obtener información adicional de la empresa
        stock = yf.Ticker(symbol)
        info = stock.info
        company_name = info.get('longName', symbol)

        results[symbol] = {
            'company': company_name,
            'start_price': start_price,
            'current_price': current_price,
            'ytd_return': ytd_return,
            'weight': portfolio_weights[i]
        }
        print(f"\n{symbol} - {company_name}")
        print(f"  Precio inicial (01/01/{datetime.now().year}): ${start_price:.2f}")
        print(f"  Precio actual: ${current_price:.2f}")
        print(f"  Rentabilidad YTD: {ytd_return:+.2f}%")

    except Exception as e:
        print(f"\nError procesando {symbol}: {str(e)}")

# Calcular rentabilidad total del portafolio (promedio ponderado)
if results:
    print("\n" + "=" * 70)
    print("RESUMEN TOTALIZADOR")
    print("=" * 70)

    # Calcular rentabilidad promedio simple
    avg_return = np.mean([data['ytd_return'] for data in results.values()])

    # Calcular rentabilidad ponderada (asumiendo pesos iguales)
    weighted_return = sum([data['ytd_return'] * data['weight'] for data in results.values()])

    print(f"\nRentabilidad promedio simple: {avg_return:+.2f}%")
    print(f"Rentabilidad ponderada del portafolio: {weighted_return:+.2f}%")

    # Mostrar tabla resumen
    print(f"\n{'SÍMBOLO':<15} {'EMPRESA':<30} {'PRECIO INICIAL':>15} {'PRECIO ACTUAL':>15} {'RENTABILIDAD YTD':>20}")
    print("-" * 110)

    for symbol, data in results.items():
        company_short = (data['company'][:27] + "...") if len(data['company']) > 30 else data['company']
        print(f"{symbol:<15} {company_short:<30} {data['start_price']:>15.2f} {data['current_price']:>15.2f} {data['ytd_return']:>19.2f}%")

    # Estadísticas adicionales
    returns_list = [data['ytd_return'] for data in results.values()]
    print(f"\nESTADÍSTICAS ADICIONALES:")
    print(f"Mejor rentabilidad: {max(returns_list):+.2f}% ({max(results, key=lambda x: results[x]['ytd_return'])})")
    print(f"Peor rentabilidad: {min(returns_list):+.2f}% ({min(results, key=lambda x: results[x]['ytd_return'])})")
    print(f"Desviación estándar: {np.std(returns_list):.2f}%")

else:
    print("\nNo se pudieron obtener datos para ninguna acción.")

# Información adicional
print(f"\nNota: Datos obtenidos de Yahoo Finance hasta {today}")
