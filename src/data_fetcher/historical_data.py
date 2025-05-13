import yfinance as yf
import matplotlib.pyplot as plt

def fetch_historical_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

def plot_historical_data(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label='Close Price')
    plt.title("Historical Price Data")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()