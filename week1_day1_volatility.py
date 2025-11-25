#week1/day1_volatility.py
import yfinance as yf
import pandas as pd
import datetime as dt

ticker = "AAPL"

data = yf.download(ticker, period="3mo")
data["Return"] = data["Close"].pct_change()
vol_30d = data["Return"].tail(30).std() * (252 ** 0.5)
print(f"{ticker} 30-day annualized volatility: {vol_30d:.2%}")
