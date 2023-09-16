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

==New Implementation Plan needs to be developed for the changes that I will be making for the second iteration of the application.== 

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

<mark style="background-color: #FFFF00">Waiting to input code snippets until after all the code changes have been made</mark>

## SQL Database Components

``` python

```

The above code snippets are used to allow the connection and creation of the SQL database that the Tool Upgrade Tracking Application use. 

## SQL Database Functions

```python
   
```

The function above allows for the cost of an available upgrade to be pulled from the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python

```

The function above allows for the Part of an available upgrade to be pulled from the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python

```

The function above allows for the Time of an available upgrade to be pulled from the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python

```

The function above allows for the upgrades of an installed upgrade to be pulled from the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python

```

The function above updates the data for cost of the available upgrade in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python

```

The function above updates the data for part of the available upgrade in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python

```

The function above updates the data for time of the available upgrade in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python

```

The function above adds an update to a tool to track the installed upgrades in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

```python

```

The function above deletes an available upgrade in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 


```python

```

The function above delete the list of installed upgrade for a tool in the SQL database, so that this code does not have to be constant written throughout the source code rather the function can be used. 

## GUI Functions

```python

```

The code above is what is used to create the GUI for the user to login to the application, so that the application knows if a viewer or engineer is logging in. 

```python

```

The code above is what is used to create the GUI for the home page of the application, this home page is the same for both the viewer and engineer mode. The different is that in the viewer mode, the users do not have access to certain features that would allow them to add, edit, or delete data from the database. 

```python
#Popup window telling users feature is not available
            sg.popup('Feature not available in Viewer Mode', title = "Not Available") 
```

The code above is the GUI that pops up when a user in the viewer mode tries to add, edit, or delete data from the database.

## Features of the Application

**Tool Comparison Installed Upgrade**

```python

```

The code above is what is used to pull data on two separate tools and output them to the user in a window so that the user can compare what upgrades are installed on the tools. 

**Add Installed Upgrade**

```python

```

The code above is what is used to add new data to the SQL database for what upgrades are installed on a tool. This always proves the user with confirmation that the data was successfully added to the database. 

**Add Available Upgrade**

```python
  
```

The code above is what is used to add new data to the SQL database for what upgrades are available to install on a tool. This always proves the user with confirmation that the data was successfully added to the database. 

**Low Cost Upgrade**

```python

```

The code above is what takes all the available upgrades that are stored in the SQL database, once it has all the upgrades it puts them into groups. These groups are if the upgrade is less than $10,000, between $10,000 and $25,000, and if they are greater than $25,000. Next, the code goes through and outputs these groups to the user to see so that they can choose an upgrade that is based on how much they cost. 

**Time Installing**

```python

```

The code above is what is used to find out how much time has been spent on upgrading a specific tool. Meaning that this code will find all the upgrades that have been installed and cross-reference them with the available upgrades to find out what their install times are and add them all up to get the correct amount of time that has been spent upgrading the tool.

**Edit Installed Upgrade**

```python

```

The code above is what is used to make edits to installed upgrades on tools that are already stored within the SQL database. This allows for engineers to add record of an upgrade being installed onto a tool that is already being tracked. 

**Edit Available Upgrade**

```python

```

The code above is what is used to make edits to available upgrades that can be installed on tools and that are already stored within the SQL database. This allows for engineers to modify either the cost, part(s), or time of the available upgrade. 

**Low Install Time**

```python

```

The code above is what takes all the available upgrades that are stored in the SQL database, once it has all the upgrades it puts them into groups. These groups are if the upgrade takes less than 8 hours to install, between 8 and 24 hours, and it takes longer than 24 hours to install. Next, the code goes through and outputs these groups to the user to see so that they can choose an upgrade that is based on how long it will take to install. 

**Amount Invested**

```python

```

The code above is what is used to find out what upgrades have been installed onto a tool. Then, take that list of upgrades and find how much money has been spent on purchasing those upgrades by using the available upgrade data to determine the cost of each upgrade installed on the tool. 

**Delete Installed Upgrade**

```python

```

The code above is what is used to delete all the data that was stored in the SQL database for a specific tool and what upgrades the tool had installed on it. This is done by using the SQL database function of delete_tool().

**Delete Available Upgrade**

```python

```

The code above is what is used to delete all the data that was stored in the SQL database for a specific available upgrade. This is done by using the SQL database function of delete_upgrade().

**Upgrade Comparison**

```python

