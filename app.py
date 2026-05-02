import yfinance as yf
import pandas as pd

def analyze_stock(stock):
    data = yf.download(stock, period="1mo")

    if data.empty:
        print("Invalid stock symbol")
        return

    # Calculate SMA
    data['SMA_5'] = data['Close'].rolling(window=5).mean()
    data['SMA_10'] = data['Close'].rolling(window=10).mean()

    print("\nLast 5 days data:")
    print(data.tail())

    # Basic signal
    if data['SMA_5'].iloc[-1] > data['SMA_10'].iloc[-1]:
        print("\nSignal: BUY 📈")
    else:
        print("\nSignal: SELL 📉")

if __name__ == "__main__":
    stock = input("Enter stock (e.g., RELIANCE.NS): ")
    analyze_stock(stock)
