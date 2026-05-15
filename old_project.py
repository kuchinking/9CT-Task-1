# Code for UI
# Michael K


import os
import matplotlib as mpl
import pandas as pd

quit = False
menu = "Introduction"
valid = True


menus = {
    "Main Menu": {
        "header_description": "",
        "description": "Select an option:",
        "1": "View data",
        "2": "View visualisations",
        "3": "Update data",
        "4": "Quit program",
        "5": "",
    },
    "Datasets Viewer": {
        "header_description": "",
        "description": "Select an option, or look at the data:",
        "1": ["(1) Select dataset", "Datasets Selector"],
        "2": "(2) View by date, quarter or year",
        "3": "(3) View a time period",
        "4": "(4) Go back to Main Menu",
        "5": "",
    },
    "Datasets Selector": {
        "description": "Select an option:",
        "1": "(1) View entire dataset",
        "2": "(2) View oil prices dataset (WTI)",
        "3": "(3) View Australian fuel price dataset",
        "4": "(4) View Australian inflation dataset",
        "5": "(5) Go back to Datasets Viewer",
    },
    "Datasets Selector - Time": {
        "description": "Select an option:",
        "1": "(1) View specific year",
        "2": "(2) View by quarter",
        "3": "(3) View by year",
        "4": "(4) Go back to Datasets Viewer",
        "5": "",
    },
    "Datasets Selector - Time Period": {
        "description": "",
        "1": "(1) View specific year",
        "2": "Enter the year",
        "3": "(3) View by year",
        "4": "(4) Go back to Datasets Viewer",
        "5": "",
    },
}


def selector():
    global menus
    global menu
    if {menus[menu]["5"][0]} == "":
        if valid:
            user_input = input("Enter your selection (1-4): ")
        else:
            user_input = input("Invalid option! Enter your selection (1-4): ")
    else:
        if valid:
            user_input = input("Enter your selection (1-5): ")
        else:
            user_input = input("Invalid option! Enter your selection (1-5): ")


def user_UI():  # I recommend collapsing this"5": "",
    global menu
    if menu == "Introduction":
        user_UI = f"""
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
"""  # noqa: F541
    elif menu == "Main Menu":
        user_UI = f"""
=============================================================================================================
Oil Prices vs Inflation - Main Menu
=============================================================================================================
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣶⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠶⢾⣿⣿⣿⣿⣧⣄⣀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    Main Menu - Select an option:
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⠛⠉⢙⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⣠⣴⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣶⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        (1) View datasets
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        (2) View visualisations
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        (3) Update data
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣴⣶⣿⣿⠿⠛⠁⠀⠘⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀        (4) Quit program
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣭⣽⡶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀        
⠀⠀⢸⣿⣿⣿⣿⣿⣿⠋⠀⠈⠉⠛⠛⠿⠿⣿⣿⣇⣿⣿⣿⢿⣿⣿⣿⣟⣛⣯⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀        
⠀⠀⠘⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀
⠀⠀⠀⠹⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⣿⣿⣇⡄⠀⠀⠀⠉⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡇    
⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⣿⣿⢻⣧⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠈⠉⠉⠛⠉⠀    
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠙⠛⠋⢸⣿⡆⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀
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
"""  # noqa: F541
    elif menu == "Datasets Viewer" or menu == "Datasets Selection":
        user_UI = f"""
=============================================================================================================
Oil Prices vs Inflation - {menu}      {menus[menu]["header_description"]}
=============================================================================================================
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣶⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠶⢾⣿⣿⣿⣿⣧⣄⣀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    {menu} - {menus[menu]["description"]}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⠛⠉⢙⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⣠⣴⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣶⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["1"][0]}
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["2"]}
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["3"]}
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣴⣶⣿⣿⠿⠛⠁⠀⠘⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["4"]}
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣭⣽⡶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["5"]}
⠀⠀⢸⣿⣿⣿⣿⣿⣿⠋⠀⠈⠉⠛⠛⠿⠿⣿⣿⣇⣿⣿⣿⢿⣿⣿⣿⣟⣛⣯⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀        
⠀⠀⠘⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀
⠀⠀⠀⠹⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⣿⣿⣇⡄⠀⠀⠀⠉⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡇    To move through the UI write the corresponding
⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⣿⣿⢻⣧⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠈⠉⠉⠛⠉⠀    number to your selected option into the input area.
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠙⠛⠋⢸⣿⡆⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠉⢳⣤⡞⠉⢻⣷⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠴⠋⠀⠙⠲⣜⣿⡆⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣷⡒⠒⠒⠒⠒⣺⢿⣿⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠉⣳⣤⣖⠋⠁⠘⣿⡇⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣠⠴⠊⠁⠀⠈⠙⠲⢤⣻⣿⡀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣿⠿⠿⣍⣉⠉⠉⠉⢉⣩⡿⠟⣿⣇⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⣉⣿⠶⢾⣍⡀⠀⠀⢹⣿⡀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⢰⣿⣧⡤⠖⠛⠉⠀⠀⠀⠈⠙⠳⢦⣬⣿⣷⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃
=============================================================================================================
"""
    return user_UI


while not quit:
    print(user_UI())

    if menu == "Introduction":
        user_input = input("Begin (enter anything)? ")
        menu = "Main Menu"

    elif menu == "Main Menu":
        if valid:
            user_input = input("Enter your selection (1-4): ")
        else:
            user_input = input("Invalid option! Enter your selection (1-4): ")

        if user_input == "1":
            valid = True
            menu = "Datasets Viewer"
        elif user_input == "2":
            valid = True
            menu = "Visualisations Viewer"
        elif user_input == "3":
            valid = True
            menu = "Data Editor"
        elif user_input == "4":
            quit = True
        else:
            valid = False

    elif menu == "Datasets Viewer":
        if valid:
            user_input = input("Enter your selection (1-4): ")
        else:
            user_input = input("Invalid option! Enter your selection (1-4): ")

        if user_input == "1":
            valid = True
            menu = "Datasets Selection"
        elif user_input == "2":
            valid = True
            menu = "Datasets Selector - Time"
        elif user_input == "2":
            valid = True
            menu = "Datasets Selector - Time"
        else:
            valid = False
    elif menu == "Datasets Selection":
        input()


print("Quit successfully!")
