<p align="center">Tool Upgrade Tracking Business Application

<p align="center">Bryce Ryan Vegh

<p align="center">Master of Science in Software Development Capstone Development Iteration 2

<p align="center">Grand Canyon University

<p align="center">Professor Robert Estey

<p align="center">Revision: A

<p align="center">October 25, 2023

# Abstract

The Tool Upgrade Tracking Business Application is being designed to give Equipment Engineers the ability to track upgrades on semiconductor tools that they are responsible for upgrading and maintaining, which the tools they work on build the different layers of microchips. This application will give the engineers a tool they can use to track what upgrades are available to install on their tools and give them the ability to track the upgrades that they already installed on the tools. The idea of this application came from looking at how inexperienced and experienced Equipment Engineers work to track the available and installed upgrades on the tools they are responsible for. From observing these engineers, it showed that the less experienced Equipment Engineers struggled to track this information and that they could not find a method that worked for them. The main point that was taken from watching the engineers was that the inexperienced engineers struggled due to not having the years of experience of working on the tools they are responsible for. Meaning that creating an application like this will help to bring the inexperienced engineers up to speed, allow them to understand what is going on with their tools better, and to understand what resources they have available to them. 

The application design will include the use of a Structured Query Language (SQL) database for storing the available upgrade and installed upgrade data. Next, the application design will include a Graphical User Interface (GUI) that will allow the user to interact with the data and will be designed to be user-friendly. The design of the GUI will include features that allow the user to initiate tasks that allow the user to add, remove, search, and view the data that is stored in the SQL database. 

The accomplishment of this application is to create a user-friendly application that helps Equipment Engineers on tracking this data. This will be achieved by designing a GUI that is easy to use and navigate while also providing the engineers with training on how to use the features of the application. 

# Implementation Plan - Second Iteration

| ID    | Task  | Estimate Hours | Actual Hours | Percent Complete |
| :---: | :---: | :------------: | :----------: | :--------------: |
| 1 | Change how the user input is received by the application, make it to where all user input comes in as all capitalized.  | 8 | 6 | 100% |
| 2 | Test that the input change did not affect any of the different features of the application by running the test plans/cases.  | 16 | 20 | 100% |
| 3 | Change the homepage GUI to have the buttons and title blocks be vertically aligned instead of horizontally aligned.  | 2 | 2 | 100% |
| 4 | Test the homepage to verify that the change to the homepage GUI did not affect any functionality of the application. | 4 | 3.5 | 100% |
| 5 | Research and change the login GUI to have the ability to hide the user's password when they are entering it into the application. | 4 | 3 | 100% |
| 6 | Test to verify that the change to the login GUI is functioning correctly.  | 1 | 0.5 | 100% |
| 7 | Change the Time Installing feature to allow for only two decimal places to be shown when outputting the time installed data to the user. | 3 | 2.5 | 100% |
| 8 | Test the added functionality to the Time Installing feature to verify the feature is functioning correctly. | 2.5 | 2 | 100% |
| 9 | Research and change how the Amount Invested feature outputs dollar amounts to the user to view.  | 6 | 7.5 | 100% |
| 10 | Test the functionality of the Amount Invested feature with the new output conversion method.  | 2.5 | 2 | 100% |
| 11 | Research and change how the Needed Investment feature outputs dollar amounts to the user to view.  | 4 | 3 | 100% |
| 12 | Test the functionality of the Amount Invested feature with the new output conversion method.  | 2 | 1.5 | 100% |

<p align="center">Table 1: Implementation Plan for First Iteration

# Mapping of Functional Requirements 

