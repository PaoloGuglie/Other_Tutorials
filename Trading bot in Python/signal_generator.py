import yfinance as yf  # (Yfinance allows only the last 60 days of data)
import pandas as pd


# Define my signal function
def signal_generator(datapoint):
    current_open = datapoint.Open.iloc[-1].item()
    current_close = datapoint.Close.iloc[-1].item()
    previous_open = datapoint.Open.iloc[-2].item()
    previous_close = datapoint.Close.iloc[-2].item()

    # Bearish pattern
    if (current_open > current_close and
            previous_open > previous_close and
            current_close < previous_open and
            current_open >= previous_close):
        return 1

    # Bullish pattern
    elif (current_open < current_close and
          current_close > previous_open > previous_close >= current_open):
        return 2

    # No clear pattern
    else:
        return 0


dataframe = yf.download("EURUSD=X", start="2025-02-01", end="2025-03-01", interval='15m')

# Get signals
signals = [0]
for i in range(1, len(dataframe)):
    datapoint = dataframe[i-1:i+1]
    signals.append(signal_generator(datapoint))

# Add a new "signal" column in my testing dataframe
dataframe["signals"] = signals
