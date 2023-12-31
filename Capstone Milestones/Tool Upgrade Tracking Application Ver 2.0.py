#Allows pysimplegui library to be used
import PySimpleGUI as sg

import sqlite3
from sqlite3 import Error

#Allows for dollar values to be shown correctly
import locale

#Determines the color of GUI
sg.theme('DarkGrey5')

#Used to determine what mode the application is in
Engineer_Mode = False
Viewer_Mode = False

#SQL Database components   
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

#SQL Database components
def create_table_for_upgrade(Path, Upgrade_name, Cost, Part, Time):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    #Used to create a cursor within the table
    cursor = connection.cursor()

    Table_Name = f"Create table '{Upgrade_name}' (Cost, part, time)"
    cursor.execute(Table_Name)

    Table_Values = f"INSERT INTO '{Upgrade_name}' VALUES('{Cost}','{Part}','{Time}')"
    cursor.execute(Table_Values)
    connection.commit()

#SQL Database components
def create_table_for_tool(Path, Tool_Name, List_of_Upgrades):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    #Used to create a cursor within the table
    cursor = connection.cursor()

    Table_Name = f"Create table '{Tool_Name}' (List_of_Upgrades)"
    cursor.execute(Table_Name)

    Table_Values = f"INSERT INTO  '{Tool_Name}' VALUES('{List_of_Upgrades}')"
    cursor.execute(Table_Values)
    connection.commit()

#Gets the cost of whatever data table that is called for
def get_Cost(Path, Upgrade_name):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    cursor = connection.cursor()
    Cursor_Name = f"SELECT Cost FROM '{Upgrade_name}' tasks"

    #Selects what table to pull the cost data from
    cost_data = cursor.execute(Cursor_Name)
    
    #Gets the data from the database
    cost_data = cursor.fetchall()
    return cost_data    

#Gets the Part of whatever data table that is called for
def get_Part(Path, Upgrade_name):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    cursor = connection.cursor()
    Cursor_Name = f"SELECT Part FROM '{Upgrade_name}' tasks"

    #Selects what table to pull the cost data from
    part_data = cursor.execute(Cursor_Name)

    #Gets the data from the database
    part_data = cursor.fetchall()
    return part_data

#Gets the Time of whatever dat table that is called for
def get_Time(Path, Upgrade_name):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    cursor = connection.cursor()
    Cursor_Name = f"SELECT Time FROM '{Upgrade_name}' tasks"

    #Selects what table to pull the cost data from
    cursor.execute(Cursor_Name)

    #Gets the data from the database
    time_data = cursor.fetchall()
    return time_data

#Gets the Upgrades of whatever Tool's data table that is called for
def get_Upgrades(Path, Tool_Name):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    cursor = connection.cursor()
    Cursor_Name = f"SELECT List_of_Upgrades FROM '{Tool_Name}' tasks"

    #Selects what table to pull the cost data from
    cursor.execute(Cursor_Name)

    #Gets the data from the database
    upgrade_data = cursor.fetchall()
    return upgrade_data

#Update the value store in table for Cost
def update_cost(Path, Upgrade_name, Update_Value_For_Cost):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    cursor = connection.cursor()
    Update_Cost = f"UPDATE '{Upgrade_name}' SET Cost = '{Update_Value_For_Cost}'"
    cursor.execute(Update_Cost)
    connection.commit()

#Update the value store in table for Part
def update_part(Path, Upgrade_name, Update_Value_For_Part):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    cursor = connection.cursor()
    Update_Part = f"UPDATE '{Upgrade_name}' SET part = '{Update_Value_For_Part}'"
    cursor.execute(Update_Part)
    connection.commit()

#Update the value store in table for Part
def update_time(Path, Upgrade_name, Update_Value_For_Time):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)
    cursor = connection.cursor()

    Update_Time = f"UPDATE '{Upgrade_name}' SET Time = '{Update_Value_For_Time}'"
    cursor.execute(Update_Time)
    connection.commit()

#Update the Upgrade data of a tool
def add_upgrade(Path, Tool_Names, Update_Value_For_List):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    #Sets the connection to the database
    cursor = connection.cursor()
    Cursor_Name = f"SELECT List_of_Upgrades FROM '{Tool_Names}' tasks"

    #Selects what table to pull the cost data from
    upgrade_data = cursor.execute(Cursor_Name)
    Update_Value_For_List_of_Upgrades = str(upgrade_data.fetchall())[
                                        3:(len(upgrade_data.fetchall()) - 4)] + ", " + Update_Value_For_List

    Update_Upgrade = f"UPDATE '{Tool_Names}' SET List_of_Upgrades = '{Update_Value_For_List_of_Upgrades}'"
    cursor.execute(Update_Upgrade)
    connection.commit()

#Deletes the Upgrade from database
def delete_upgrade(path, Upgrade_name):
    #Used to create or connect to SQLite Database
    connection = create_connection(path)

    cursor = connection.cursor()
    cursor_name = f"DROP TABLE '{Upgrade_name}'"
    cursor.execute(cursor_name)
    connection.commit()

#Deletes the tool from the database
def delete_tool(path, Tool_name):
    #Used to create or connect to SQLite Database
    connection = create_connection(path)

    cursor = connection.cursor()
    cursor_name = f"DROP TABLE '{Tool_name}'"
    cursor.execute(cursor_name)
    connection.commit()