| User Story | Technical Design | Code Module | Test Case |
| :--------: | :--------------: | :---------: | :-------: |
| US-1: Track Available Upgrades | Project Proposal: Section Tool Upgrade Tracking Application High-Level Solution | GUI Buttons for Add, Edit, and Delete of Available Upgrades | TC-1 |
| US-2: Tracking of the Installed Upgrades | Project Proposal: Section Tool Upgrade Tracking Application High-Level Solution | GUI Buttons for Add, Edit, and Delete of Installed Upgrades | TC-2 |
| US-3:Ability to Interact with Database | Project Proposal: Section Tool Upgrade Tracking Application High-Level Solution | SQL Database Functions | TC-3 |
| US-4: Low Cost Upgrade | Project Requirement Specification: Section Functional Requirements | GUI Button for Low Cost Upgrade | TC-4 |
| US-5: Low Install Time | Project Requirement Specification: Section Functional Requirements | GUI Button for Low Install Time | TC-5 |
| US-6: Tool Comparison for Installed Upgrades | Project Requirement Specification: Section Functional Requirements | GUI Button for Tool Comparison Installed Upgrades | TC-6 |
| US-7: Tool Comparison for Available Upgrades | Project Requirement Specification: Section Functional Requirements | GUI Button for Tool Comparison Available Upgrades | TC-7 |
| US-8: Amount to Invest in the Tool | Project Requirement Specification: Section Functional Requirements | GUI Button for Needed Investment | TC-8 |
| US-9: Time Spent Installing | Project Requirement Specification: Section Functional Requirements | GUI Button for Time Installing | TC-9 |
| US-10: Investment | Project Requirement Specification: Section Functional Requirements | GUI Button for Amount Invested | TC-10 |

<p align="center">Table 2: Traceability Matrix

# Source Code Listing

## Import Statement and Variable definitions

```python
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
```

## SQL Database Components

``` python
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
```

The above code snippets are used to allow the connection and creation of the SQL database that the Tool Upgrade Tracking Application use. 

## SQL Database Functions

```python
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
```

The function above allows for the cost of an available upgrade to be pulled from the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python
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
```

The function above allows for the Part of an available upgrade to be pulled from the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python
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
```

The function above allows for the Time of an available upgrade to be pulled from the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python
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
```

The function above allows for the upgrades of an installed upgrade to be pulled from the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python
#Update the value store in table for Cost
def update_cost(Path, Upgrade_name, Update_Value_For_Cost):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    cursor = connection.cursor()
    Update_Cost = f"UPDATE '{Upgrade_name}' SET Cost = '{Update_Value_For_Cost}'"
    cursor.execute(Update_Cost)
    connection.commit()
```

The function above updates the data for cost of the available upgrade in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python
#Update the value store in table for Part
def update_part(Path, Upgrade_name, Update_Value_For_Part):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)

    cursor = connection.cursor()
    Update_Part = f"UPDATE '{Upgrade_name}' SET part = '{Update_Value_For_Part}'"
    cursor.execute(Update_Part)
    connection.commit()
```

The function above updates the data for part of the available upgrade in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python
#Update the value store in table for Part
def update_time(Path, Upgrade_name, Update_Value_For_Time):
    #Used to create or connect to SQLite Database
    connection = create_connection(Path)
    cursor = connection.cursor()

    Update_Time = f"UPDATE '{Upgrade_name}' SET Time = '{Update_Value_For_Time}'"
    cursor.execute(Update_Time)
    connection.commit()
```

The function above updates the data for time of the available upgrade in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python
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
```

The function above adds an update to a tool to track the installed upgrades in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python
#Deletes the Upgrade from database
def delete_upgrade(path, Upgrade_name):
    #Used to create or connect to SQLite Database
    connection = create_connection(path)

    cursor = connection.cursor()
    cursor_name = f"DROP TABLE '{Upgrade_name}'"
    cursor.execute(cursor_name)
    connection.commit()
```

The function above deletes an available upgrade in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 


```python
#Deletes the tool from the database
def delete_tool(path, Tool_name):
    #Used to create or connect to SQLite Database
    connection = create_connection(path)

    cursor = connection.cursor()
    cursor_name = f"DROP TABLE '{Tool_name}'"
    cursor.execute(cursor_name)
    connection.commit()
```

The function above delete the list of installed upgrade for a tool in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

## GUI Functions

```python
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
```

The code above is what is used to create the GUI for the user to login to the application, so that the application knows if a viewer or engineer is logging in. The changes that were made to this portion of the code from the first iteration was the adding of the password_char = '*'. This was changed because it allows the password to be hidden when it is typed in, so it adds another layer of protection for the user's password. 

