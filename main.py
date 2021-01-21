import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import getdatafromyahoo as dg
import math
import indictors as indic

time.sleep(1)
sns.set()
START_DATE = "01/01/2020"
END_DATE = "12/31/2020"
TICKER = "RDSA.AS"


def main():
    ticker = dg.set_as_ticker(TICKER)
    stock_info = get_relevant_info(ticker)
    historical_data = dg.get_historical_data(ticker.ticker, START_DATE, END_DATE)
    clean_data = clean_dataset(historical_data)
    plot_data(clean_data["adjclose"])
    indicators = indic.build_indicators(clean_data)

    print(clean_data)
    print(stock_info)

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
        df['PE Ratio'] = ticker.info['previousClose'] / df["EPS"]

    return df


if __name__ == "__main__":
    # execute only if run as a script
    main()
