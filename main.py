# Code for UI
# Michael K

from data_module import (
    display_data,
    time_viewer,
    viewing_description,
    display_full_dataset,
    dataset_year_range,
    visualise,
    bar_chart,
    line_graph,
    scatter_plot,
)

import matplotlib as mpl
import pandas as pd

quit = False
menu = "Main Menu"
valid = True
one = 1
data_module_output = ""
input_1 = -99999
input_2 = -99999


def non(yes=True):
    "bimbimbapbap"
    return ""


menus = {
    "Main Menu": {
        "additional_description": [non, "To move through the UI write the corresponding", "number to your selected option in the input area."],
        "description": ["Select an option:", non],
        "1": ["(1) View data", "Datasets Viewer"],
        "2": ["(2) View visualisations", "Visualisations Viewer"],
        "3": ["(3) Update data", "Data Editor"],
        "4": ["(4) Calculate data", "Data Calculator"],
        "5": ["(5) Quit program", "Quit"],
    },
    "Datasets Viewer": {
        "additional_description": [viewing_description, "", ""],
        "description": ["Select an option:", display_data],
        "1": ["(1) View by year", "", time_viewer],
        "2": ["(2) View a time period", "Datasets Range Selector"],
        "3": ["(3) View specific quarter or year", "Dataset Year Range"],
        "4": ["(4) View FULL dataset", "", display_full_dataset],
        "5": ["(5) Go back to Main Menu", "Main Menu"],
    },
    "Datasets Range Selector": {
        "additional_description": [viewing_description, "", ""],
        "description": ["Please do one of the following:", display_data],
        "1": ["Enter the first year of your range (YYYY)", ""],
        "2": ["     e.g '2000'", ""],
        "3": ["or 'all' to view the full dataset", ""],
        "4": [""],
        "5": ["To go back to Main Menu enter 5", "Main Menu"],
    },
    "Dataset Year Range": {
        "additional_description": [viewing_description, "", ""],
        "description": ["Please do one of the following:", display_data],
        "1": ["Enter the first year of your range in 'YYYY' format", ""],
        "2": ["     e.g '2000-2020'", ""],
        "3": ["or 'all' to view the full dataset", ""],
        "4": [""],
        "5": ["To go back to Datasets Viewer enter 5", "Datasets Viewer"],
    },
    "Visualisations Viewer": {
        "additional_description": [viewing_description, "", ""],
        "description": ["Select a visualisation:", visualise],
        "1": ["(1) Visualisations Selector", "Visualisations Selector"],
        "2": ["(2) View by year", "", time_viewer],
        "3": ["(3) View a time period", "Dataset Year Range"],
        "4": ["(4) Select datasets to compare", "Datasets Selector"],
        "5": ["(5) Go back to Main Menu", "Main Menu"],
    },
        "Visualisations Selector": {
        "additional_description": [viewing_description, "", ""],
        "description": ["Select a visualisation:", visualise],
        "1": ["(1) Bar chart", "", bar_chart],
        "2": ["(2) Line graph", "", line_graph],
        "3": ["(3) Scatter plot", "", scatter_plot],
        "4": ["(4) Go back to Main Menu", "Main Menu"],
        "5": ["", ""],
    },
        "Datasets Selector": {
        "additional_description": [viewing_description, "", ""],
        "description": ["Select a visualisation:", visualise],
        "1": ["(1) Deselect Australian automotive fuel price change", "", ],
        "2": ["(2) Deselect Australian quartely inflation rate (CPI)", "", line_graph],
        "3": ["(3) Deselect WTI oil trades data.", "", scatter_plot],
        "4": ["(4) Select datasets to compare", "Main Menu"],
        "5": ["(5) Go back to Main Menu", "Main Menu"],
    },
    "Data Editor": {
        "additional_description": [viewing_description, "To do more advanced selection on viewing", "the dataset, go to Datasets Viewer."],
        "description": ["Select an option:", non],
        "1": ["(1) Add quarter or year", ""],
        "2": ["(2) Remove year or quarter", ""],
        "3": ["(3) Select a time range", "Datasets Range Selector"],
        "4": ["(4) Go back to Main Menu", "Main Menu"],
        "5": ["", ""],
    },
    "Data Calculator": {
        "additional_description": [non, "", ""],
        "description": ["Select an option:", non],
        "1": ["(1) Calculate averages", ""],
        "2": ["(2) Calculate medians", ""],
        "3": ["(3) Calculate modes", ""],
        "4": ["(4) View all calculations", ""],
        "5": ["(5) Go back to Main Menu", "Main Menu"],
    },
}