```python
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
        
        #Add Installed Upgrade Button pushed
        if event in "Add Installed Upgrade":
        
        #Add Available Upgrade Button pushed
        if event in "Add Available Upgrade":
        
        #Low Cost Upgrade Button pushed
        if event in "Low Cost Upgrade":
        
        #Time Installing Button pushed
        if event in "Time Installing":
        
        #Edit Installed Upgrade Button pushed
        if event in "Edit Installed Upgrade":
        
        #Edit Available Upgrade Button pushed
        if event in "Edit Available Upgrade":
        
        #Low Install Time Button pushed
        if event in "Low Install Time":        
        
        #Amount Invested Button pushed
        if event in "Amount Invested":
        
        #Delete Installed Upgrade pushed
        if event in "Delete Installed Upgrade":
        
        #Delete Available Upgrade pushed
        if event in "Delete Available Upgrade":
        
        #Tool Comparison pushed
        if event in "Tool Comparison Available Upgrade":
        
        #View Installed Upgrade pushed
        if event in "View Installed Upgrade":
        
        #View Available Upgrade pushed
        if event in "View Available Upgrade":
        
        #Needed Investment pushed
        if event in "Needed Investment":
    
    #Closes the GUI
    window_Engineer.close()
```

The code above is what is used to create the GUI for the home page of the application, this home page is the same for both the viewer and engineer mode. The different is that in the viewer mode, the users do not have access to certain features that would allow them to add, edit, or delete data from the database. I changed the layout of the home GUI screen to be vertically aligned with all the buttons instead of horizontally aligned due to the vertically aligned looking visually better. I also went through the previous Capstone Milestones and updated the home GUI wireframes to reflect this, but the iteration 1 code will still have the Home GUI horizontally aligned as I want to have record of this change. 

```python
#Popup window telling users feature is not available
            sg.popup('Feature not available in Viewer Mode', title = "Not Available") 
```

The code above is the GUI that pops up when a user in the viewer mode tries to add, edit, or delete data from the database.

## Features of the Application

**Tool Comparison**

```python
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
```

The code above is what is used to pull data on two separate tools and output them to the user in a window so that the user can compare what upgrades are installed on the tools. 

**Add Installed Upgrade**

```python
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
```

The code above is what is used to add new data to the SQL database for what upgrades are installed on a tool. This always proves the user with confirmation that the data was successfully added to the database. 

**Add Available Upgrade**

```python
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
```

The code above is what is used to add new data to the SQL database for what upgrades are available to install on a tool. This always proves the user with confirmation that the data was successfully added to the database. 

**Low Cost Upgrade**

```python
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
```

The code above is what takes all the available upgrades that are stored in the SQL database, once it has all the upgrades it puts them into groups. These groups are if the upgrade is less than $10,000, between $10,000 and $25,000, and if they are greater than $25,000. Next, the code goes through and outputs these groups to the user to see so that they can choose an upgrade that is based on how much they cost. Changed up how the GUI window layout is defined from the first iteration of the software. Removed the spaces that were added behind the under $10k and Over $25k title blocks to make the GUI window layout code line look a bit neater. Added two separate sg.Text() functions with the needed spacing to align the title blocks in their correct position instead of just having the spaces after the title block names in their respective sg.Text() function. 

**Time Installing**

```python
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
```

The code above is what is used to find out how much time has been spent on upgrading a specific tool. Meaning that this code will find all the upgrades that have been installed and cross-reference them with the available upgrades to find out what their install times are and add them all up to get the correct amount of time that has been spent upgrading the tool. The changes that were made to this portion of the code were the adding of the rounding function when finding the total time spent installing upgrades on the tool. This rounding function will allow for the output to be more visually appealing to the user and be in a format that the user is more use to. This was a small change, but it makes the application more user friendly due to the output of this portion being what the user is used to. 

**Edit Installed Upgrade**

```python
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
```

The code above is what is used to make edits to installed upgrades on tools that are already stored within the SQL database. This allows for engineers to add record of an upgrade being installed onto a tool that is already being tracked. 

**Edit Available Upgrade**

```python
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
```

The code above is what is used to make edits to available upgrades that can be installed on tools and that are already stored within the SQL database. This allows for engineers to modify either the cost, part(s), or time of the available upgrade. 

**Low Install Time**

```python
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
```

The code above is what takes all the available upgrades that are stored in the SQL database, once it has all the upgrades it puts them into groups. These groups are if the upgrade takes less than 8 hours to install, between 8 and 24 hours, and it takes longer than 24 hours to install. Next, the code goes through and outputs these groups to the user to see so that they can choose an upgrade that is based on how long it will take to install. Changed up how the GUI window layout is defined from the first iteration of the software. Removed the spaces that were added behind the Less Than 8 Hours and Over 24 Hours title blocks to make the GUI window layout code line look a bit neater. Added two separate sg.Text() functions with the needed spacing to align the title blocks in their correct position instead of just having the spaces after the title block names in their respective sg.Text() function. 

