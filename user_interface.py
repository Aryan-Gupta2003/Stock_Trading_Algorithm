from data_collection import fetch_data
from preprocess_data import preprocess_data, compute_indicators
from strategy import generate_signals
from backtester import Backtester
from api_key import apikey

def user_interface():
    print("Welcome to the Stock Trading Algorithm")
    print("Fetching data...")
    
    api_key = apikey()
    symbol = 'AAPL'
    df = fetch_data(symbol, api_key)
    if df is not None:
        df = preprocess_data(df)
        df = compute_indicators(df)
        df = generate_signals(df)
        
        print("Running backtest...")
        backtester = Backtester(df)
        backtester.run()
        performance = backtester.get_performance()
        print(f"Final portfolio value: {performance}")
        
        while True:
            print("\nMenu:")
            print("1. View recent trades")
            print("2. View performance")
            print("3. Exit")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                print("Recent Trades:")
                for trade in backtester.trades[-5:]:
                    print(trade)
            elif choice == '2':
                print(f"Current portfolio value: {performance}")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