```

The code above is what is used to pull data on two separate available upgrades and output them to the user in a window so that the user can compare the two available upgrades against each other.

**View Installed Upgrade**

```python

```

The code above is what is used to pull all the data on a specific tool to view all the different upgrades that have been installed on the tool. This is done by using the SQL database function of get_Upgrades().

**View Available Upgrade**

```python

```

The code above is what is used to pull all the data on a specific available upgrade to view the cost, part(s), and time of the upgrade. This is done by using the SQL database function of get_Cost(), get_Part(), and get_Time().

**Needed Investment**

```python

```

The code above is what is used to find out what upgrades have not been installed onto a tool yet. Then, the code takes that list of upgrades and finds how much money will need to be spent on purchasing those upgrades by using the available upgrade data to determine the cost of each upgrade that hasn’t been installed on the tool yet. 

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
| 7 | Repeat test step 5 for the viewing mode. | Read the test steps in step 5 to redo this test for the viewing mode. | N/A | Successfully sorted the Upgrades | Pass |

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

**Module:** GUI Button for Tool Comparison Installed Upgrades

**Test Objective:** To verify that the tool comparison method of the application is correctly pulling the Installed Upgrade data for both of the tools and displaying it for the user.

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the engineering mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Add an Installed Upgrades. | Once Logged in, click on the Add Installed Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Installed Upgrade. | Tool Name: CFM T1 List of Upgrades: Power Valve, Computer, Software Update | Successful Adding of Data Message | Pass |
| 3 | Add an Installed Upgrades. | Once Logged in, click on the Add Installed Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Installed Upgrade. | Tool Name: CFM T3 List of Upgrades: UPS, Injection Rack, Rapitran | Successful Adding of Data Message | Pass |
| 4 | Choose the name of the tool you want to compare. | Once the Installed Upgrades are added to the application, you will navigate to the home page and click the Tool Comparison Installed Upgrades button. This will open another window where you will enter in the two names of the tools you want to compare. | Tool Name #1: CFM T1 Tool Name #2: CFM T2 | Successful pulling of Tools Installed Upgrade Data | Pass |
| 5 | Verify that the data that was pulled for both of the Installed Upgrades is correct. | After the submit button is clicked, the text box in the window will be updated with the Installed Upgrade data. Verify that the data is correct for each of the tools. | N/A | Successful Comparison of the Installed Upgrades | Pass |

<p align="center">Table 8: Test Case for Tool Upgrade Tracking Application

**Test Case Name:** TC-7

**Module:** GUI Button for Tool Comparison Available Upgrades

**Test Objective:** To verify that the upgrade comparison method of the application is correctly pulling the Available Upgrade data for both of the upgrades and displaying it for the user.

| Step  | Test Name | Test Steps | Test Data | Results | Pass/Fail |
| :---: | :-------: | :--------: | :-------: | :-----: | :-------: |
| 1 | Log in to Engineering Mode. | Enter the username and password of the engineering mode. | Username: Engineering Password: EM141852 | Successful Login | Pass |
| 2 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Power Valve Cost: 8,000 Parts: Card, Airline, Screws Time: 7 | Successful Adding of Data Message | Pass |
| 3 | Add an Available Upgrades. | Once Logged in, click on the Add Available Upgrade button. This will bring up another GUI that will allow you to enter in the information for an Available Upgrade. | Upgrade Name: Computer Cost: 18,000 Parts: Monitor, Cables Time: 12 | Successful Adding of Data Message | Pass |
| 4 | Choose the name of the upgrades you want to compare. | Once the Available Upgrades are added to the application, you will naviagate to the home page and click the Upgrade Comparison button. This will open another window where you will enter in the two names of the upgrades you want to compare. | Upgrade Name #1: Power Valve Upgrade Name #2: Computer | Successful pulling of Available Upgrade Data | Pass |
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
| 7 | Verifiy that the Needed Investment methods of the application are working correctly. | Once all the upgrades are added and the tool is added, naviagate back to the home page and click on the needed investment button. Another window will pop when the button is clicked, here you will input the Tool Name. Hit submit, this will update the text box within the window with the needed upgrades and the cost of all the upgrades. Verify this information so that the needed upgardes is Power Valve and the total  investment about is $8,000. | Tool Name: CFM T2 | Successful output of needed upgrades and investment | Pass |

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
