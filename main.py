import time

import matplotlib.pyplot as plt
import seaborn as sns

import getdatafromyahoo as dg
import indictors as indic
import trading as trd
from models import Stock, Index

time.sleep(1)
sns.set()
START_DATE = "01/01/2020"
END_DATE = "12/31/2020"
TICKER = "GSP"


def main():
    snp = Index("^GSPC", "INDEX")
    apple = Stock("APPL", "STOCK")
    shell = Stock("RDSA.AS", "STOCK")

    snp.load_data()
    shell.load_data()

    snp.get_relevant_info()
    shell.get_relevant_info()

    print(shell.info)
    print(snp.info)
    historical_data = dg.get_historical_data(snp.ticker, START_DATE, END_DATE)
    clean_data = clean_dataset(historical_data)
    #plot_data(clean_data["adjclose"])
    indicators = indic.build_indicators(clean_data)
    results = trd.run_trade_simulation(indicators)
    print(indicators.head(10))

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


if __name__ == "__main__":
    # execute only if run as a script
    main()
