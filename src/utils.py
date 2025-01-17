import pandas as pd
import json
import pickle

def time_unix_from_datetime_ms(x):
    """Returns unix format integer time from pandas series x"""
    return [1000 * int(x_.timestamp()) for x_ in
                pd.to_datetime(x, unit="ms")]

def read_json(file):
    # read a single file
    with open(file, "r") as f:
        data_json = json.load(f)
    return data_json
    del data_json
    
def read_pickle(file):
    with open(file, 'rb') as f:
        return pickle.load(f)