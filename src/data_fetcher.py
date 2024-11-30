
import yfinance as yf
import pandas as pd

def get_historical_data(ticker, start_date, end_date):
    data = yf.download(tickers=ticker, start=start_date, end=end_date, interval='1d', progress=False)
    data.dropna(inplace=True)
    return data
