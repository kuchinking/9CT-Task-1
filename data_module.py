import matplotlib as plt
import pandas as pd


all_data = pd.read_csv("fuel_vs_inflation_data.csv")

current_data_state = {
    "by_time_period": "quarter",
    "time_period": "1974-2026",
    "specific_time": [False, 1],
    "full_dataset": False,
}


def display_data():
    global all_data
    return all_data


def search():
    "god knows"


def range():
    67


def time_viewer(menus, menu):

    if current_data_state["by_time_period"] == "quarter":
        current_data_state["by_time_period"] = "year"
        menus[menu]["1"][0] = "(1) View by quarter"
    else:
        current_data_state["by_time_period"] = "quarter"
        menus[menu]["1"][0] = "(1) View by year"


def viewing_description():
    return f"Currently viewing {current_data_state['by_time_period']} by {current_data_state['by_time_period']}"


def display_full_dataset(menus, menu):
    if current_data_state["full_dataset"]:
        current_data_state["full_dataset"] = False
        menus[menu]["4"][0] = "(4) View SUMMARISED dataset"
    else:
        current_data_state["full_dataset"] = True
        menus[menu]["4"][0] = "(4) View FULL dataset"