**Amount Invested**

```python
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
```

The code above is what is used to find out what upgrades have been installed onto a tool. Then, take that list of upgrades and find how much money has been spent on purchasing those upgrades by using the available upgrade data to determine the cost of each upgrade installed on the tool. The changes that were made were to add a way to make the amount of money spent upgrading the tool to be display how money should be displayed. This was done by importing the locale library and setting the locale currency to dollars. Then, passing the total amount invested into the locale.currency function to allow the function to covert the output to be viewed how dollars should be. 

**Delete Installed Upgrade**

```python
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
```

The code above is what is used to delete all the data that was stored in the SQL database for a specific tool and what upgrades the tool had installed on it. This is done by using the SQL database function of delete_tool().

**Delete Available Upgrade**

```python
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
```

The code above is what is used to delete all the data that was stored in the SQL database for a specific available upgrade. This is done by using the SQL database function of delete_upgrade().

**Upgrade Comparison**

```python
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
```

The code above is what is used to pull data on two separate available upgrades and output them to the user in a window so that the user can compare the two available upgrades against each other.

**View Installed Upgrade**

```python
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
```

The code above is what is used to pull all the data on a specific tool to view all the different upgrades that have been installed on the tool. This is done by using the SQL database function of get_Upgrades().

**View Available Upgrade**

```python
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
```

The code above is what is used to pull all the data on a specific available upgrade to view the cost, part(s), and time of the upgrade. This is done by using the SQL database function of get_Cost(), get_Part(), and get_Time().

**Needed Investment**

```python
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
```

The code above is what is used to find out what upgrades have not been installed onto a tool yet. Then, the code takes that list of upgrades and finds how much money will need to be spent on purchasing those upgrades by using the available upgrade data to determine the cost of each upgrade that hasn’t been installed on the tool yet. The changes that were made were to add a way to make the amount of money needed to upgrade the tool to be display how money should be displayed. This was done by importing the locale library and setting the locale currency to dollars. Then, passing the total amount needed into the locale.currency function to allow the function to covert the output to be viewed how dollars should be.

## Global Changes to the Code

Made changes across all of the GUIs so that any time a user inputs data into the application it automatically makes the data fully capitalized. This change was implemented so that it would prevent errors or bugs from users inputting data differently from each other. An example would be if one user inputted CFM T1 for a tool, then a different user tries to view what the list of upgrades are installed on this tool, but they input cfm t1. With this, the first iteration would error and crash, but with this change it corrects this so that it doesn't matter what the user inputs they can find the information they are looking for. 

# Test Plan and Cases
**Test Case Name:** TC-1

**Module:** GUI Buttons for Add, Edit, and Delete of Available Upgrades

**Test Objective:** To verify the functionality of adding, editing, and deleting Available Upgrades data from the SQL database.

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the Engineering Mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Test the add functionality of the Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Power Valve Cost: 8,000 Parts: Card, Airline, Screws Time: 7 | Successful Adding of Data Message | Pass |
| 3 | View data in database to verify add data was completed. | Open the SQL database using the DB Browser for SQLite, and verify that the Available Upgrade was added into the database. | N/A | Successfully found Data | Pass |
| 4 | Still being logged into Engineering mode, test the edit functionality of the Available Upgrades | Being at the homepage with all the buttons you will click on the Edit Available Upgrades buttons. This will bring up a GUI and you will enter the upgrade name, what data of the upgrade to edit, and enter the new data value for the upgrade edit. To test this functionality you will need to repeat this step three times, once for cost, once for parts, and once for time. | Upgrade Name: Power Valve Cost: 10,000 Parts: Face Plate Time: 4 | Three Successfully Edited Data Messages | Pass |
| 5 | View data in database to verify the data was edited correctly. | Open the SQL database using the DB Browser for SQLite, and verify that the Available Upgrade was edited in the database. | N/A | Successfully found Data | Pass |
| 6 | Still being logged into Engineering mode, view data by using the view button. | Being at the homepage with all the buttons you will click on the View Available Upgrades button. This will bring up a GUI and you will enter the name of the Available Upgrade. Once you hit submit, you will see text generate in the box below. | Upgrade Name: Power Valve | Successfully Viewed Data | Pass |
| 7 | Still being logged into Engineering mode, Delete data by using the delete button. | Being at the homepage with all the buttons you will click on the Delete Available Upgrades button. This will bring up a GUI and you will enter the name of the Available Upgrade. Once you hit submit, you will get a message saying the data was been deleted. | Upgrade Name:  Power Valve | Successfully Deleted Data | Pass |
| 8 | View data in database to verify the data was deleted correctly. | Open the SQL database using the DB Browser for SQLite, and verify that the Available Upgrade was deleted in the database. | N/A | Successfully found Data | Pass |
| 9 | Exit out of the application so that you can log in to Viewing Mode. | Enter the username and password of the Viewing Mode. | Username: Viewing Password: VM181604| Successful Login | Pass |
| 10 | Check the Add, Edit, and Delete Buttons for Viewing Mode. | Click on each of the buttons to verify they bring up a popup GUI that says this feature is not available. | N/A | Successful popup GUI | Pass |

