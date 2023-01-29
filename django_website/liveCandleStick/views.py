import os
from pathlib import Path

from django.shortcuts import render
import plotly.graph_objs as go
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
file_path = os.path.join(STATIC_ROOT, '3131.csv')
df = pd.read_csv(file_path, parse_dates=True, index_col=0)

def chart_view(request):
    # data preprocessing and calculations
    window = 10
    df["MA"] = df['close'].rolling(window=window).mean()

    # create the plotly chart
    trace1 = go.Candlestick(x=df.index,
                            open=df['open'],
                            high=df['high'],
                            low=df['low'],
                            close=df['close'])

    trace2 = go.Bar(x=df.index, y=df['volume'], name='Volume')

    trace3 = go.Scatter(x=df.index, y=df['MA'], name='MA' + str(window), line=dict(color='red', width=1))

    data = [trace1, trace2, trace3]

    layout = go.Layout(title='Candlestick Chart with Volume and Moving Average', xaxis=dict(type='date'),
                       yaxis=dict(title='Price'), yaxis2=dict(title='Volume', overlaying='y', side='right'))

    fig = go.Figure(data=data, layout=layout)

    # convert the plotly chart to JSON
    plot_div = fig.to_json()

    # render the template
    return render(request, 'chart.html', {'plot_div': plot_div})