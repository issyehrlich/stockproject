import numpy as np


def build_indicators(dataset):
    dataset["SMA_5"] = moving_average(dataset["adjclose"], 5)
    dataset["SMA_15"] = moving_average(dataset["adjclose"], 15)
    dataset["ATR"] = average_true_ration(dataset)
    return dataset


def moving_average(dataset, interval):
    """
    function to calculate and return a simple moving average dataframe
    :param dataset: data on which you wish to calculate the simple moving average
    :param interval: time interval in which you want to calculate it over in datapoints
    :return:
    """
    simple_ma = dataset.transform(lambda x: x.rolling(window=interval).mean())
    return simple_ma


def wilder(data, periods):
    start = np.where(~np.isnan(data))[0][0]  # Check if nans present in beginning
    wilder = np.array([np.nan] * len(data))
    wilder[start + periods - 1] = data[start:(start + periods)].mean()  # Simple Moving Average
    for i in range(start + periods, len(data)):
        wilder[i] = (wilder[i - 1] * (periods - 1) + data[i]) / periods  # Wilder Smoothing
    return wilder


def average_true_ration(dataset):
    """

    :param dataset:
    :return: the average t
    """
    temp_data = dataset.copy()
    temp_data['prev_close'] = temp_data['adjclose'].shift(1)
    temp_data['TR'] = np.maximum((temp_data['high'] - temp_data['low']),
                                 np.maximum(abs(temp_data['high'] - temp_data['prev_close']),
                                            abs(temp_data['prev_close'] - temp_data['low'])))
    temp_data['ATR_5'] = wilder(temp_data['TR'], 5)
    temp_data['ATR_15'] = wilder(temp_data['TR'], 15)
    temp_data['ATR_Ratio'] = temp_data['ATR_5'] / temp_data['ATR_15']
    return temp_data['ATR_Ratio']