<p align="center">Table 3: Test Case for Tool Upgrade Tracking Application

**Test Case Name:** TC-2

**Module:** GUI Buttons for Add, Edit, and Delete of Installed Upgrades

**Test Objective:** To verify the functionality of adding, editing, and deleting Installed Upgrades data from the SQL database.

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the Engineering Mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Test the add functionality of the Installed Upgrades. | Once Logged in, click on the Add Installed Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Installed Upgrade. | Tool Name: CFM T1 List of Upgrades: Power Valve, Computer, Software Update | Successful Adding of Data Message | Pass |
| 3 | View data in database to verify add data was completed. | Open the SQL database using the DB Browser for SQLite, and verify that the Installed Upgrade was added into the database. | N/A | Successfully found Data | Pass |
| 4 | Still being logged into Engineering mode, test the edit functionality of the Installed Upgrades | Being at the homepage with all the buttons you will click on the Edit Installed Upgrades buttons. This will bring up a GUI and you will enter the tool name and what upgrade is being added to the tool. Once you hit submit, the text box at the bottom will give you a message saying it is complete. | Tool Name: CFM T1 Upgrade Being Added: Rapitran | Successfully Edited Data Messages | Pass |
| 5 | View data in database to verify the data was edited correctly. | Open the SQL database using the DB Browser for SQLite, and verify that the Installed Upgrade was edited in the database. | N/A | Successfully found Data | Pass |
| 6 | Still being logged into Engineering mode, view data by using the view button. | Being at the homepage with all the buttons you will click on the View Installed Upgrades button. This will bring up a GUI and you will enter the name of the tool. Once you hit submit, you will see text generate in the box below. | Tool Name: CFM T1 | Successfully Viewed Data | Pass |
| 7 | Still being logged into Engineering mode, Delete data by using the delete button. | Being at the homepage with all the buttons you will click on the Delete Installed Upgrades button. This will bring up a GUI and you will enter the name of the tool to delete. Once you hit submit, you will get a message saying the data was been deleted. | Upgrade Name:  Power Valve | Successfully Deleted Data | Pass |
| 8 | View data in database to verify the data was deleted correctly. | Open the SQL database using the DB Browser for SQLite, and verify that the Installed Upgrade was deleted in the database. | N/A | Successfully found Data | Pass |
| 9 | Exit out of the application so that you can log in to Viewing Mode. | Enter the username and password of the Viewing Mode. | Username: Viewing Password: VM181604 | Successful Login | Pass |
| 10 | Check the Add, Edit, and Delete Buttons for Viewing Mode. | Click on each of the buttons to verify they bring up a popup GUI that says this feature is not available. | N/A | Successful popup GUI | Pass |

<p align="center">Table 4: Test Case for Tool Upgrade Tracking Application

**Test Case Name:** TC-3

**Module:** SQL Database Functions

