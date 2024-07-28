import pandas as pd
import pandas_ta as ta

def preprocess_data(df):
    df = df.sort_index()
    df = df.ffill().bfill()
    return df

def compute_indicators(df):
    # SMA - Simple Moving Average - 14 day average price range
    # RSI - Relative Strength Index - >30 oversold and <70 overbought
    # MACD - Moving Average Convergence Divergence - strength
    df['SMA_30'] = ta.sma(df['close'], length=30)
    df['SMA_100'] = ta.sma(df['close'], length=100)
    df['RSI'] = ta.rsi(df['close'], length=14)
    macd = ta.macd(df['close'])
    df['MACD'] = macd['MACD_12_26_9']
    df['MACD_signal'] = macd['MACDs_12_26_9']
    df['MACD_hist'] = macd['MACDh_12_26_9']
    return df
