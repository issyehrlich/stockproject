import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import getdatafromyahoo as dg
import math

time.sleep(1)
sns.set()

def main():
    ticker = dg.set_as_ticker("RDSA.AS")
    stock_info = get_relevant_info(ticker)
    print("stock_info")
    #historal_data = get_historical_data(ticker, startdate, enddate)
    #print(historical_data)
    print(stock_info)



def get_all_revelant_info(ticker):
    info = dg.get_stock_info(ticker.ticker)
    return info


def get_relevant_info(ticker):
    yahoo_info = dg.get_stock_info(ticker.ticker)


    df = {
        'Country': ticker.info["country"],
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
        df['PE Ratio'] = ticker.info['previousClose']/df["EPS"]

    return df


if __name__ == "__main__":
    # execute only if run as a script
    main()
