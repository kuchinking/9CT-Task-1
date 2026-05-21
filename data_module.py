import matplotlib.pyplot as plt
import pandas as pd


all_data = pd.read_csv("fuel_vs_inflation_data.csv", index_col = "Date")

current_data_state = {
    "by_time_period": "quarter",
    "time_period": ["1974-2026", 1974, 2026],
    "specific_time": [False, 1],
    "full_dataset": "summarised",
    "visualisation": ["scatter", "scatter plot"],
    "quarters": ["-03-01", "-06-01", "-09-01", "-12-01"]
}


def display_data():
    global all_data
    display = []
    if current_data_state["by_time_period"] == "quarter":
        for x in range(current_data_state["time_period"][1], current_data_state["time_period"][2] + 1):
            for quarter in current_data_state["quarters"]:
                if str(x) + quarter in all_data.index:
                    display.append(all_data.loc[[str(x) + quarter]])
    else:
        for x in range(current_data_state["time_period"][1], current_data_state["time_period"][2] + 1):
            if str(x) + "-03-01" in all_data.index:
                display.append(all_data.loc[[str(x) + "-03-01"]])

    if current_data_state["full_dataset"] == "summarised":
        return pd.concat(display)
    else:
        67
def search(year, quarter):
    year = str(year)
    search = pd.DataFrame()
    if quarter == 5:
        search = []
        for quarter in current_data_state["quarters"]:
            if year + quarter in all_data.index:
                search.append(all_data.loc[[year + quarter]])
    else:
        if year + current_data_state["quarters"][quarter - 1] in all_data.index:
            search = all_data.loc(current_data_state["quarters"][quarter - 1])
    pd.concat(search) if search is list else search
    return search




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
    if current_data_state["full_dataset"] == "summarised":
        current_data_state["full_dataset"] = "full"
        menus[menu]["4"][0] = "(4) View SUMMARISED dataset"
    else:
        current_data_state["full_dataset"] = "summarised"
        menus[menu]["4"][0] = "(4) View FULL dataset"


def dataset_year_range(a, b):
    if a < b:
        current_data_state["time_period"][0] = f"{a}-{b}"
        current_data_state["time_period"][1] = a
        current_data_state["time_period"][2] = b
    else:
        current_data_state["time_period"][0] = f"{b}-{a}"
        current_data_state["time_period"][1] = b
        current_data_state["time_period"][2] = a

def visualise():
    if current_data_state["visualisation"][0] == "scatter":
        all_data.plot(
            kind = current_data_state["visualisation"][0],
            x = "Fuel",
            y = "Inflation",
            color = "blue",
            alpha = 0.3,
            title = "Correlation of fuel prices and inflation",
            )
    else:
        all_data.plot(
            kind = current_data_state["visualisation"][0],
            y = ["Fuel", "Inflation"],
            color = "blue",
            alpha = 0.3,
            title = f"Fuel Prices and Inflation from {current_data_state['by_time_period'][0]}",
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