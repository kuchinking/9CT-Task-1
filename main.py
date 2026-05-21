# Code for UI
# Michael K

from data_module import (
    display_data,
    data_info,
    viewing_description,
    display_full_dataset,
    dataset_year_range,
    visualise,
    bar_chart,
    line_graph,
    scatter_plot,
    search,
    averages
)

quit = False
menu = "Main Menu"
valid = True
data_module_output = ""
input_1 = -99999
input_2 = -99999


def non(yes=True):
    "bimbimbapbap"
    return ""


menus = {
    "previous_menu": "menu",
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
        "1": ["(1) View info on data", "", data_info],
        "2": ["(2) View a time period", "Datasets Range Selector"],
        "3": ["(3) Search for a specific quarter or year", "Datasets Search"],
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
    "Datasets Search": {
        "additional_description": [viewing_description, "", ""],
        "description": ["Please do one of the following:", non],
        "1": ["Enter the year you are searching for.", ""],
        "2": ["", ""],
        "3": ["", ""],
        "4": ["", ""],
        "5": ["To go back to Datasets Viewer enter 5", "Datasets Viewer"],
    },
    "Visualisations Viewer": {
        "additional_description": [viewing_description, "", ""],
        "description": ["Select a visualisation:", visualise],
        "1": ["(1) Visualisations Selector", "Visualisations Selector"],
        "2": ["(2) View by year", "", non],
        "3": ["(3) View a time period", "Visualisations Range Selector"],
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
    "Visualisations Range Selector": {
        "additional_description": [viewing_description, "", ""],
        "description": ["Please do one of the following:", visualise],
        "1": ["Enter the first year of your range (YYYY)", ""],
        "2": ["     e.g '2000'", ""],
        "3": ["or 'all' to view the full dataset", ""],
        "4": [""],
        "5": ["To go back to Visualisations Viewer enter 5", "Visualisations Viewer"],
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
        "1": ["(1) Add quarter", "", add_quarter],
        "2": ["(2) Remove year or quarter", "", ],
        "3": ["(3) Select a time range", "Datasets Range Selector"],
        "4": ["(4) Go back to Main Menu", "Main Menu"],
        "5": ["", ""],
    },
    "Data Calculator": {
        "additional_description": [non, "", ""],
        "description": ["Select an option:", averages],
        "1": ["(1) Calculate averages, mean and mode for a specific time period", ""],
        "2": ["(2) Calculate percentage change between two years", ""],
        "3": ["(3) Find the lowest/highest changes", ""],
        "4": ["(4) Go back to Main Menu", "Main Menu"],
        "5": ["", ""],
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

    if menus[menu]["description"][0] != "Please do one of the following:" and input_1 == -99999:
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
            elif menu == "Data Editor":
                input_1 = user_input
            elif menus[menu][user_input][1] == "":
                menus[menu][user_input][2](menus, menu)
                data_module_output = menus[menu]["description"][1]()
            else:
                menus["previous_menu"] = menu
                menu = menus[menu][user_input][1]
                data_module_output = menus[menu]["description"][1]()

    elif menu == "Datasets Range Selector" or menu == "Visualisations Range Selector":
        first_second = "first" if input_1 == -99999 else "second"

        if valid:
            user_input = input(f"Enter the {first_second} year of your range (YYYY) or 5 to go back to Main Menu: ")
        else:
            user_input = input(f"Invalid option! Enter the {first_second} year of your range (YYYY-YYYY) or 5 to go back to Main Menu: ")

        valid = (True if (user_input.isdigit() and len(user_input) == 4 and 1973 < int(user_input) < 2027) or user_input == "5" else False)

        if valid and user_input != "5" and input_1 == -99999:
            input_1 = int(user_input)
            menus[menu]["1"][0] = "Enter the second year of your range (YYYY)"
            menus[menu]["2"][0] = "     e.g '2020'"
        elif valid and user_input != "5":
            input_2 = int(user_input)
            dataset_year_range(input_1, input_2, True) if menu == "Visualisations Range Selector" else dataset_year_range(input_1, input_2, False)
            input_1 = -99999
        elif valid:
            menus["previous_menu"] = menu
            menu = menus[menu][user_input][1]
            input_1 = -99999
        data_module_output = menus[menu]["description"][1]() if input_2 != -99999 or menu == "Datasets Range Selector" else ""
        input_2 = -99999
    elif menu == "Datasets Search":
        first_second = "year you wish to search for (e.g 2020)" if input_1 == -99999 else "quarter you want to search for or 'full' to search for the whole year"

        if valid:
            user_input = input(f"Enter the {first_second}, or 5 to go back to Main Menu: ")
        else:
            user_input = input(f"Invalid option! Enter the {first_second}, or 5 to go back to Main Menu: ")

        if first_second == "year you wish to search for (e.g 2020)":
            valid = (True if (user_input.isdigit() and 1973 < int(user_input) < 2027) or user_input == "5" else False)

            if valid and user_input != "5" and input_1 == -99999:
                input_1 = int(user_input)
                menus[menu]["1"][0] = "Enter the quarter you wish to search for (e.g 1)"
                menus[menu]["2"][0] = "     or 'full' to search the full year."
            elif valid:
                menus["previous_menu"] = menu
                menu = menus[menu][user_input][1]

        else:
            valid = True if user_input in ["1", "2", "3", "4", "5", "full"] else False

            if valid and user_input != "5" and user_input != "full":
                data_module_output = search(input_1, int(user_input))
            elif valid and user_input != "5":
                data_module_output = search(input_1, 5)
            elif valid:
                menu = menus[menu][user_input][1]
            if valid:
                input_1 = -99999
    elif menu == "Data Editor":
        input_2 = []
        if input_1 == "1":
            if valid:
                user_input = "Enter the year you wish to add an entry for (e.g 2026): "
            else:
                user_input = "Invalid option! Enter the year you wish to add an entry for (e.g 2026): "
            valid = True if len(user_input) == 4 and user_input.isdigit() else False
            input_2 = user_input

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
print(
        """
"""
        * 2000
        + """
=============================================================================================================
Quit Successfully! - Thanks for using the program, from Michael K
=============================================================================================================
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣶⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠶⢾⣿⣿⣿⣿⣧⣄⣀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⠛⠉⢙⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⣠⣴⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣶⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣴⣶⣿⣿⠿⠛⠁⠀⠘⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣭⣽⡶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀      
⠀⠀⢸⣿⣿⣿⣿⣿⣿⠋⠀⠈⠉⠛⠛⠿⠿⣿⣿⣇⣿⣿⣿⢿⣿⣿⣿⣟⣛⣯⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀    
⠀⠀⠘⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀   
⠀⠀⠀⠹⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⣿⣿⣇⡄⠀⠀⠀⠉⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡇        
⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⣿⣿⢻⣧⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠈⠉⠉⠛⠉⠀ 
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
"""
    )