**Test Objective:** To verify the functionality of the SQL functions that were developed to support the Upgrade Tracking Application. 

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Test the function for creating SQL tables. | Call the function to create SQL databases for both Available Upgrades and Installed Upgrades in Python script. | Upgrade Name: Power Valve Cost: 8,000 Parts: Card, Airline, Screws Time: 7 Tool Name: CFM T1 List of Upgrades: Power Valve, Computer, Software Update | Successfully Creating the SQL Database Files | Pass |
| 2 | Test the function for getting the Cost of an available Upgrade. | Call the function to get the cost data from the SQL database and verify the data with what was entered in the database. | Upgrade Name: Power Valve | Successfully get the Cost Data | Pass |
| 3 | Test the function for getting the Part of an available Upgrade. | Call the function to get the part data from the SQL database and verify the data with what was entered in the database. | Upgrade Name: Power Valve | Successfully get the Part Data | Pass |
| 4 | Test the function for getting the Time of an available Upgrade. | Call the function to get the time data from the SQL database and verify the data with what was entered in the database. | Upgrade Name: Power Valve | Successfully get the Time Data | Pass |
| 5 | Test the function for getting the Upgrades of an Installed Upgrade. | Call the function to get the installed upgrade data from the SQL database and verify the data with what was entered in the database. | Tool Name: CFM T1 | Successfully get  Installed Upgrade Data | Pass |
| 6 | Test the function for Updating the Cost of an Available Upgrade. | Call the function to update the cost data and input the data from the test data column. Verify that the cost was updated by using the DB Browser Application. | Upgrade Name: Power Valve Cost: 10,000 | Successfully Updated Data | Pass |
| 7 | Test the function for Updating the Parts of an Available Upgrade. | Call the function to update the part data and input the data from the test data column. Verify that the part was updated by using the DB Browser Application. | Upgrade Name: Power Valve Parts: Face Plate | Successfully Updated Data | Pass |
| 8 | Test the function for Updating the Time of an Available Upgrade. | Call the function to update the time data and input the data from the test data column. Verify that the time was updated by using the DB Browser Application. | Upgrade Name: Power Valve  Time: 4 | Successfully Updated Data | Pass |
| 9 | Test the function for adding an upgrades to the list of Installed Upgrade. | Call the function to update the installed upgrades data and input the data from the test data column. Verify that the installed upgrade was updated by using the DB Browser Application. | Tool Name: CFM T1               List of Upgrades: Rapitran | Successfully Updated Data | Pass |
| 10 | Test the function for deleting of an Available Upgrade. | Call the function to delete the Available Upgrade from the data base. Verify that the upgrade was deleted by using the DB Browser Application. | Upgrade Name: Power Valve | Successfully Deleted Data | Pass |
| 11 | Test the function for deleting of an Installed Upgrade. | Call the function to delete the Installed Upgrade from the data base. Verify that the upgrade was deleted by using the DB Browser Application. | Tool Name: CFM T1 | Successfully Deleted Data | Pass |

<p align="center">Table 5: Test Case for Tool Upgrade Tracking Application

**Test Case Name:** TC-4

**Module:** GUI Button for Low Cost Upgrade

**Test Objective:** To verify that the application feature of finding a low cost upgrade for the Available upgrades is working correctly. 

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the engineering mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Add an Available Upgrade that is less than $10,000. | Use the Add Available Upgrade button, add the upgrade. | Upgrade Name: Power Valve Cost: 10,000 Parts: Face Plate Time: 4 | Successfully added the upgrade | Pass |
| 3 | Add an Available Upgrade that is between $10,000 and $25,000. | Use the Add Available Upgrade button, add the upgrade. | Upgrade Name: Computer Cost: 18,000 Parts: Monitor, Cables Time: 12 | Successfully added the upgrade | Pass |
| 4 | Add an Available Upgrade that is over $25,000. | Use the Add Available Upgrade button, add the upgrade. | Upgrade Name: Rapitran Cost: 75,000 Parts: Rapitran, Mounting Plate Time: 48 | Successfully added the upgrade | Pass |
| 5 | Test the functionality of the Low Cost Upgrade. | From the homepage, click on the Low Cost Upgrade button. This will open up GUI and all that will need to be done is hit the submit button. Hitting the submit will cause the three text boxes to be updated. Verify that the Power Valve upgrade is in the left most box, the computer upgrade is in the middle box, and the Raptiran is in the right most box. | N/A | Successfully sorted the Upgrades | Pass |
| 6 | Log out by exiting the application, and log back in in the viewing mode. | Enter the username and password of the viewing mode. | Username: Viewing Password: VM181604 | Successful Login | Pass |
| 7 | Repeat test step 5 for the viewing mode. | Read the test steps in step 5 to re-do this test for the viewing mode. | N/A | Successfully sorted the Upgrades | Pass |

