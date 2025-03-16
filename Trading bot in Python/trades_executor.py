# Example using OANDA
import pandas as pd

from apscheduler.schedulers.blocking import BlockingScheduler
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
from oandapyV20.contrib.requests import MarketOrderRequest
from oanda_candles import Pair, Gran, CandleCollector, CandleClient
from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails

from config import access_token, accountID


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


def get_candles(n):
    # access_token = 'XXXXXXX'. I need a token generated from an OANDA account
    client = CandleClient(access_token, real=False)
    collector = client.get_collector(Pair.EUR_USD, Gran.M15)
    candles = collector.grab(n)
    return candles


def trading_job():
    candles = get_candles(3)
    dataframe_stream = pd.DataFrame(columns=['Open', 'Close', 'High', 'Low'])

    # Fill the candle info in the dataframe
    i = 0
    for candle in candles:
        dataframe_stream.loc[i, ['Open']] = float(str(candle.bid.o))
        dataframe_stream.loc[i, ['Close']] = float(str(candle.bid.o))
        dataframe_stream.loc[i, ['High']] = float(str(candle.bid.o))
        dataframe_stream.loc[i, ['Low']] = float(str(candle.bid.o))
        i += 1

    # Cast the column types to float
    dataframe_stream['Open'] = dataframe_stream['Open'].astype(float)
    dataframe_stream['Close'] = dataframe_stream['Close'].astype(float)
    dataframe_stream['High'] = dataframe_stream['High'].astype(float)
    dataframe_stream['Low'] = dataframe_stream['Low'].astype(float)

    # Call the signal function with the created dataframe
    signal = signal_generator(dataframe_stream.iloc[:-1, :])

    # EXECUTING ORDERS
    # accountID = "XXXXXXX". My account ID here
    client = API(access_token)

    # define stop loss and take profit ratio
    SLTP_ratio = 2.
    previous_candle_result = abs(dataframe_stream['High'].iloc[-2] - dataframe_stream['Low'].iloc[-2])
    # stop losses
    SL_Buy = float(str(candle.bid.o)) - previous_candle_result
    SL_Sell = float(str(candle.bid.o)) + previous_candle_result
    # take profits
    TP_Buy = float(str(candle.bid.o)) + previous_candle_result * SLTP_ratio
    TP_Sell = float(str(candle.bid.o)) - previous_candle_result * SLTP_ratio

    # Sell
    if signal == 1:
        market_order = MarketOrderRequest(
            instrument="EUR_USD",
            units=-1000,
            takeProfitOnFill=TakeProfitDetails(price=TP_Sell).data,
            stopLossOnFill=StopLossDetails(price=SL_Sell).data)

        r = orders.OrderCreate(accountID, data=market_order.data)
        rv = client.request(r)
        print(rv)

    # Buy
    elif signal == 2:
        market_order = MarketOrderRequest(
            instrument="EUR_USD",
            units=1000,
            takeProfitOnFill=TakeProfitDetails(price=TP_Buy).data,
            stopLossOnFill=StopLossDetails(price=SL_Buy).data
        )
        r = orders.OrderCreate(accountID, data=market_order.data)
        rv = client.request(r)
        print(rv)


# Scheduler
scheduler = BlockingScheduler()
scheduler.add_job(
    trading_job,
    'cron',
    day_of_week='mon-fri',
    hour='00-23',
    minute='1, 16, 31, 46',
    start_date='2025-03-01 12:00:00',
    timezone='America/Chicago'
)
scheduler.start()
