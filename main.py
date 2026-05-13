# Code for UI
# Michael Kuchin


import os
import matplotlib as mpl
import pandas as pd
quit = False
menu = "Intoduction"
inflation = 67
def oilman():
    timer += 1
sixseven = """
6
7
6
"""
body = f"""
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
⠀⠀⠀⠹⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⣿⣿⣇⡄⠀⠀⠀⠉⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡇    To move through the UI write the corresponding
⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⣿⣿⢻⣧⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠈⠉⠉⠛⠉⠀    number to your selected option into the input area.
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠙⠛⠋⢸⣿⡆⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠉⢳⣤⡞⠉⢻⣷⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠴⠋⠀⠙⠲⣜⣿⡆⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    *** If the lines of equal signs (headers) are folding into
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣷⡒⠒⠒⠒⠒⣺⢿⣿⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    multiple lines, please increase the size of your terminal
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠉⣳⣤⣖⠋⠁⠘⣿⡇⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    window. 
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣠⠴⠊⠁⠀⠈⠙⠲⢤⣻⣿⡀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣿⠿⠿⣍⣉⠉⠉⠉⢉⣩⡿⠟⣿⣇⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀    {sixseven}
⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⣉⣿⠶⢾⣍⡀⠀⠀⢹⣿⡀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⢰⣿⣧⡤⠖⠛⠉⠀⠀⠀⠈⠙⠳⢦⣬⣿⣷⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃
=============================================================================================================
"""
def heading():
    global menu
    header = f"""
    =============================================================================================================
    Oil Prices vs Inflation - {menu}
    ============================================================================================================="""
    return header

begin = input(f"""
{heading()}
Comparing the effect of oil prices on inflation and various metrics of cost of living in Australia.
{body}

Begin (enter anything)? """)
while not quit:
    menu = "Main Menu"
    heading = heading
    option = input(f"""
{heading()}
{body}
Options: View dataset (1), 
Select an option (1-67): """)
    
    if option == "1":
        "idk"
    quit = True
print("program quit")