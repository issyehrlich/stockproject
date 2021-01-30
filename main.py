import math
import time

import matplotlib.pyplot as plt
import seaborn as sns

import getdatafromyahoo as dg
import indictors as indic
import trading as trd

time.sleep(1)
sns.set()
START_DATE = "01/01/2020"
END_DATE = "12/31/2020"
TICKER = "GSP"


def main():
    snp = asset_index("^GSPC", "INDEX")
    apple = asset_stock("APPL", "STOCK")
    shell = asset_stock("RDSA.AS", "STOCK")

    snp.get_yahoo_ticker()
    shell.get_yahoo_ticker()

    snp.get_relevant_info()
    shell.get_relevant_info()

    historical_data = dg.get_historical_data(snp.ticker, START_DATE, END_DATE)
    clean_data = clean_dataset(historical_data)
    plot_data(clean_data["adjclose"])
    indicators = indic.build_indicators(clean_data)
    results = trd.run_trade_simulation(indicators)
    print(indicators.head(10))



class asset:
    def __init__(self, tickername, assetclass):
        self.ticker = tickername
        self.assetclass = assetclass

    def get_yahoo_ticker(self):
        self.yticker = dg.set_as_ticker(self.ticker)

class asset_stock(asset):
    def __init__(self, ticker, assetclass):
        asset.__init__(self, ticker, assetclass)

    def get_relevant_info(self):
        self.info = get_relevant_info_stock(self.yticker)

class asset_index(asset):
    def __init__(self, ticker, assetclass):
        asset.__init__(self, ticker, assetclass)

    def get_relevant_info(self):
        self.info = get_relevant_info_index(self.yticker)

def clean_dataset(dataset):
    """
    remove unwanted data from the dataframe
    :param dataset:
    :return:
    """
    dataset = dataset.dropna()
    return dataset

def plot_data(dataset):
    fig, ax1 = plt.subplots()
    ax1.plot(dataset)
    plt.show()


def get_relevant_info_stock(ticker):
    yahoo_info = dg.get_info(ticker.ticker)

    df = {
        '52 Week Range': ticker.info["country"],
        'website': ticker.info["website"],
        'Industry': ticker.info["industry"],
        'dividendRate': ticker.info["dividendRate"],
        'currency': ticker.info["currency"],
        'EPS': yahoo_info["EPS (TTM)"].value,
        'nextEarnings': yahoo_info['Earnings Date'].value,
        'marketCap': yahoo_info['Market Cap'].value,
        'PE Ratio': yahoo_info['PE Ratio (TTM)'].value,
    }

    if math.isnan(df['PE Ratio']):
        df['PE Ratio'] = ticker.info['previousClose'] / df["EPS"]

    return df

def get_relevant_info_index(ticker):
    yahoo_info = dg.get_info(ticker.ticker)
    return yahoo_info.T

if __name__ == "__main__":
    # execute only if run as a script
    main()
