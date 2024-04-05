import os 
import yfinance as yf


class DataCollector:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self):
        if not os.path.exists(os.path.join(os.getcwd(), "lstm", "data")):
            os.makedirs(os.path.join(os.getcwd(), "lstm", "data"))
        data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        data = data.to_csv(os.path.join(os.getcwd(), "lstm", "data", f"{self.ticker}.csv"))
        return "Data downloaded successfully!"
    
if __name__ == "__main__":
    btc = DataCollector("BTC-CAD", "2015-01-01", "2021-01-01")
    print(btc.get_data())

    doge = DataCollector("DOGE-CAD", "2015-01-01", "2021-01-01")
    print(doge.get_data())

    eth = DataCollector("ETH-CAD", "2015-01-01", "2021-01-01")
    print(eth.get_data())

    ltc = DataCollector("LTC-CAD", "2015-01-01", "2021-01-01")
    print(ltc.get_data())

    shiba = DataCollector("SHIB-CAD", "2015-01-01", "2021-01-01")
    print(shiba.get_data())
