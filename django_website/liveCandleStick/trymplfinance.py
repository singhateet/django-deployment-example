import os
from pathlib import Path

import mplfinance as mpf
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
file_path = os.path.join(STATIC_ROOT, '3131.csv')
df = pd.read_csv(file_path, parse_dates=True, index_col=0)
# print(df['2006':'2007'])
# Plot the candlestick chart
mpf.plot(df['2006':'2007'], type='candle', style='yahoo', title='Candlestick Chart', volume=False, mav=(5), ylabel='Price')