<p align="center">Table 6: Test Case for Tool Upgrade Tracking Application

**Test Case Name:** TC-5

**Module:** GUI Button for Low Install Time

**Test Objective:** To verify that the method of sorting the Available Upgrades by their install time is working correctly.

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the engineering mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Power Valve Cost: 8,000 Parts: Card, Airline, Screws Time: 7 | Successful Adding of Data Message | Pass |
| 3 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Computer Cost: 18,000 Parts: Monitor, Cables Time: 12 | Successful Adding of Data Message | Pass |
| 4 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Rapitran Cost: 75,000 Parts: Rapitran, Mounting Plate Time: 48 | Successful Adding of Data Message | Pass |
| 5 | Verify that the Available Upgrades are sorted correctly by their time. | Once the three upgrades are added to the application. You will click the Low Install Time button. Then, when the next window opens you will click submit. This will allow the sorting of the upgrades to be done, verify that all the upgrades are in the correct group. | N/A | Successfully grouped the Upgrades | Pass |

<p align="center">Table 7: Test Case for Tool Upgrade Tracking Application

**Test Case Name:** TC-6

**Module:** GUI Button for Tool Comparison

**Test Objective:** To verify that the tool comparison method of the application is correctly pulling the Installed Upgrade data for both of the tools and displaying it for the user.

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the engineering mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Add an Installed Upgrades. | Once Logged in, click on the Add Installed Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Installed Upgrade. | Tool Name: CFM T1 List of Upgrades: Power Valve, Computer, Software Update | Successful Adding of Data Message | Pass |
| 3 | Add an Installed Upgrades. | Once Logged in, click on the Add Installed Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Installed Upgrade. | Tool Name: CFM T3 List of Upgrades: UPS, Injection Rack, Rapitran | Successful Adding of Data Message | Pass |
| 4 | Choose the name of the tool you want to compare. | Once the Installed Upgrades are added to the application, you will navigate to the home page and click the Tool Comparison button. This will open another window where you will enter in the two names of the tools you want to compare. | Tool Name #1: CFM T1 Tool Name #2: CFM T2 | Successful pulling of Tools Installed Upgrade Data | Pass |
| 5 | Verify that the data that was pulled for both of the Installed Upgrades is correct. | After the submit button is clicked, the text box in the window will be updated with the Installed Upgrade data. Verify that the data is correct for each of the tools. | N/A | Successful Comparison of the Installed Upgrades | Pass |

<p align="center">Table 8: Test Case for Tool Upgrade Tracking Application

**Test Case Name:** TC-7

**Module:** GUI Button for Upgrade Comparison

**Test Objective:** To verify that the upgrade comparison method of the application is correctly pulling the Available Upgrade data for both of the upgrades and displaying it for the user.

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the engineering mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Power Valve Cost: 8,000 Parts: Card, Airline, Screws Time: 7 | Successful Adding of Data Message | Pass |
| 3 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Computer Cost: 18,000 Parts: Monitor, Cables Time: 12 | Successful Adding of Data Message | Pass |
| 4 | Choose the name of the upgrades you want to compare. | Once the Available Upgrades are added to the application, you will navigate to the home page and click the Upgrade Comparison button. This will open another window where you will enter in the two names of the upgrades you want to compare. | Upgrade Name #1: Power Valve Upgrade Name #2: Computer | Successful pulling of Available Upgrade Data | Pass |
| 5 | Verify that the data that was pulled for both of the Available Upgrades is correct. | After the submit button is clicked, the text box in the window will be updated with the Available Upgrade data. Verify that the data is correct for each of the upgrades. | N/A | Successful Comparison of the Available Upgrades | Pass |

<p align="center">Table 9: Test Case for Tool Upgrade Tracking Application

**Test Case Name:** TC-8

**Module:** GUI Button for Needed Investment