def selector():
    global menus
    global menu
    global valid
    global quit
    global data_module_output
    global input_1
    global input_2

    user_input = ""
    n = 0

    if menus[menu]["description"][0] != "Please do one of the following:":
        if menus[menu]["5"][0] == "":
            ranger = 4
            valid_range = ["1", "2", "3", "4"]
        else:
            ranger = 5
            valid_range = ["1", "2", "4", "3", "5"]

        if valid:
            user_input = input(f"Enter your selection (1-{ranger}): ")
        else:
            user_input = input(f"Invalid option! Enter your selection (1-{ranger}): ")
        valid = False if user_input not in valid_range else True

        if valid:
            if menus[menu][user_input][1] == "Quit":
                quit = True
            elif menus[menu][user_input][1] == "":
                data_module_output = menus[menu][user_input][2](menus, menu)
                data_module_output = menus[menu]["description"][1]()
            else:
                menu = menus[menu][user_input][1]
                data_module_output = menus[menu]["description"][1]()
    else:
        first_second = "first" if input_1 == -99999 else "second"

        if valid:
            user_input = input(f"Enter the {first_second} year of your range (YYYY) or 5 to go back to Main Menu.: ")
        else:
            user_input = input(f"Invalid option! Enter the {first_second} year of your range (YYYY-YYYY) or 5 to go back to Main Menu.: ")

        valid = (True if (user_input.isdigit() and len(user_input) == 4) or user_input == "5" else False)

        if valid and user_input != "5" and input_1 == -99999:
            input_1 = int(user_input)
            menus[menu]["1"][0] = "Enter the second year of your range (YYYY)"
            menus[menu]["2"][0] = "     e.g '2020'"
        elif valid and user_input != "5":
            input_2 = int(user_input)
            data_module_output = dataset_year_range(input_1, input_2)
            input_1 = -99999
            input_2 = -99999
        elif valid:
            menu = menus[menu][user_input][1]
            input_1 = -99999


input("""
=============================================================================================================
Oil Prices vs Inflation - Introduction
=============================================================================================================
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣶⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠶⢾⣿⣿⣿⣿⣧⣄⣀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⠛⠉⢙⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    Welcome to Michael's oil vs inflation analysis
⠀⠀⠀⠀⣠⣴⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣶⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    tool, where you can:
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        - View tables of data, on oil prices/inflation
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣴⣶⣿⣿⠿⠛⠁⠀⠘⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀        - View graphs on said data
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣭⣽⡶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀        - Ammend data
⠀⠀⢸⣿⣿⣿⣿⣿⣿⠋⠀⠈⠉⠛⠛⠿⠿⣿⣿⣇⣿⣿⣿⢿⣿⣿⣿⣟⣛⣯⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀        - Get information on data
⠀⠀⠘⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀
⠀⠀⠀⠹⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⣿⣿⣇⡄⠀⠀⠀⠉⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡇    IMPORTANT: If the lines of equal signs (headers) are 
⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⣿⣿⢻⣧⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠈⠉⠉⠛⠉⠀    folding into multiple lines, or if you cannot see the
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠙⠛⠋⢸⣿⡆⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    full UI, please adjust the terminal.
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠉⢳⣤⡞⠉⢻⣷⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠴⠋⠀⠙⠲⣜⣿⡆⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    To move through the UI write the corresponding
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣷⡒⠒⠒⠒⠒⣺⢿⣿⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    number to your selected option into the input area.
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠉⣳⣤⣖⠋⠁⠘⣿⡇⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣠⠴⠊⠁⠀⠈⠙⠲⢤⣻⣿⡀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣿⠿⠿⣍⣉⠉⠉⠉⢉⣩⡿⠟⣿⣇⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⣉⣿⠶⢾⣍⡀⠀⠀⢹⣿⡀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⢰⣿⣧⡤⠖⠛⠉⠀⠀⠀⠈⠙⠳⢦⣬⣿⣷⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀    
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃
=============================================================================================================

Begin (enter anything)? """)


while not quit:
    print(
        """
"""
        * 2000
    )
    print(f"""
=============================================================================================================
Oil Prices vs Inflation - {menu}       
=============================================================================================================
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣶⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠶⢾⣿⣿⣿⣿⣧⣄⣀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⠛⠉⢙⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    {menu}
⠀⠀⠀⠀⣠⣴⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣶⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    {menus[menu]["description"][0]} 
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["1"][0]}
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣴⣶⣿⣿⠿⠛⠁⠀⠘⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["2"][0]}
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣭⣽⡶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["3"][0]}
⠀⠀⢸⣿⣿⣿⣿⣿⣿⠋⠀⠈⠉⠛⠛⠿⠿⣿⣿⣇⣿⣿⣿⢿⣿⣿⣿⣟⣛⣯⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀        {menus[menu]["4"][0]}
⠀⠀⠘⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀        {menus[menu]["5"][0]}
⠀⠀⠀⠹⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⣿⣿⣇⡄⠀⠀⠀⠉⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡇        
⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⣿⣿⢻⣧⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠈⠉⠉⠛⠉⠀    {menus[menu]["additional_description"][0](menu)}
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠙⠛⠋⢸⣿⡆⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠉⢳⣤⡞⠉⢻⣷⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    {menus[menu]["additional_description"][1]}
⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠴⠋⠀⠙⠲⣜⣿⡆⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    {menus[menu]["additional_description"][2]}
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣷⡒⠒⠒⠒⠒⣺⢿⣿⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠉⣳⣤⣖⠋⠁⠘⣿⡇⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣠⠴⠊⠁⠀⠈⠙⠲⢤⣻⣿⡀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣿⠿⠿⣍⣉⠉⠉⠉⢉⣩⡿⠟⣿⣇⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⣉⣿⠶⢾⣍⡀⠀⠀⢹⣿⡀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⢰⣿⣧⡤⠖⠛⠉⠀⠀⠀⠈⠙⠳⢦⣬⣿⣷⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃
=============================================================================================================""")
    print(data_module_output)
    selector()

print("Quit successfully!")
