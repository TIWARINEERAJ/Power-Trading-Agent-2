import pandas as pd

def calculate_moving_average(data, window):
    data[f"MA_{window}"] = data['Close'].rolling(window=window).mean()
    return data

def calculate_volume_indicator(data):
    data['Volume_Indicator'] = data['Volume'] / data['Volume'].mean()
    return data