import yfinance as yf
import yahoo_fin.stock_info as si


def set_as_ticker(stock_name):
    ticker = yf.Ticker(stock_name)
    return ticker


def get_info(ticker):
    info = si.get_quote_table(ticker, dict_result=False)
    info = info.set_index("attribute").T
    return info


def get_historical_data(ticker, startdate, enddate):
    hist = si.get_data(ticker, start_date=startdate, end_date=enddate, interval="1d")
    return hist
