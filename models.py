import math
import getdatafromyahoo as dg


class Asset:
    def __init__(self, tickername, assetclass):
        self.ticker = tickername
        self.assetclass = assetclass

    def get_yahoo_ticker(self):
        self.yticker = dg.set_as_ticker(self.ticker)

    def get_yahoo_info(self):
        self.yinfo = dg.get_info(self.ticker)

    def load_data(self):
        self.get_yahoo_ticker()
        self.get_yahoo_info()

class Stock(Asset):

    def get_relevant_info(self):
        df = {
            '52 Week Range': self.yticker.info["country"],
            'website': self.yticker.info["website"],
            'Industry': self.yticker.info["industry"],
            'dividendRate': self.yticker.info["dividendRate"],
            'currency': self.yticker.info["currency"],
            'EPS': self.yinfo["EPS (TTM)"].value,
            'nextEarnings': self.yinfo['Earnings Date'].value,
            'marketCap': self.yinfo['Market Cap'].value,
            'PE Ratio': self.yinfo['PE Ratio (TTM)'].value,
        }

        if math.isnan(df['PE Ratio']):
            df['PE Ratio'] = self.yticker.info['previousClose'] / df["EPS"]

        self.info = df


class Index(Asset):

    def get_relevant_info(self):
        self.info = self.yinfo.T



