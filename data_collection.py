import pandas as pd
import requests

def fetch_data(symbol, api_key, interval='1min'):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    # To check if the API response is valid
    if 'Time Series (1min)' in data:
        df = pd.DataFrame.from_dict(data['Time Series (1min)'], orient='index')
        df = df.rename(columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
        df = df.astype(float)
        df.index = pd.to_datetime(df.index)
        return df
    else:
        print("Error fetching data:", data)
        return None

# Fetch data example
# api_key = 'your_api_key'
# symbol = 'AAPL'
# df = fetch_data(symbol, api_key)
# print(df.head())