**Test Objective:** To verify that the needed investment method of the application is correctly pulling the upgrades that the tool needs and correctly finding the cost of these needed upgrades.

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the engineering mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: UPS Cost: 8,500 Parts: Rack, Batteries Time: 4 | Successful Adding of Data Message | Pass |
| 3 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Injection Rack Cost: 20,000 Parts: Rack, Airline Time: 16 | Successful Adding of Data Message | Pass |
| 4 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Rapitran Cost: 75,000 Parts: Rapitran, Mounting Plate Time: 48 | Successful Adding of Data Message | Pass |
| 5 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Power Valve Cost: 8,000 Parts: Card, Airline, Screws Time: 7 | Successful Adding of Data Message | Pass |
| 6 | Add an Installed Upgrades. | Once Logged in, click on the Add Installed Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Installed Upgrade. | Tool Name: CFM T2 List of Upgrades: UPS, Injection Rack, Rapitran | Successful Adding of Data Message | Pass |
| 7 | Verify that the Needed Investment methods of the application are working correctly. | Once all the upgrades are added and the tool is added, navigate back to the home page and click on the needed investment button. Another window will pop when the button is clicked, here you will input the Tool Name. Hit submit, this will update the text box within the window with the needed upgrades and the cost of all the upgrades. Verify this information so that the needed upgrade is Power Valve and the total  investment about is $8,000. | Tool Name: CFM T2 | Successful output of needed upgrades and investment | Pass |

<p align="center">Table 10: Test Case for Tool Upgrade Tracking Application

**Test Case Name:** TC-9

**Module:** GUI Button for Time Installing

**Test Objective:** To verify that the time installing method of the application is correctly pulling the hours spent installing upgrades onto the specific tool entered by the user.

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the engineering mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: UPS Cost: 8,500 Parts: Rack, Batteries Time: 4 | Successful Adding of Data Message | Pass |
| 3 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Injection Rack Cost: 20,000 Parts: Rack, Airline Time: 16 | Successful Adding of Data Message | Pass |
| 4 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Rapitran Cost: 75,000 Parts: Rapitran, Mounting Plate Time: 48 | Successful Adding of Data Message | Pass |
| 5 | Add an Installed Upgrades. | Once Logged in, click on the Add Installed Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Installed Upgrade. | Tool Name: CFM T2 List of Upgrades: UPS, Injection Rack, Rapitran | Successful Adding of Data Message | Pass |
| 6 | Verify the method of finding the time spent installing upgrades on the tool. | Once the upgrages and tool has been added to the application. Navigate to the home page and click on the button Time Installing. Then, enter the tool name and hit submit. This will update the text box within the window with the amount of hours that have been spent installing upgrades. Verify that the hours being display in the text box are 68 hours in total. | Tool Name: CFM T2 | Successful on finding the time spent installing upgrades | Pass |

<p align="center">Table 11: Test Case for Tool Upgrade Tracking Application

**Test Case Name:** TC-10

**Module:** GUI Button for Amount Invested

**Test Objective:** To verify that the amount invested method of the application is correctly pulling the upgrades that the tool has and correctly finding the cost of these upgrades.

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the engineering mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: UPS Cost: 8,500 Parts: Rack, Batteries Time: 4 | Successful Adding of Data Message | Pass |
| 3 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Injection Rack Cost: 20,000 Parts: Rack, Airline Time: 16 | Successful Adding of Data Message | Pass |
| 4 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Rapitran Cost: 75,000 Parts: Rapitran, Mounting Plate Time: 48 | Successful Adding of Data Message | Pass |
| 5 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Power Valve Cost: 8,000 Parts: Card, Airline, Screws Time: 7 | Successful Adding of Data Message | Pass |
| 6 | Add an Installed Upgrades. | Once Logged in, click on the Add Installed Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Installed Upgrade. | Tool Name: CFM T2 List of Upgrades: UPS, Injection Rack, Rapitran | Successful Adding of Data Message | Pass |
| 7 | Verify that the Needed Investment methods of the application are working correctly. | Once all the upgrades are added and the tool is added, navigate back to the home page and click on the amount invested button. Another window will pop when the button is clicked, here you will input the Tool Name. Hit submit, this will update the text box within the window with the amount of money that has been invested into the tool. Verify this information so that the total invested is $103,500. | Tool Name: CFM T2 | Successful output of the amount invested | Pass |

<p align="center">Table 12: Test Case for Tool Upgrade Tracking Application

# Application Demo Screencast
[Application Demo Screencast](https://youtu.be/Mp7tbNfrDNQ)
