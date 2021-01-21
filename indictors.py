
def build_indicators(dataset):
    SMA_5 = moving_average(dataset, 5)
    SMA_15 = moving_average(dataset, 15)
    print(SMA_15)

def moving_average(dataset, interval):
    simple_ma = dataset.transform(lambda x: x.rolling(window = interval).mean())
    return simple_ma