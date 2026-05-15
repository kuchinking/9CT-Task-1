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
        "description": "Select an option:",
        "selector1": "View data",
        "selector2": "View visualisations",
        "selector3": "Update data",
        "selector4": "Quit program",
        "selector5": "",
    },
    "Datasets Viewer": {
        "description": "Select an option, or look at the data:",
        "selector1": "(1) Select dataset",
        "selector2": "(2) View by date, quarter or year",
        "selector3": "(3) View a time period",
        "selector4": "(4) Go back to Main Menu",
        "selector5": "",
    },
    "Datasets Selector": {
        "description": "Select an option:",
        "selector1": "(1) View entire dataset",
        "selector2": "(2) View oil prices dataset (WTI)",
        "selector3": "(3) View Australian fuel price dataset",
        "selector4": "(4) View Australian inflation dataset",
        "selector5": "(5) Go back to Datasets Viewer",
    },
    "Datasets Selector - Time": {
        "description": "Select an option:",
        "selector1": "(1) View specific year",
        "selector2": "(2) View by quarter",
        "selector3": "(3) View by year",
        "selector4": "(4) Go back to Datasets Viewer",
        "selector5": "",
    },
    "Datasets Selector - Time Period": {
        "description": "",
        "selector1": "(1) View specific year",
        "selector2": "Enter the year",
        "selector3": "(3) View by year",
        "selector4": "(4) Go back to Datasets Viewer",
        "selector5": "",
    },
}


def user_UI():  # I recommend collapsing this"selector5": "",
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
Oil Prices vs Inflation - {menu}      Currently viewing: placeholder
=============================================================================================================
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣶⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠶⢾⣿⣿⣿⣿⣧⣄⣀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    {menu} {menus[menu]["description"]}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⠛⠉⢙⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⣠⣴⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣶⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["selector1"]}
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["selector2"]}
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["selector3"]}
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣴⣶⣿⣿⠿⠛⠁⠀⠘⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["selector4"]}
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣭⣽⡶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀        {menus[menu]["selector5"]}
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
