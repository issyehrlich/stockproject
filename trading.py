import numpy as np

def run_trade_simulation(df):
    trade_open = False
    for index, row in df.iterrows():
       if row["SMA_5"] == "nan":
           print("HI")
       else:
           if (row["open"] > row["SMA_5"]) and not trade_open:
               trade_open = True


