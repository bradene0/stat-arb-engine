import yfinance as yf 
def load_prices(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)["Adj Close"]
    return data.dropna()
