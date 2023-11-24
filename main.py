import plotly.graph_objects as go
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
import process as pr
import pandas as pd


def graph_plotly(df):

    fig = go.Figure(
        data=[go.Candlestick(x=df['tradedate'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])]
    )
    fig.show()
    
    return 0


yndxdf = pd.read_csv('YNDX.csv', sep=';')
flotdf = pd.read_csv('FLOT.csv', sep=';')
yndxdf['tradedate'] = pd.to_datetime(yndxdf['tradedate'], format=r'%Y-%m-%d')
flotdf['tradedate'] = pd.to_datetime(flotdf['tradedate'], format=r'%Y-%m-%d')
# yndxdf.set_index('tradedate', inplace=True)
# flotdf.set_index('tradedate', inplace=True)



if __name__ == '__main__':
    graph_plotly(flotdf.iloc[670:800])