import matplotlib.pyplot as plt
import pandas as pd


all_data = pd.read_csv("fuel_vs_inflation_data.csv")

current_data_state = {
    "by_time_period": "quarter",
    "time_period": ["1974-2026", 1974, 2026],
    "specific_time": [False, 1],
    "full_dataset": "summarised",
    "visualisation": ["scatter", "scatter plot"]
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


def viewing_description(menu):
    if menu != "Visualisations Viewer" and menu != "Data Editor":
        return f"Currently viewing {current_data_state['time_period'][0]} by {current_data_state['by_time_period']}"
    elif menu == "Visualisations Viewer":
        return f"Currently viewing {current_data_state['visualisation'][1]} from {current_data_state['time_period'][0]} by {current_data_state['by_time_period']}"

def display_full_dataset(menus, menu):
    if current_data_state["full_dataset"]:
        current_data_state["full_dataset"] = "full"
        menus[menu]["4"][0] = "(4) View SUMMARISED dataset"
    else:
        current_data_state["full_dataset"] = "summarised"
        menus[menu]["4"][0] = "(4) View FULL dataset"


def dataset_year_range(a, b):
    current_data_state["time_period"][0] = f"{a}-{b}"
    current_data_state["time_period"][1] = a
    current_data_state["time_period"][2] = b
    return a + b

def visualise():
    all_data.plot(
        kind = current_data_state["visualisation"][0],
        x = "Fuel" if current_data_state["visualisation"][0] == "scatter" else "Date",
        y = "Inflation" if current_data_state["visualisation"][0] == "scatter" else ["Fuel", "Inflation"],
        color = "blue",
        alpha = 0.3,
        title = "Correlation of fuel prices and inflation",
        )
    plt.show()


def bar_chart(menus, menu):
    current_data_state["visualisation"][0] = "bar"
    current_data_state["visualisation"][1] = "bar chart"
def line_graph(menus, menu):
    current_data_state["visualisation"][0] = "line"
    current_data_state["visualisation"][1] = "line graph"
def scatter_plot(menus, menu):
    current_data_state["visualisation"][0] = "scatter"
    current_data_state["visualisation"][1] = "scatter plot"