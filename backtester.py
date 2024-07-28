class Backtester:
    def __init__(self, df, initial_capital=10000):
        self.df = df
        self.initial_capital = initial_capital
        self.capital = initial_capital
        self.position = 0
        self.trades = []

    def run(self):
        for index, row in self.df.iterrows():
            if row['positions'] == 1:
                self.buy(row['close'], index)
            elif row['positions'] == -1:
                self.sell(row['close'], index)

    def buy(self, price, date):
        self.position = self.capital // price
        self.capital -= self.position * price
        self.trades.append(('BUY', price, date))
        
    def sell(self, price, date):
        self.capital += self.position * price
        self.position = 0
        self.trades.append(('SELL', price, date))
        
    def get_performance(self):
        print('Initial Capital: ', self.initial_capital)
        return self.capital + self.position * self.df.iloc[-1]['close']
