import matplotlib as mpl
import pandas as pd


def placeholder():
    all_data = pd.read_csv("fuel_vs_inflation_data.csv")
    return all_data


all_data = pd.read_csv("fuel_vs_inflation_data.csv")
print(all_data)
