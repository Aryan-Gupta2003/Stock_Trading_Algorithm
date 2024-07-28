def generate_signals(df):
    df['signal'] = 0
    df.loc[df['RSI'] < 30, 'signal'] = 1
    df.loc[df['RSI'] > 70, 'signal'] = -1
    df['positions'] = df['signal'].diff()
    return df