#Login Layout for GUI
layout_Login = [
    [sg.Text('Please enter your Username and Password')],
    [sg.Text('Username', size=(15, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
    [sg.Text('Password', size=(15, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False, password_char='*')],
    [sg.Submit(), sg.Exit(key = '-EXIT-')]
]

#Opens up the GUI window
window_Login = sg.Window('Login', layout_Login, enable_close_attempted_event = True)

# This is an Event Loop
while True:  
    event, values = window_Login.read()

    #Allows the Application to get into Engineering Mode
    if values[0] == "Engineering" and values[1] == "EM141852":
        Engineer_Mode = True
        break

    #Allows the Application to get into Manager Mode    
    if values[0] == "Viewing" and values[1] == "VM181604":
        Viewer_Mode = True
        break

    #Closes the GUI
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
        break

#Closes the GUI
window_Login.close()

#Opens up the Engineer GUIs
if Engineer_Mode == True:
    #Layout for the Engineer Mode
    layout_Enginer = [
        [sg.Stretch(), sg.Text('Installed Upgrade'), sg.Stretch()],
        [sg.Stretch(), sg.Button('Tool Comparison', size = (20,2)), sg.Stretch(), sg.Button('Add Installed Upgrade',  size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Time Installing', size = (20,2)), sg.Stretch(), sg.Button('Edit Installed Upgrade',  size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Amount Invested', size = (20,2)), sg.Stretch(), sg.Button('Delete Installed Upgrade',  size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Button('View Installed Upgrade', size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Text('Available Upgrades'), sg.Stretch()],
        [sg.Stretch(), sg.Button('Add Available Upgrade',  size = (20,2)), sg.Stretch(), sg.Button('Low Cost Upgrade',  size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Edit Available Upgrade',  size = (20,2)), sg.Stretch(), sg.Button('Low Install Time',  size = (20,2)), sg.Stretch()],        
        [sg.Stretch(), sg.Button('Delete Available Upgrade',  size = (20,2)), sg.Stretch(), sg.Button('Upgrade Comparison',  size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Button('View Available Upgrade',  size = (20,2)), sg.Stretch(), sg.Button('Needed Investment',  size = (20,2)), sg.Stretch()]
    ]
    
    #Opens the Engineer Mode GUI
    window_Engineer = sg.Window('Engineering Mode', layout_Enginer, enable_close_attempted_event = True) 

    # This is an Event Loop
    while True:  
        event, values = window_Engineer.read()

        #Closes the GUI
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
            break

        #Tool comparison Button pushed
        if event in "Tool Comparison":
            #Setup for the Tool Comparison GUI
            layout_Tool_Comparison_Installed_Upgrade = [
                [sg.Text('Tool Name #1', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Text('Tool Name #2', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Tool Comparison Data'), sg.Stretch()],                
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]
            ]

            #Opens the Tool Comparison Installed Upgrade GUI
            window_Tool_Comparison_Installed_Upgrade = sg.Window('Tool Comparison Installed Upgrade', layout_Tool_Comparison_Installed_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Tool_Comparison_Installed_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Tool Comparison
                if event in "Submit":
                    #Gets the first tool data
                    Tool_1 = str(get_Upgrades("Tools", values[0].upper()))
                    Tool_1 = Tool_1[3:len(Tool_1)-4]

                    #Gets the second tool data
                    Tool_2 = str(get_Upgrades("Tools", values[1].upper()))
                    Tool_2 = Tool_2[3:len(Tool_2)-4]
                    
                    #Used to update the text box with Tool comparisons 
                    window_Tool_Comparison_Installed_Upgrade['-MULTILINE KEY-'].print('Tool 1 Installed Upgrade Data', justification = 'center', font=('Arial', 10, 'bold'))
                    window_Tool_Comparison_Installed_Upgrade['-MULTILINE KEY-'].print(f"{Tool_1}", justification = 'center')

                    window_Tool_Comparison_Installed_Upgrade['-MULTILINE KEY-'].print('Tool 2 Installed Upgrade Data', justification = 'center', font=('Arial', 10, 'bold'))
                    window_Tool_Comparison_Installed_Upgrade['-MULTILINE KEY-'].print(f"{Tool_2}", justification = 'center')

            #Closes the GUI
            window_Tool_Comparison_Installed_Upgrade.close()           

        #Add Installed Upgrade Button pushed
        if event in "Add Installed Upgrade":
            #Setup for the Add Installed Upgrade GUI
            layout_Tool_Comparison_Installed_Upgrade = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Text('List of Upgrades', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Confirmation of Data Being Added'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]
            ]

            #Opens the Add Installed Upgrade GUI
            window_Tool_Comparison_Installed_Upgrade = sg.Window('Add Installed Upgrade', layout_Tool_Comparison_Installed_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Tool_Comparison_Installed_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Add Installed Upgrade
                if event in "Submit":
                    #stuff to add the installed upgrade
                    create_table_for_tool("Tools", values[0].upper() , values[1].upper())
                    #Used to update the text box to say it has been completed 
                    window_Tool_Comparison_Installed_Upgrade['-MULTILINE KEY-'].print('New Installed Upgrade has been Added', justification = 'center')

            #Closes the GUI
            window_Tool_Comparison_Installed_Upgrade.close()  

        #Add Available Upgrade Button pushed
        if event in "Add Available Upgrade":
            #Setup for the Add Available Upgrade GUI
            layout_Tool_Add_Available_Upgrade = [
                [sg.Text('Upgrade Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Text('Cost', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Text('Part(s)', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Text('Time', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Confirmation of Data Being Added'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]
            ]

            #Opens the Add Available Upgrade GUI
            window_Tool_Add_Available_Upgrade = sg.Window('Add Available Upgrade', layout_Tool_Add_Available_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Tool_Add_Available_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Add Available Upgrade
                if event in "Submit":
                    #stuff to add the installed upgrade
                    create_table_for_upgrade("Tool Upgrades", values[0].upper(), values[1].upper(), values[2].upper(), values[3].upper())
                    
                    #Used to update the text box to say it has been completed 
                    window_Tool_Add_Available_Upgrade['-MULTILINE KEY-'].print('New Available Upgrade has been Added', justification = 'center')

            #Closes the GUI
            window_Tool_Add_Available_Upgrade.close()            

        #Low Cost Upgrade Button pushed
        if event in "Low Cost Upgrade":
            #Setup for the Low Cost Upgrade GUI
            layout_Low_Cost_Upgrade = [
                [sg.Stretch(), sg.Text('Under $10k', justification = 'center'),sg.Text('                    '), sg.Stretch(), sg.Text('Under $25k', justification = 'center'), sg.Stretch(), sg.Text('                    '), sg.Text('Over $25k', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-Under $10k KEY-', size=(30,10)), sg.Stretch(), sg.Multiline('', key = '-Under $25k KEY-', size=(30,10)), sg.Stretch(), sg.Multiline('', key = '-Over $25k KEY-', size=(30,10))],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
            ]

            #Opens the Low Cost Upgrade GUI
            window_Low_Cost_Upgrade = sg.Window('Low Cost Upgrade', layout_Low_Cost_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Low_Cost_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Low Cost Upgrade
                if event in "Submit":
                    # Used to create or connect to SQLite Database
                    connection = create_connection("Tool Upgrades")

                    cursor = connection.cursor()
                    Cursor_Name = "SELECT name FROM sqlite_master WHERE type='table';"

                    # Selects what table to pull the cost data from
                    Low_Cost_Upgrade = cursor.execute(Cursor_Name)

                    #Gets the data from the database
                    Low_Cost_Upgrade = cursor.fetchall()

                    #To determine how many upgrades are in the database
                    Number_of_Upgrades = len(Low_Cost_Upgrade)

                    #Used to create a list of upgrades 
                    Under_10k = []
                    Between_10k_25k = []
                    Over_25k = []

                    #Used to print list of upgrades
                    Under_10k_str = ""
                    Between_10k_25k_str = ""
                    Over_25k_str = ""

                    #Iterates through upgrades to get their name
                    for i in range(Number_of_Upgrades):
                        upgrade = str(Low_Cost_Upgrade[i])
                        upgrade = upgrade.split("'")

                        #Used to find the Cost of the upgrade
                        Cost_of_Upgrade = str(get_Cost("Tool Upgrades", upgrade[1]))
                        Cost_of_Upgrade = Cost_of_Upgrade[3:len(Cost_of_Upgrade)-4]
                        Cost_of_Upgrade = float(Cost_of_Upgrade)

                        #Puts the upgrade in the Under 10K list
                        if Cost_of_Upgrade < 10000.00:
                            Under_10k.append(upgrade[1])
                            
                        #Puts the upgrade in the between 10k and 25k list
                        if Cost_of_Upgrade > 10000.00 and Cost_of_Upgrade < 25000.00:
                            Between_10k_25k.append(upgrade[1])

                        #Puts the upgrade in the over 25K
                        if Cost_of_Upgrade > 25000.00:
                            Over_25k.append(upgrade[1])

                    #Used to create the list of upgrades to output
                    for i in range(len(Under_10k)):
                        if i == 0:
                            Under_10k_str = Under_10k_str + Under_10k[i]
                        if i != 0:
                            Under_10k_str = Under_10k_str + ", " + Under_10k[i]

                    #Used to create the list of upgrades to output
                    for i in range(len(Between_10k_25k)):
                        if i == 0:
                            Between_10k_25k_str = Between_10k_25k_str + Between_10k_25k[i]
                        if i != 0:
                            Between_10k_25k_str = Between_10k_25k_str + ", " + Between_10k_25k[i]

                    #Used to create the list of upgrades to output
                    for i in range(len(Over_25k)):
                        if i == 0:
                            Over_25k_str = Over_25k_str + Over_25k[i]
                        if i != 0:
                            Over_25k_str = Over_25k_str + ", " + Over_25k[i]
                    
                    #Used to update the text box for under $10k 
                    window_Low_Cost_Upgrade['-Under $10k KEY-'].print(Under_10k_str, justification = 'left')

                    #Used to update the text box for under $25k 
                    window_Low_Cost_Upgrade['-Under $25k KEY-'].print(Between_10k_25k_str, justification = 'left')

                    #Used to update the text box for over $25k 
                    window_Low_Cost_Upgrade['-Over $25k KEY-'].print(Over_25k_str, justification = 'left')

            #Closes the GUI
            window_Low_Cost_Upgrade.close()            

        #Time Installing Button pushed
        if event in "Time Installing":
            #Setup for the Time Installing GUI
            layout_Time_Installing = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (35,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Time Installed Data', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Time Installing GUI
            window_Time_Installing = sg.Window('Time Installing', layout_Time_Installing, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Time_Installing.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Time Install
                if event in "Submit":
                    #Used to get the list of upgrades from tool
                    List_of_Upgrades = str(get_Upgrades("Tools", values[0].upper()))
                    List_of_Upgrades = List_of_Upgrades[3:len(List_of_Upgrades)-4]
                    List_of_Upgrades = List_of_Upgrades.split(", ")

                    #String used to print output
                    Total_Time_Installing = "The total amount of time installing: "
                    Total_Time = 0.00

                    #Used to find the install time of each upgrade
                    for i in range(len(List_of_Upgrades)):
                        #Used to find the Cost of the upgrade
                        Install_Time = str(get_Time("Tool Upgrades", List_of_Upgrades[i]))
                        Install_Time = Install_Time[3:len(Install_Time)-4]
                        Install_Time = float(Install_Time)
                        Total_Time = Total_Time + Install_Time
                        Total_Time = round(Total_Time, 2)

                    #Used to get final text ready to output
                    Total_Time_Installing = Total_Time_Installing + str(Total_Time) + " hours for " + str(values[0].upper())
                    
                    #Used to update the text for Time Installed Data
                    window_Time_Installing['-MULTILINE KEY-'].print(Total_Time_Installing, justification = 'center')

            #Closes the GUI
            window_Time_Installing.close()             

        #Edit Installed Upgrade Button pushed
        if event in "Edit Installed Upgrade":
            #Setup for the Edit Installed Upgrade GUI
            layout_Edit_Installed_Upgrade = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Text('Upgrade Being Added', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Confirmation of Data Being Edited', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Edit Installed Upgrade GUI
            window_Edit_Installed_Upgrade = sg.Window('Edit Installed Upgrade', layout_Edit_Installed_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Edit_Installed_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Edit Installed Upgrade
                if event in "Submit":
                    #stuff to Edit Installed Upgrade
                    add_upgrade("Tools", values[0].upper(), values[1].upper())
                    
                    #Used to update the text box for under $10k 
                    window_Edit_Installed_Upgrade['-MULTILINE KEY-'].print('New Upgrade added to Tool', justification = 'center')

            #Closes the GUI
            window_Edit_Installed_Upgrade.close()            

        #Edit Available Upgrade Button pushed
        if event in "Edit Available Upgrade":
            #Setup for the Edit Available Upgrade GUI
            layout_Edit_Available_Upgrade = [
                [sg.Text('Upgrade Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Checkbox('Cost'), sg.Stretch(), sg.Checkbox('Part'), sg.Stretch(), sg.Checkbox('Time'), sg.Stretch()],
                [sg.Text('New Upgrade Data', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Confirmation of Data Being Edited', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Edit Available Upgrade GUI
            window_Edit_Available_Upgrade = sg.Window('Edit Available Upgrade', layout_Edit_Available_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Edit_Available_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Edit Available Upgrade
                if event in "Submit":                    
                    #If the Cost Checkbox is checked 
                    if values[1] == True:
                        update_cost("Tool Upgrades", values[0].upper(), values[4].upper())

                    #If the Parts Checkbox is checked
                    if values[2] == True:
                        update_part("Tool Upgrades", values[0].upper(), values[4].upper())

                    #If the Times Checkbox is checked
                    if values[3] == True:
                        update_time("Tool Upgrades", values[0].upper(), values[4].upper())
                    
                    #Used to update the text box for the edited Available Upgrade
                    window_Edit_Available_Upgrade['-MULTILINE KEY-'].print('New Upgrade added to Tool', justification = 'center')

            #Closes the GUI
            window_Edit_Available_Upgrade.close()             

        #Low Install Time Button pushed
        if event in "Low Install Time":
            #Setup for the Low Install Upgrade GUI
            layout_Low_Install_Upgrade = [
                [sg.Stretch(), sg.Text('Less Than 8 Hours', justification = 'center'), sg.Text('               '), sg.Stretch(), sg.Text('Less Than 24 Hours', justification = 'center'), sg.Stretch(), sg.Text('               '), sg.Text('Over 24 Hours', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-Less Than 8 Hours KEY-', size=(30,10)), sg.Stretch(), sg.Multiline('', key = '-Less Than 24 Hours KEY-', size=(30,10)), sg.Stretch(), sg.Multiline('', key = '-Over 24 Hours KEY-', size=(30,10))],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
            ]

            #Opens the Low Cost Upgrade GUI
            window_Low_Install_Upgrade = sg.Window('Low Install Time', layout_Low_Install_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Low_Install_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Low Install Time
                if event in "Submit":
                    # Used to create or connect to SQLite Database
                    connection = create_connection("Tool Upgrades")

                    cursor = connection.cursor()
                    Cursor_Name = "SELECT name FROM sqlite_master WHERE type='table';"

                    # Selects what table to pull the cost data from
                    Low_Install_Time = cursor.execute(Cursor_Name)

                    #Gets the data from the database
                    Low_Install_Time = cursor.fetchall()

                    #To determine how many upgrades are in the database
                    Number_of_Upgrades = len(Low_Install_Time)

                    #Used to create a list of upgrades 
                    Under_8hr = []
                    Between_8hr_24hr = []
                    Over_24hr = []

                    #Used to print list of upgrades
                    Under_8hr_str = ""
                    Between_8hr_24hr_str = ""
                    Over_24hr_str = ""

                    #Iterates through upgrades to get their name
                    for i in range(Number_of_Upgrades):
                        upgrade = str(Low_Install_Time[i])
                        upgrade = upgrade.split("'")

                        #Used to find the Cost of the upgrade
                        Time_Installing = str(get_Time("Tool Upgrades", upgrade[1]))
                        Time_Installing = Time_Installing[3:len(Time_Installing)-4]
                        Time_Installing = float(Time_Installing)

                        #Puts the upgrade in the Under 8hr list
                        if Time_Installing < 8.0:
                            Under_8hr.append(upgrade[1])
                            
                        #Puts the upgrade in the between 8hr and 24hr list
                        if Time_Installing > 8.0 and Time_Installing < 24.00:
                            Between_8hr_24hr.append(upgrade[1])

                        #Puts the upgrade in the over 24hr
                        if Time_Installing > 24.00:
                            Over_24hr.append(upgrade[1])

                    #Used to create the list of upgrades to output
                    for i in range(len(Under_8hr)):
                        if i == 0:
                            Under_8hr_str = Under_8hr_str + Under_8hr[i]
                        if i != 0:
                            Under_8hr_str = Under_8hr_str + ", " + Under_8hr[i]

                    #Used to create the list of upgrades to output
                    for i in range(len(Between_8hr_24hr)):
                        if i == 0:
                            Between_8hr_24hr_str = Between_8hr_24hr_str + Between_8hr_24hr[i]
                        if i != 0:
                            Between_8hr_24hr_str = Between_8hr_24hr_str + ", " + Between_8hr_24hr[i]

                    #Used to create the list of upgrades to output
                    for i in range(len(Over_24hr)):
                        if i == 0:
                            Over_24hr_str = Over_24hr_str + Over_24hr[i]
                        if i != 0:
                            Over_24hr_str = Over_24hr_str + ", " + Over_24hr[i] 
                    
                    #Used to update the text box for Less Than 8 Hours
                    window_Low_Install_Upgrade['-Less Than 8 Hours KEY-'].print(Under_8hr_str, justification = 'center')

                    #Used to update the text box for Less Than 24 Hours
                    window_Low_Install_Upgrade['-Less Than 24 Hours KEY-'].print(Between_8hr_24hr_str, justification = 'center')

                    #Used to update the text box for Over 24 Hours 
                    window_Low_Install_Upgrade['-Over 24 Hours KEY-'].print(Over_24hr_str, justification = 'center')

            #Closes the GUI
            window_Low_Install_Upgrade.close()            

        #Amount Invested Button pushed
        if event in "Amount Invested":
            #Setup for the Amount Invested GUI
            layout_Amount_Invested = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Amount Invested Data', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Amount Invested GUI
            window_Edit_Available_Upgrade = sg.Window('Amount Invested', layout_Amount_Invested, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Edit_Available_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Amount Invested
                if event in "Submit":
                    #Used to get the list of upgrades
                    List_of_Upgrades = str(get_Upgrades("Tools", values[0].upper()))
                    List_of_Upgrades = List_of_Upgrades[3:len(List_of_Upgrades)-4]
                    List_of_Upgrades = List_of_Upgrades.split(", ")

                    #String used to print output
                    Total_Amount_Invested_str = "The total amount Invested: "
                    Total_Amount_Invested = 0.00                    

                    #To determine how many upgrades are in the database
                    Number_of_Upgrades = len(List_of_Upgrades)

                    #Used to find the amount invested
                    for i in range(Number_of_Upgrades):
                        #Used to find the total cost of investment
                        Amount_Invested = str(get_Cost("Tool Upgrades", List_of_Upgrades[i]))
                        Amount_Invested = Amount_Invested[3:len(Amount_Invested)-4]
                        Amount_Invested = float(Amount_Invested)
                        Total_Amount_Invested = Total_Amount_Invested + Amount_Invested

                    #Converts the total amount to be displayed as money would
                    locale.setlocale( locale.LC_ALL, 'English_United States.1252' )
                    Total_Amount_Invested = locale.currency( Total_Amount_Invested, grouping = True )

                    #Used to get final text ready to output
                    Total_Amount_Invested_str = Total_Amount_Invested_str + str(Total_Amount_Invested) + " for " + str(values[0].upper())
                    
                    #Used to update the text box for the Amount Invested
                    window_Edit_Available_Upgrade['-MULTILINE KEY-'].print(Total_Amount_Invested_str, justification = 'center')

            #Closes the GUI
            window_Edit_Available_Upgrade.close()            

        #Delete Installed Upgrade pushed
        if event in "Delete Installed Upgrade":
            #Setup for the Delete Installed Upgrade GUI
            layout_Delete_Installed_Upgrade = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Confirmation of Data Being Deleted', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Delete Installed Upgrade GUI
            window_Delete_Installed_Upgrade = sg.Window('Delete Installed Upgrade', layout_Delete_Installed_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Delete_Installed_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Delete Installed Upgrade
                if event in "Submit":
                    #stuff to Delete Installed Upgrade
                    delete_tool("Tools", values[0].upper())
                    
                    #Used to update the text box for the Deleted Installed Upgrade
                    window_Delete_Installed_Upgrade['-MULTILINE KEY-'].print('Installed Upgrade has been Deleted Sucessfully', justification = 'center')

            #Closes the GUI
            window_Delete_Installed_Upgrade.close()

        #Delete Available Upgrade pushed
        if event in "Delete Available Upgrade":
            #Setup for the Delete Available Upgrade GUI
            layout_Delete_Available_Upgrade = [
                [sg.Text('Upgrade Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Confirmation of Data Being Deleted', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Delete Available Upgrade GUI
            window_Delete_Available_Upgrade = sg.Window('Delete Available Upgrade', layout_Delete_Available_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Delete_Available_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Delete Available Upgrade
                if event in "Submit":
                    #stuff to find Delete Available Upgrade
                    delete_upgrade("Tool Upgrades", values[0].upper())
                    
                    #Used to update the text box for the Deleted Available Upgrade
                    window_Delete_Available_Upgrade['-MULTILINE KEY-'].print('Available Upgrade has been Deleted Sucessfully', justification = 'center')

            #Closes the GUI
            window_Delete_Available_Upgrade.close()            

        #Tool Comparison pushed
        if event in "Upgrade Comparison":
            #Setup for the Upgrade Comparison GUI
            layout_Upgrade_Comparison = [
                [sg.Text('Upgrade Name #1', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Text('Upgrade Name #2', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Upgrade Comparison Data'), sg.Stretch()],                
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]
            ]

            #Opens the Tool Comparison Installed Upgrade GUI
            window_Upgrade_Comparison = sg.Window('Upgrade Comparison', layout_Upgrade_Comparison, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Upgrade_Comparison.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Tool Comparison
                if event in "Submit":
                    #Sets the upgarde names 
                    Upgrade_1 = values[0].upper()
                    Upgrade_2 = values[1].upper()

                    #Gets the first upgrade cost data
                    Upgrade_Cost_1 = str(get_Cost("Tool Upgrades", Upgrade_1))

                    #Gets the first upgrade part data
                    Upgrade_Part_1 = str(get_Part("Tool Upgrades", Upgrade_1))

                    #Gets the first upgrade time data
                    Upgrade_Time_1 = str(get_Time("Tool Upgrades", Upgrade_1))

                    #Gets the second upgrade cost data
                    Upgrade_Cost_2 = str(get_Cost("Tool Upgrades", Upgrade_2))

                    #Gets the second upgrade part data
                    Upgrade_Part_2 = str(get_Part("Tool Upgrades", Upgrade_2))

                    #Gets the second upgrade time data
                    Upgrade_Time_2 = str(get_Time("Tool Upgrades", Upgrade_2))

                    #Modifies data to output it
                    Upgrade_Cost_1 = Upgrade_Cost_1[3:len(Upgrade_Cost_1)-4]
                    Upgrade_Part_1 = Upgrade_Part_1[3:len(Upgrade_Part_1)-4]
                    Upgrade_Time_1 = Upgrade_Time_1[3:len(Upgrade_Time_1)-4]

                    Upgrade_Cost_2 = Upgrade_Cost_2[3:len(Upgrade_Cost_2)-4]
                    Upgrade_Part_2 = Upgrade_Part_2[3:len(Upgrade_Part_2)-4]
                    Upgrade_Time_2 = Upgrade_Time_2[3:len(Upgrade_Time_2)-4]
                    
                    #Used to update the text box with upgrades comparisons 
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print('First Available Upgrade', justification = 'left', font=('Arial', 10, 'bold'))
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Upgrade Name: {Upgrade_1}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Cost: {Upgrade_Cost_1}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Part(s): {Upgrade_Part_1}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Time: {Upgrade_Time_1}", justification = 'left')
                    
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print('Second Available Upgrade', justification = 'left', font=('Arial', 10, 'bold'))
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Upgrade Name: {Upgrade_2}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Cost: {Upgrade_Cost_2}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Part(s): {Upgrade_Part_2}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Time: {Upgrade_Time_2}", justification = 'left')

            #Closes the GUI
            window_Upgrade_Comparison.close()             

        #View Installed Upgrade pushed
        if event in "View Installed Upgrade":
            #Setup for the View Installed Upgrade GUI
            layout_View_Installed_Upgrade = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Installed Upgrade Data', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the View Installed Upgrade GUI
            window_View_Installed_Upgrade = sg.Window('View Installed Upgrade', layout_View_Installed_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_View_Installed_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Time Install
                if event in "Submit":
                    Installed_Upgrade_Data = str(get_Upgrades("Tools", values[0].upper()))
                    
                    #Used to update the text for View Installed Upgrade Data
                    window_View_Installed_Upgrade['-MULTILINE KEY-'].print(str(Installed_Upgrade_Data[3:(len(Installed_Upgrade_Data)-4)]), justification = 'center')

            #Closes the GUI
            window_View_Installed_Upgrade.close()            

        #View Available Upgrade pushed
        if event in "View Available Upgrade":
            #Setup for the View Available Upgrade GUI
            layout_View_Available_Upgrade = [
                [sg.Text('Upgrade Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Available Upgrade Data', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the View Available Upgrade GUI
            window_View_Available_Upgrade = sg.Window('View Available Upgrade', layout_View_Available_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_View_Available_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the View Available Upgrade
                if event in "Submit":
                    #Available Upgrade Name
                    upgrade_name = values[0].upper()
                    
                    #Gets the cost data from databse
                    cost = str(get_Cost("Tool Upgrades", upgrade_name))

                    #Gets the part data from databse
                    part = str(get_Part("Tool Upgrades", upgrade_name))

                    #Gets the time data from databse
                    time = str(get_Time("Tool Upgrades", upgrade_name))

                    #Modifies Data to be ready to output
                    cost = cost[3:len(cost)-4]

                    #Modifies Data to be ready to output
                    part = part[3:len(part)-4]

                    #Modifies Data to be ready to output
                    time = time[3:len(time)-4]
                    
                    #Used to update the text for View Available Upgrade Data
                    window_View_Available_Upgrade['-MULTILINE KEY-'].print(f"Upgrade Name: {upgrade_name}", justification = 'left')
                    window_View_Available_Upgrade['-MULTILINE KEY-'].print(f"Cost: {cost}", justification = 'left')
                    window_View_Available_Upgrade['-MULTILINE KEY-'].print(f"Part(s): {part}", justification = 'left')
                    window_View_Available_Upgrade['-MULTILINE KEY-'].print(f"Time: {time}", justification = 'left')

            #Closes the GUI
            window_View_Available_Upgrade.close()           

        #Needed Investment pushed
        if event in "Needed Investment":
            #Setup for the View Available Upgrade GUI
            layout_Needed_Investment = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Needed Investment Data', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Needed Investment GUI
            window_Needed_Investment = sg.Window('Needed Investment', layout_Needed_Investment, enable_close_attempted_event = True) 

            #This is an Event Loop
            while True:  
                event, values = window_Needed_Investment.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Needed Investment
                if event in "Submit":
                    #Used to create or connect to SQLite Database
                    connection = create_connection("Tool Upgrades")

                    cursor = connection.cursor()
                    Cursor_Name = "SELECT name FROM sqlite_master WHERE type='table';"

                    #Selects what table to all the avilable upgrade from database
                    List_of_Available_Upgrades = cursor.execute(Cursor_Name)

                    #Gets the data from the database
                    List_of_Available_Upgrades = cursor.fetchall()

                    #List of all upgrades in the database
                    All_Available_Upgrades = []
                    All_Installed_Upgrades = []
                    Needed_Upgrades = []
                    Needed_Upgrades_str = ""
                    Total_Amount_Needed_Invested = 0.00
                    Total_Amount_Needed_Invested_str = "The total needed investment: "

                    #Used to put the upgrades into a list
                    List_of_Available_Upgrades = str(List_of_Available_Upgrades)
                    List_of_Available_Upgrades = List_of_Available_Upgrades[3:len(List_of_Available_Upgrades)-4]
                    List_of_Available_Upgrades = List_of_Available_Upgrades.split("',), ('")

                    #Used to get a list of all the upgrades inputted into the databse
                    for i in range(len(List_of_Available_Upgrades)):
                        All_Available_Upgrades.append(List_of_Available_Upgrades[i])

                    #Used to get the list of upgrades from tool
                    List_of_Installed_Upgrades = str(get_Upgrades("Tools", values[0].upper()))
                    List_of_Installed_Upgrades = List_of_Installed_Upgrades[3:len(List_of_Installed_Upgrades)-4]
                    List_of_Installed_Upgrades = List_of_Installed_Upgrades.split(", ")

                    #Used to get a list of installed upgrades from database
                    for i in range(len(List_of_Installed_Upgrades)):
                        #Used to find the Cost of the upgrade
                        All_Installed_Upgrades.append(List_of_Installed_Upgrades[i])

                    #Used to find what upgrades are not installed
                    for i in range(len(List_of_Available_Upgrades)):
                        #Pulls the available upgrade out of list
                        Available_Upgrade = List_of_Available_Upgrades[i]

                        #Checks if the value is in the all available list
                        if Available_Upgrade not in All_Installed_Upgrades:
                            Needed_Upgrades.append(Available_Upgrade)

                    #Used to get the String of Needed Upgrades for output
                    for i in range(len(Needed_Upgrades)):
                        #If the first value is being outputted
                        if i == 0:
                            Needed_Upgrades_str = Needed_Upgrades_str + Needed_Upgrades[i]

                        #if the rest of the values are being outputted
                        if i != 0:
                            Needed_Upgrades_str = Needed_Upgrades_str + ", " + Needed_Upgrades[i]

                    #Used to find the amount invested
                    for i in range(len(Needed_Upgrades)):
                        #Used to find the total cost of investment
                        Amount_Needed_Invested = str(get_Cost("Tool Upgrades", Needed_Upgrades[i]))
                        Amount_Needed_Invested = Amount_Needed_Invested[3:len(Amount_Needed_Invested)-4]
                        Amount_Needed_Invested = float(Amount_Needed_Invested)
                        Total_Amount_Needed_Invested = Total_Amount_Needed_Invested + Amount_Needed_Invested

                    #Converts the total amount to be displayed as money would
                    locale.setlocale( locale.LC_ALL, 'English_United States.1252' )
                    Total_Amount_Needed_Invested = locale.currency( Total_Amount_Needed_Invested, grouping = True )

                    #Used to get final text ready to output
                    Total_Amount_Needed_Invested_str = Total_Amount_Needed_Invested_str + str(Total_Amount_Needed_Invested) + " for " + values[0].upper()                        
                    
                    #Used to update the text for Needed Investment Data
                    window_Needed_Investment['-MULTILINE KEY-'].print('Needed Upgrades for ' + values[0].upper(), justification = 'left', font=('Arial', 10, 'bold'))
                    window_Needed_Investment['-MULTILINE KEY-'].print(Needed_Upgrades_str, justification = 'left')
                    window_Needed_Investment['-MULTILINE KEY-'].print('Needed Investement for ' + values[0].upper(), justification = 'left', font=('Arial', 10, 'bold'))
                    window_Needed_Investment['-MULTILINE KEY-'].print(Total_Amount_Needed_Invested_str, justification = 'left')

            #Closes the GUI
            window_Needed_Investment.close()
            
    #Closes the GUI
    window_Engineer.close()

#Opens up the Viewer GUIs
if Viewer_Mode == True:
    #Layout for the Engineer Mode
    layout_Viewer = [
        [sg.Stretch(), sg.Text('Installed Upgrade'), sg.Stretch()],
        [sg.Stretch(), sg.Button('Tool Comparison', size = (20,2)), sg.Stretch(), sg.Button('Add Installed Upgrade',  size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Time Installing', size = (20,2)), sg.Stretch(), sg.Button('Edit Installed Upgrade',  size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Amount Invested', size = (20,2)), sg.Stretch(), sg.Button('Delete Installed Upgrade',  size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Button('View Installed Upgrade', size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Text('Available Upgrades'), sg.Stretch()],
        [sg.Stretch(), sg.Button('Add Available Upgrade',  size = (20,2)), sg.Stretch(), sg.Button('Low Cost Upgrade',  size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Edit Available Upgrade',  size = (20,2)), sg.Stretch(), sg.Button('Low Install Time',  size = (20,2)), sg.Stretch()],        
        [sg.Stretch(), sg.Button('Delete Available Upgrade',  size = (20,2)), sg.Stretch(), sg.Button('Upgrade Comparison',  size = (20,2)), sg.Stretch()],
        [sg.Stretch(), sg.Button('View Available Upgrade',  size = (20,2)), sg.Stretch(), sg.Button('Needed Investment',  size = (20,2)), sg.Stretch()]
        ]
    
    #Opens the Engineer Mode GUI
    window_Viewer = sg.Window('Viewer Mode', layout_Viewer, enable_close_attempted_event = True) 

    # This is an Event Loop
    while True:  
        event, values = window_Viewer.read()

        #Closes the GUI
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
            break
        
        #Tool comparison Button pushed
        if event in "Tool Comparison":
            #Setup for the Tool Comparison GUI
            layout_Tool_Comparison_Installed_Upgrade = [
                [sg.Text('Tool Name #1', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Text('Tool Name #2', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Tool Comparison Data'), sg.Stretch()],                
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]
            ]

            #Opens the Tool Comparison Installed Upgrade GUI
            window_Tool_Comparison_Installed_Upgrade = sg.Window('Tool Comparison Installed Upgrade', layout_Tool_Comparison_Installed_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Tool_Comparison_Installed_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Tool Comparison
                if event in "Submit":
                    #Gets the first tool data
                    Tool_1 = str(get_Upgrades("Tools", values[0].upper()))
                    Tool_1 = Tool_1[3:len(Tool_1)-4]

                    #Gets the second tool data
                    Tool_2 = str(get_Upgrades("Tools", values[1].upper()))
                    Tool_2 = Tool_2[3:len(Tool_2)-4]
                    
                    #Used to update the text box with Tool comparisons 
                    window_Tool_Comparison_Installed_Upgrade['-MULTILINE KEY-'].print('Tool 1 Installed Upgrade Data', justification = 'center', font=('Arial', 10, 'bold'))
                    window_Tool_Comparison_Installed_Upgrade['-MULTILINE KEY-'].print(f"{Tool_1}", justification = 'center')

                    window_Tool_Comparison_Installed_Upgrade['-MULTILINE KEY-'].print('Tool 2 Installed Upgrade Data', justification = 'center', font=('Arial', 10, 'bold'))
                    window_Tool_Comparison_Installed_Upgrade['-MULTILINE KEY-'].print(f"{Tool_2}", justification = 'center')

            #Closes the GUI
            window_Tool_Comparison_Installed_Upgrade.close()            

        #Add Installed Upgrade Button pushed
        if event in "Add Installed Upgrade":
            #Popup window telling users feature is not available
            sg.popup('Feature not available in Viewer Mode', title = "Not Available")
            
        #Add Available Upgrade Button pushed
        if event in "Add Available Upgrade":
            #Popup window telling users feature is not available
            sg.popup('Feature not available in Viewer Mode', title = "Not Available")
            

        #Low Cost Upgrade Button pushed
        if event in "Low Cost Upgrade":
            #Setup for the Low Cost Upgrade GUI
            layout_Low_Cost_Upgrade = [
                [sg.Stretch(), sg.Text('Under $10k', justification = 'center'),sg.Text('                    '), sg.Stretch(), sg.Text('Under $25k', justification = 'center'), sg.Stretch(), sg.Text('                    '), sg.Text('Over $25k', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-Under $10k KEY-', size=(30,10)), sg.Stretch(), sg.Multiline('', key = '-Under $25k KEY-', size=(30,10)), sg.Stretch(), sg.Multiline('', key = '-Over $25k KEY-', size=(30,10))],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
            ]

            #Opens the Low Cost Upgrade GUI
            window_Low_Cost_Upgrade = sg.Window('Low Cost Upgrade', layout_Low_Cost_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Low_Cost_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Low Cost Upgrade
                if event in "Submit":
                    # Used to create or connect to SQLite Database
                    connection = create_connection("Tool Upgrades")

                    cursor = connection.cursor()
                    Cursor_Name = "SELECT name FROM sqlite_master WHERE type='table';"

                    # Selects what table to pull the cost data from
                    Low_Cost_Upgrade = cursor.execute(Cursor_Name)

                    #Gets the data from the database
                    Low_Cost_Upgrade = cursor.fetchall()

                    #To determine how many upgrades are in the database
                    Number_of_Upgrades = len(Low_Cost_Upgrade)

                    #Used to create a list of upgrades 
                    Under_10k = []
                    Between_10k_25k = []
                    Over_25k = []

                    #Used to print list of upgrades
                    Under_10k_str = ""
                    Between_10k_25k_str = ""
                    Over_25k_str = ""

                    #Iterates through upgrades to get their name
                    for i in range(Number_of_Upgrades):
                        upgrade = str(Low_Cost_Upgrade[i])
                        upgrade = upgrade.split("'")

                        #Used to find the Cost of the upgrade
                        Cost_of_Upgrade = str(get_Cost("Tool Upgrades", upgrade[1]))
                        Cost_of_Upgrade = Cost_of_Upgrade[3:len(Cost_of_Upgrade)-4]
                        Cost_of_Upgrade = float(Cost_of_Upgrade)

                        #Puts the upgrade in the Under 10K list
                        if Cost_of_Upgrade < 10000.00:
                            Under_10k.append(upgrade[1])
                            
                        #Puts the upgrade in the between 10k and 25k list
                        if Cost_of_Upgrade > 10000.00 and Cost_of_Upgrade < 25000.00:
                            Between_10k_25k.append(upgrade[1])

                        #Puts the upgrade in the over 25K
                        if Cost_of_Upgrade > 25000.00:
                            Over_25k.append(upgrade[1])

                    #Used to create the list of upgrades to output
                    for i in range(len(Under_10k)):
                        if i == 0:
                            Under_10k_str = Under_10k_str + Under_10k[i]
                        if i != 0:
                            Under_10k_str = Under_10k_str + ", " + Under_10k[i]

                    #Used to create the list of upgrades to output
                    for i in range(len(Between_10k_25k)):
                        if i == 0:
                            Between_10k_25k_str = Between_10k_25k_str + Between_10k_25k[i]
                        if i != 0:
                            Between_10k_25k_str = Between_10k_25k_str + ", " + Between_10k_25k[i]

                    #Used to create the list of upgrades to output
                    for i in range(len(Over_25k)):
                        if i == 0:
                            Over_25k_str = Over_25k_str + Over_25k[i]
                        if i != 0:
                            Over_25k_str = Over_25k_str + ", " + Over_25k[i]
                    
                    #Used to update the text box for under $10k 
                    window_Low_Cost_Upgrade['-Under $10k KEY-'].print(Under_10k_str, justification = 'left')

                    #Used to update the text box for under $25k 
                    window_Low_Cost_Upgrade['-Under $25k KEY-'].print(Between_10k_25k_str, justification = 'left')

                    #Used to update the text box for over $25k 
                    window_Low_Cost_Upgrade['-Over $25k KEY-'].print(Over_25k_str, justification = 'left')

            #Closes the GUI
            window_Low_Cost_Upgrade.close()            

        #Time Installing Button pushed
        if event in "Time Installing":
            #Setup for the Time Installing GUI
            layout_Time_Installing = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (35,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Time Installed Data', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Time Installing GUI
            window_Time_Installing = sg.Window('Time Installing', layout_Time_Installing, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Time_Installing.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Time Install
                if event in "Submit":
                    #Used to get the list of upgrades from tool
                    List_of_Upgrades = str(get_Upgrades("Tools", values[0].upper()))
                    List_of_Upgrades = List_of_Upgrades[3:len(List_of_Upgrades)-4]
                    List_of_Upgrades = List_of_Upgrades.split(", ")

                    #String used to print output
                    Total_Time_Installing = "The total amount of time installing: "
                    Total_Time = 0.00

                    #Used to find the install time of each upgrade
                    for i in range(len(List_of_Upgrades)):
                        #Used to find the Cost of the upgrade
                        Install_Time = str(get_Time("Tool Upgrades", List_of_Upgrades[i]))
                        Install_Time = Install_Time[3:len(Install_Time)-4]
                        Install_Time = float(Install_Time)
                        Total_Time = Total_Time + Install_Time
                        Total_Time = round(Total_Time, 2)

                    #Used to get final text ready to output
                    Total_Time_Installing = Total_Time_Installing + str(Total_Time) + " hours for " + str(values[0].upper())
                    
                    #Used to update the text for Time Installed Data
                    window_Time_Installing['-MULTILINE KEY-'].print(Total_Time_Installing, justification = 'center')

            #Closes the GUI
            window_Time_Installing.close()            

        #Edit Installed Upgrade Button pushed
        if event in "Edit Installed Upgrade":
            #Popup window telling users feature is not available
            sg.popup('Feature not available in Viewer Mode', title = "Not Available")            

        #Edit Available Upgrade Button pushed
        if event in "Edit Available Upgrade":
            #Popup window telling users feature is not available
            sg.popup('Feature not available in Viewer Mode', title = "Not Available")            

        #Low Install Time Button pushed
        if event in "Low Install Time":
            #Setup for the Low Install Upgrade GUI
            layout_Low_Install_Upgrade = [
                [sg.Stretch(), sg.Text('Less Than 8 Hours', justification = 'center'), sg.Text('               '), sg.Stretch(), sg.Text('Less Than 24 Hours', justification = 'center'), sg.Stretch(), sg.Text('               '), sg.Text('Over 24 Hours', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-Less Than 8 Hours KEY-', size=(30,10)), sg.Stretch(), sg.Multiline('', key = '-Less Than 24 Hours KEY-', size=(30,10)), sg.Stretch(), sg.Multiline('', key = '-Over 24 Hours KEY-', size=(30,10))],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
            ]

            #Opens the Low Cost Upgrade GUI
            window_Low_Install_Upgrade = sg.Window('Low Install Time', layout_Low_Install_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Low_Install_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Low Install Time
                if event in "Submit":
                    # Used to create or connect to SQLite Database
                    connection = create_connection("Tool Upgrades")

                    cursor = connection.cursor()
                    Cursor_Name = "SELECT name FROM sqlite_master WHERE type='table';"

                    # Selects what table to pull the cost data from
                    Low_Install_Time = cursor.execute(Cursor_Name)

                    #Gets the data from the database
                    Low_Install_Time = cursor.fetchall()

                    #To determine how many upgrades are in the database
                    Number_of_Upgrades = len(Low_Install_Time)

                    #Used to create a list of upgrades 
                    Under_8hr = []
                    Between_8hr_24hr = []
                    Over_24hr = []

                    #Used to print list of upgrades
                    Under_8hr_str = ""
                    Between_8hr_24hr_str = ""
                    Over_24hr_str = ""

                    #Iterates through upgrades to get their name
                    for i in range(Number_of_Upgrades):
                        upgrade = str(Low_Install_Time[i])
                        upgrade = upgrade.split("'")

                        #Used to find the Cost of the upgrade
                        Time_Installing = str(get_Time("Tool Upgrades", upgrade[1]))
                        Time_Installing = Time_Installing[3:len(Time_Installing)-4]
                        Time_Installing = float(Time_Installing)

                        #Puts the upgrade in the Under 8hr list
                        if Time_Installing < 8.0:
                            Under_8hr.append(upgrade[1])
                            
                        #Puts the upgrade in the between 8hr and 24hr list
                        if Time_Installing > 8.0 and Time_Installing < 24.00:
                            Between_8hr_24hr.append(upgrade[1])

                        #Puts the upgrade in the over 24hr
                        if Time_Installing > 24.00:
                            Over_24hr.append(upgrade[1])

                    #Used to create the list of upgrades to output
                    for i in range(len(Under_8hr)):
                        if i == 0:
                            Under_8hr_str = Under_8hr_str + Under_8hr[i]
                        if i != 0:
                            Under_8hr_str = Under_8hr_str + ", " + Under_8hr[i]

                    #Used to create the list of upgrades to output
                    for i in range(len(Between_8hr_24hr)):
                        if i == 0:
                            Between_8hr_24hr_str = Between_8hr_24hr_str + Between_8hr_24hr[i]
                        if i != 0:
                            Between_8hr_24hr_str = Between_8hr_24hr_str + ", " + Between_8hr_24hr[i]

                    #Used to create the list of upgrades to output
                    for i in range(len(Over_24hr)):
                        if i == 0:
                            Over_24hr_str = Over_24hr_str + Over_24hr[i]
                        if i != 0:
                            Over_24hr_str = Over_24hr_str + ", " + Over_24hr[i] 
                    
                    #Used to update the text box for Less Than 8 Hours
                    window_Low_Install_Upgrade['-Less Than 8 Hours KEY-'].print(Under_8hr_str, justification = 'center')

                    #Used to update the text box for Less Than 24 Hours
                    window_Low_Install_Upgrade['-Less Than 24 Hours KEY-'].print(Between_8hr_24hr_str, justification = 'center')

                    #Used to update the text box for Over 24 Hours 
                    window_Low_Install_Upgrade['-Over 24 Hours KEY-'].print(Over_24hr_str, justification = 'center')

            #Closes the GUI
            window_Low_Install_Upgrade.close()            

        #Amount Invested Button pushed
        if event in "Amount Invested":
            #Setup for the Amount Invested GUI
            layout_Amount_Invested = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Amount Invested Data', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Amount Invested GUI
            window_Edit_Available_Upgrade = sg.Window('Amount Invested', layout_Amount_Invested, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Edit_Available_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Amount Invested
                if event in "Submit":
                    #Used to get the list of upgrades
                    List_of_Upgrades = str(get_Upgrades("Tools", values[0].upper()))
                    List_of_Upgrades = List_of_Upgrades[3:len(List_of_Upgrades)-4]
                    List_of_Upgrades = List_of_Upgrades.split(", ")

                    #String used to print output
                    Total_Amount_Invested_str = "The total amount Invested: "
                    Total_Amount_Invested = 0.00                    

                    #To determine how many upgrades are in the database
                    Number_of_Upgrades = len(List_of_Upgrades)

                    #Used to find the amount invested
                    for i in range(Number_of_Upgrades):
                        #Used to find the total cost of investment
                        Amount_Invested = str(get_Cost("Tool Upgrades", List_of_Upgrades[i]))
                        Amount_Invested = Amount_Invested[3:len(Amount_Invested)-4]
                        Amount_Invested = float(Amount_Invested)
                        Total_Amount_Invested = Total_Amount_Invested + Amount_Invested

                    #Converts the total amount to be displayed as money would
                    locale.setlocale( locale.LC_ALL, 'English_United States.1252' )
                    Total_Amount_Invested = locale.currency( Total_Amount_Invested, grouping = True )

                    #Used to get final text ready to output
                    Total_Amount_Invested_str = Total_Amount_Invested_str + str(Total_Amount_Invested) + " for " + str(values[0].upper())
                    
                    #Used to update the text box for the Amount Invested
                    window_Edit_Available_Upgrade['-MULTILINE KEY-'].print(Total_Amount_Invested_str, justification = 'center')

            #Closes the GUI
            window_Edit_Available_Upgrade.close()            

        #Delete Installed Upgrade pushed
        if event in "Delete Installed Upgrade":
            #Popup window telling users feature is not available
            sg.popup('Feature not available in Viewer Mode', title = "Not Available")            

        #Delete Available Upgrade pushed
        if event in "Delete Available Upgrade":
            #Popup window telling users feature is not available
            sg.popup('Feature not available in Viewer Mode', title = "Not Available")           

        #Tool Comparison pushed
        if event in "Upgrade Comparison":
            #Setup for the Tool Comparison GUI
            layout_Upgrade_Comparison = [
                [sg.Text('Upgrade Name #1', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Text('Upgrade Name #2', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Tool Comparison Data'), sg.Stretch()],                
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]
            ]

            #Opens the Tool Comparison Installed Upgrade GUI
            window_Upgrade_Comparison = sg.Window('Upgrade Comparison', layout_Upgrade_Comparison, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_Upgrade_Comparison.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Tool Comparison
                if event in "Submit":
                    #Sets the upgarde names 
                    Upgrade_1 = values[0].upper()
                    Upgrade_2 = values[1].upper()

                    #Gets the first upgrade cost data
                    Upgrade_Cost_1 = str(get_Cost("Tool Upgrades", Upgrade_1))

                    #Gets the first upgrade part data
                    Upgrade_Part_1 = str(get_Part("Tool Upgrades", Upgrade_1))

                    #Gets the first upgrade time data
                    Upgrade_Time_1 = str(get_Time("Tool Upgrades", Upgrade_1))

                    #Gets the second upgrade cost data
                    Upgrade_Cost_2 = str(get_Cost("Tool Upgrades", Upgrade_2))

                    #Gets the second upgrade part data
                    Upgrade_Part_2 = str(get_Part("Tool Upgrades", Upgrade_2))

                    #Gets the second upgrade time data
                    Upgrade_Time_2 = str(get_Time("Tool Upgrades", Upgrade_2))

                    #Modifies data to output it
                    Upgrade_Cost_1 = Upgrade_Cost_1[3:len(Upgrade_Cost_1)-4]
                    Upgrade_Part_1 = Upgrade_Part_1[3:len(Upgrade_Part_1)-4]
                    Upgrade_Time_1 = Upgrade_Time_1[3:len(Upgrade_Time_1)-4]

                    Upgrade_Cost_2 = Upgrade_Cost_2[3:len(Upgrade_Cost_2)-4]
                    Upgrade_Part_2 = Upgrade_Part_2[3:len(Upgrade_Part_2)-4]
                    Upgrade_Time_2 = Upgrade_Time_2[3:len(Upgrade_Time_2)-4]
                    
                    #Used to update the text box with upgrades comparisons 
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print('First Available Upgrade', justification = 'left', font=('Arial', 10, 'bold'))
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Upgrade Name: {Upgrade_1}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Cost: {Upgrade_Cost_1}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Part(s): {Upgrade_Part_1}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Time: {Upgrade_Time_1}", justification = 'left')
                    
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print('Second Available Upgrade', justification = 'left', font=('Arial', 10, 'bold'))
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Upgrade Name: {Upgrade_2}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Cost: {Upgrade_Cost_2}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Part(s): {Upgrade_Part_2}", justification = 'left')
                    window_Upgrade_Comparison['-MULTILINE KEY-'].print(f"Time: {Upgrade_Time_2}", justification = 'left')

            #Closes the GUI
            window_Upgrade_Comparison.close()            

        #View Installed Upgrade pushed
        if event in "View Installed Upgrade":
            #Setup for the Time Installing GUI
            layout_View_Installed_Upgrade = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Installed Upgrade Data', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Time Installing GUI
            window_View_Installed_Upgrade = sg.Window('View Installed Upgrade', layout_View_Installed_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_View_Installed_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Time Install
                if event in "Submit":
                    Installed_Upgrade_Data = str(get_Upgrades("Tools", values[0].upper()))
                    
                    #Used to update the text for View Installed Upgrade Data
                    window_View_Installed_Upgrade['-MULTILINE KEY-'].print(str(Installed_Upgrade_Data[3:(len(Installed_Upgrade_Data)-4)]), justification = 'center')

            #Closes the GUI
            window_View_Installed_Upgrade.close()            

        #View Available Upgrade pushed
        if event in "View Available Upgrade":
            #Setup for the View Available Upgrade GUI
            layout_View_Available_Upgrade = [
                [sg.Text('Upgrade Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Available Upgrade Data', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the View Available Upgrade GUI
            window_View_Available_Upgrade = sg.Window('View Available Upgrade', layout_View_Available_Upgrade, enable_close_attempted_event = True) 

            # This is an Event Loop
            while True:  
                event, values = window_View_Available_Upgrade.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the View Available Upgrade
                if event in "Submit":
                    #Available Upgrade Name
                    upgrade_name = values[0].upper()
                    
                    #Gets the cost data from databse
                    cost = str(get_Cost("Tool Upgrades", upgrade_name))

                    #Gets the part data from databse
                    part = str(get_Part("Tool Upgrades", upgrade_name))

                    #Gets the time data from databse
                    time = str(get_Time("Tool Upgrades", upgrade_name))

                    #Modifies Data to be ready to output
                    cost = cost[3:len(cost)-4]

                    #Modifies Data to be ready to output
                    part = part[3:len(part)-4]

                    #Modifies Data to be ready to output
                    time = time[3:len(time)-4]
                    
                    #Used to update the text for View Available Upgrade Data
                    window_View_Available_Upgrade['-MULTILINE KEY-'].print(f"Upgrade Name: {upgrade_name}", justification = 'left')
                    window_View_Available_Upgrade['-MULTILINE KEY-'].print(f"Cost: {cost}", justification = 'left')
                    window_View_Available_Upgrade['-MULTILINE KEY-'].print(f"Part(s): {part}", justification = 'left')
                    window_View_Available_Upgrade['-MULTILINE KEY-'].print(f"Time: {time}", justification = 'left')

            #Closes the GUI
            window_View_Available_Upgrade.close()            

        #Needed Investment pushed
        if event in "Needed Investment":
            #Setup for the View Available Upgrade GUI
            layout_Needed_Investment = [
                [sg.Text('Tool Name', size=(17, 1), justification = 'center'), sg.InputText(size = (30,1), do_not_clear=False)],
                [sg.Stretch(), sg.Submit(), sg.Exit(key = '-EXIT-'), sg.Stretch()],
                [sg.Stretch(), sg.Text('Needed Investment Data', justification = 'center'), sg.Stretch()],
                [sg.Stretch(), sg.Multiline('', key = '-MULTILINE KEY-', size=(50,5)), sg.Stretch()]                
            ]

            #Opens the Needed Investment GUI
            window_Needed_Investment = sg.Window('Needed Investment', layout_Needed_Investment, enable_close_attempted_event = True) 

            #This is an Event Loop
            while True:  
                event, values = window_Needed_Investment.read()

                #Closes the GUI
                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '-EXIT-') and sg.popup_yes_no('Do you really want to exit?', no_titlebar = True, background_color = "Grey", text_color = "Black", button_color = ("Black", "Grey")) == 'Yes':
                    break

                #Starts the Needed Investment
                if event in "Submit":
                    #Used to create or connect to SQLite Database
                    connection = create_connection("Tool Upgrades")

                    cursor = connection.cursor()
                    Cursor_Name = "SELECT name FROM sqlite_master WHERE type='table';"

                    #Selects what table to all the avilable upgrade from database
                    List_of_Available_Upgrades = cursor.execute(Cursor_Name)

                    #Gets the data from the database
                    List_of_Available_Upgrades = cursor.fetchall()

                    #List of all upgrades in the database
                    All_Available_Upgrades = []
                    All_Installed_Upgrades = []
                    Needed_Upgrades = []
                    Needed_Upgrades_str = ""
                    Total_Amount_Needed_Invested = 0.00
                    Total_Amount_Needed_Invested_str = "The total needed investment: "

                    #Used to put the upgrades into a list
                    List_of_Available_Upgrades = str(List_of_Available_Upgrades)
                    List_of_Available_Upgrades = List_of_Available_Upgrades[3:len(List_of_Available_Upgrades)-4]
                    List_of_Available_Upgrades = List_of_Available_Upgrades.split("',), ('")

                    #Used to get a list of all the upgrades inputted into the databse
                    for i in range(len(List_of_Available_Upgrades)):
                        All_Available_Upgrades.append(List_of_Available_Upgrades[i])

                    #Used to get the list of upgrades from tool
                    List_of_Installed_Upgrades = str(get_Upgrades("Tools", values[0].upper()))
                    List_of_Installed_Upgrades = List_of_Installed_Upgrades[3:len(List_of_Installed_Upgrades)-4]
                    List_of_Installed_Upgrades = List_of_Installed_Upgrades.split(", ")

                    #Used to get a list of installed upgrades from database
                    for i in range(len(List_of_Installed_Upgrades)):
                        #Used to find the Cost of the upgrade
                        All_Installed_Upgrades.append(List_of_Installed_Upgrades[i])

                    #Used to find what upgrades are not installed
                    for i in range(len(List_of_Available_Upgrades)):
                        #Pulls the available upgrade out of list
                        Available_Upgrade = List_of_Available_Upgrades[i]

                        #Checks if the value is in the all available list
                        if Available_Upgrade not in All_Installed_Upgrades:
                            Needed_Upgrades.append(Available_Upgrade)

                    #Used to get the String of Needed Upgrades for output
                    for i in range(len(Needed_Upgrades)):
                        #If the first value is being outputted
                        if i == 0:
                            Needed_Upgrades_str = Needed_Upgrades_str + Needed_Upgrades[i]

                        #if the rest of the values are being outputted
                        if i != 0:
                            Needed_Upgrades_str = Needed_Upgrades_str + ", " + Needed_Upgrades[i]

                    #Used to find the amount invested
                    for i in range(len(Needed_Upgrades)):
                        #Used to find the total cost of investment
                        Amount_Needed_Invested = str(get_Cost("Tool Upgrades", Needed_Upgrades[i]))
                        Amount_Needed_Invested = Amount_Needed_Invested[3:len(Amount_Needed_Invested)-4]
                        Amount_Needed_Invested = float(Amount_Needed_Invested)
                        Total_Amount_Needed_Invested = Total_Amount_Needed_Invested + Amount_Needed_Invested

                    #Converts the total amount to be displayed as money would
                    locale.setlocale( locale.LC_ALL, 'English_United States.1252' )
                    Total_Amount_Needed_Invested = locale.currency( Total_Amount_Needed_Invested, grouping = True )

                    #Used to get final text ready to output
                    Total_Amount_Needed_Invested_str = Total_Amount_Needed_Invested_str + str(Total_Amount_Needed_Invested) + " for " + values[0].upper()                        
                    
                    #Used to update the text for Needed Investment Data
                    window_Needed_Investment['-MULTILINE KEY-'].print('Needed Upgrades for ' + values[0].upper(), justification = 'left', font=('Arial', 10, 'bold'))
                    window_Needed_Investment['-MULTILINE KEY-'].print(Needed_Upgrades_str, justification = 'left')
                    window_Needed_Investment['-MULTILINE KEY-'].print('Needed Investement for ' + values[0].upper(), justification = 'left', font=('Arial', 10, 'bold'))
                    window_Needed_Investment['-MULTILINE KEY-'].print(Total_Amount_Needed_Invested_str, justification = 'left')

            #Closes the GUI
            window_Needed_Investment.close()

    window_Viewer.close()
