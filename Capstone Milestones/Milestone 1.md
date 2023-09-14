<p align="center">Tool Upgrade Tracking Business Application

<p align="center">Bryce Ryan Vegh

<p align="center">Master of Science in Software Development Capstone Project Proposal

<p align="center">Grand Canyon University

<p align="center">Professor Jeremy Wright

<p align="center">Revision: B

<p align="center">January 11,2023

# Abstract
The Tool Upgrade Tracking Business Application is an application that is being designed to give Equipment Engineers the ability to track upgrades on the semiconductor tools that they work on that are used to build the different layers of a microchip. This application will give the ability for the engineers to track what upgrades are available to install on their tools while also giving them the ability to track the upgrades that have already been installed on their tools. The idea of creating this application came from studying how younger and older (more experienced) Equipment Engineers work to track the different upgrades of the tools they work on. From the study it showed that the younger less experienced Equipment Engineers struggled to track the different upgrades that they installed or have available to them to install on their different tools. But the studied showed the main cause of this issue was that the younger engineers just did not have the years under their belt of working on their tools and knowing the tools like the back of their hand. So, creating an application like this has the possibility to bring the younger engineers up to speed by allowing them to get a better feel for their tools and have a resource they can go to when needed. 

The application will need to have a Structured Query Language (SQL) database created so that all the different upgrade data can be stored. Next, the application will need to have a Graphical User Interface (GUI) designed and the GUI needs to be easy to use so that it is not difficult for engineers to input and view data. This task will include designing different features within the GUI to allow the engineers to add, remove, search, and view the upgrade data that is stored in either of the databases. 

The main accomplishments of this project will be creating a user-friendly application, which entices engineers to want to use the application. This can be done by designing a robust and transparent GUI that comes naturally for the engineers to use with little needed training on how the application works. While also creating the SQL databases to perform all of their complex task in the background of the application where the user will not have to see or initiate these tasks for the application to function correctly. 

# Project Overview & Objectives
## Backgroud 
The project of designing this application is being undertaken because there was room to improve how Equipment Engineers function at semiconductor factories. It was noticed a few of the newer engineers were struggling to keep track of the different tools that they were performing upgrades on, which was due to these engineers being solely responsible for over ten different tools each. With this number of tools, it is understandable how trying to track all the upgrades for over ten different tools can get out of hand quite quickly. This issue led to having conversations with other Equipment Engineers to see how they were handling keeping track of the different upgrades they had installed and are available to install on their tools. From these discussions, it realized all the engineers were doing various ways that were being tried by the younger engineers already. The various different ways of solving these issues that were tried were keeping excel files with the various upgrade information and even trying to keep a notebook where the engineers would track this information. The young engineers found that it was always hard and time intensive to track and find this information even with trying these different methods. Plus, only this information was available to the young engineers due to the information being stored on either their personal computer or notebook. Also, it was found that the other Equipment Engineers used these same methods and were struggling to keep up on the information, or they had just given up all together on trying to track this information. 

## State the Problem
The project problem is that there is not an efficient way for Equipment Engineers to store their tool upgrade data that allows the information to be found easily or accessible within minutes. 

## Objectives
- Create SQL database that can store and retrieve data for the GUI when a user is asking for the information to be inputted or retrieved. 

- Create a functioning GUI that allows the user a way to add and see the data that the SQL database is either inputting or retrieving. 

- Designing the application to be robust with an 85% uptime when running. (Uptime meaning that the application is fully functional and not having issues or some bug within the application.)

- Have a simple design of the GUI, meaning there is minimal number of features (buttons, tab selection, etc.) within the different portions of the GUI. 

- Create levels of control to the application so that different users have different accesses to what they can do within the application. (An example would be having one level that only allows data to be viewed.)

## Challenges
- Designing buttons that can be clicked by the user that trigger functions for the SQL databases to input or retrieve data for the correct databases.

- Figuring out a way to have the data stored in the different SQL databases shown to the user in some window within the GUI.

- Having a learning curve to designing a GUI for the project due to having no experience in developing a GUI ever before. 

## Benefits & Opportunities

### Benefits 
The greatest benefit of the project is that it is providing a useful resource to Equipment Engineers that will allow them to better track available upgrades and what upgrades have been installed on their tools. The application will allow the engineers to pull any information about either what upgrades are installed or what upgrades are available to install within minutes now. Plus, it will allow the engineers to provide upper management with information as to what they have done on their tools so that they can better understand why certain tools may run better than others. While also allowing upper management to better understand how to budget money for the different upgrades and which ones they will want to purchase first. 

### Opportunities
The opportunity that this application gives is that it allows for younger engineers to better understand what upgrades have been installed on their tool, while also giving them the ability to get familiar with what upgrades are available to install on their tools. This is due to how when implementing the application, the engineers will have to perform audits on their tools to determine what upgrades have been installed. With the engineers doing these audits, it will allow them to learn more information on their tools and to get more comfortable with what is going on with their tools. 

## Project Scope
The project is to design a business application that Equipment Engineers will use to track available upgrades and what upgrades have been installed on their tools. With the information for the available upgrades to include what parts are needed for the upgrade, how much the upgrade will cost, and how much time it will take to install the upgrade. In addition, the installed upgrade information will just be a list of all the different upgrades that a specific tool has installed on it. Lastly, below are a few examples of in scope and out of scope features of the business application. 

In Scope Features:
- Allow for different levels of user’s privileges where upper management is only able to view the information and the engineers can make edits and delete information. 

- Create a tab selection button that allows the user to choose which data they want to look at, meaning one tab selection for installed upgrades and a second tab selection for available upgrades. 

- Can make changes to data that is stored in the databases due to possible changes in the information about the upgrade. 
 
Out of Scope Features:
- Having the application track the amount of downtime that the tools are experiencing, and whether the downtime is for preventative maintenance or due to failures on the tool.

- Make the application be able to storage manuals for each of the tool, so that all of this information is all in one place as well. 

- Design the application to accept qualification data from the tool’s qualifications so that trends can be made, and tool efficiency can be determined. 

| Stakeholder Name | Role | Responsiblities |
| :----------------: | :------: | :----: |
| Bryce Vegh | Lead Designer | To draft and finalize all documents pertaining to the project. While also designing all the code for the project |

# Work Breakdown Structure Table Goes Here 

| Stakeholder Name | Role | Responsiblities |
| :----------------: | :------: | :----: |
| Bryce Vegh | Lead Designer | To draft and finalize all documents pertaining to the project. While also designing all the code for the project |

<p align="center">Table 1:Stakeholder Information

## Project Success Measures

# Project Completion Criterian Table Goes Here 

| ID    | Task  | Dependencies | Status | Effort Hours | Start Datae | Planned Completion | Estimate to Complete | Actual Completion |
| :---: | :---: | :----------: |:-----: | :----------: | :---------: |:-----------------: | :------------------: | :---------------: | 
| 1     | Create the first portion of the functions and methods used to pull data from SQL Database. |     N/A      |  N.C.  |      12      |   5/5/2023  |      5/8/2023      |       1.5 Days       |         -         |
| 2     | Tests the first portion of the functions and methods used to pull data from SQL Database for initial bugs. |     1        |  N.C.  |      4       |   5/8/2023  |      5/8/2023      |       0.5 Days       |         -         |
| 3     | Create the second portion of the functions and methods used to pull data from SQL Database. |     2        |  N.C.  |      12      |   5/9/2023  |      5/10/2023     |       1.5 Days       |         -         |
| 4     |Tests the second portion of the functions and methods used to pull data from SQL Database for initial bugs.|     3        |  N.C.  |      4       |   5/10/2023 |      5/10/2023     |       0.5 Days       |         -         |
| 5     | Create Simple GUI with basic uses and permission levels to get a feel for designing GUIs. |     4        |  N.C.  |      80      |   5/11/2023 |      5/23/2023     |       10 Days        |         -         |
| 6     | Test GUI that was designed for functionality. |     5        |  N.C.  |      24      |   5/24/2023 |      5/26/2023     |       3 Days         |         -         |
| 7     | Add features to GUI for adding, removing, and editing data with the different SQL Databases. |     6        |  N.C.  |      64      |   5/29/2023 |      6/7/2023      |       8 Days         |         -         |
| 8     |Test the new features added to the GUI for correct functionality. |     7        |  N.C.  |      24      |   6/8/2023  |      6/12/2023     |       3 Days         |         -         |
| 9     | Add feature to the GUI so that the user can see the data in a window for the different databases. |     8        |  N.C.  |      64      |   6/13/2023 |      6/22/2023     |       8 Days         |         -         |
| 10    |Test the new feature added to the GUI for correct functionality. |     9        |  N.C.  |      24      |   6/23/2023 |      6/27/2023     |       3 Days         |         -         |
| 11    | Final look through the code and functionality of application. |     10       |  N.C.  |      80      |   6/28/2023 |      7/11/2023     |       10 Days        |         -         |

# Assumptions and Contraints Table Goes Here 

| Stakeholder Name | Role | Responsiblities |
| :----------------: | :------: | :----: |
| Bryce Vegh | Lead Designer | To draft and finalize all documents pertaining to the project. While also designing all the code for the project |

## Tool Upgrade Tracking Applicaiton High-Level Solution

### Introduction 

The challenge that is being addressed is how Equipment Engineers track the different upgrades that are available to install or have been installed on the tools they are responsible for. With having discussions with various Equipment Engineers, it was found that there was not a single way to track this information in an efficient way whatsoever. The various engineers also discussed that they tried to keep track of this information either in their head, in notebooks at their desk, or in excel files on their work computers. The commonality that was found from these discussions with the engineers was that all of them said that the listed ways were inefficient and took too much time to find the information. In addition, the engineers said they would like to see a more efficient and reliable way to track this information developed. Leading to the need to develop this application so that these Equipment Engineers have an efficient way to track this information and reference it at a moment’s notice. 

### Known Information

The information that is known is that the Equipment Engineers are using one of the following methods for tracking tool upgrade information, which are to remember them off the top of their head, writing them down in notebooks at their desk, or tracking the information in excel files on their work computers. It is also known that there are multiple engineers that would like to see a better way of tracking this information created because their current methods are inefficient and take too much time to reference. In addition, it is known that the information will need to be tracked with two different categories which are what available upgrades there are to install on the tools and what upgrades have already been installed on the tools. In these categories there is different information that will need to be kept track in an efficient and reliable way. For example, with the available upgrades category the needed information that will be tracked are the name of the upgrade, the cost of the upgrade, the needed parts for the upgrade, and how long it will take to install the upgrade. While the installed upgrade category will only need to keep track of the tool name and the running list of upgrades that have been installed on the tool so far. With this, this is all the known information for the project and next examples of the data that will be inputted into the application will be provided.

### Example of Data Inputted into the Application

**Available Upgrade Data**

This data will be inputted into the portion of the SQL database that is used to track the available upgrades. The user will need to supply the application with a name of the upgrade, how much it costs, the needed parts for the upgrade, and how long it will take to install the upgrade. The Upgrade name will be used to allow the user to easily sort the different upgrades within the SQL database and allow the user to search for the upgrade. An example of the data that will be inputted into the application is provided below. 

**Upgrade Name:** Power Valve Card

**Cost:** $13,200

**Part/Parts:** 6 x Power Valve Cards

**Time:** 4 Hours

**Upgrade on Tool**

This data will be inputted into the second portion of the SQL database that is used to track which upgrades have been installed on the different tools that the Equipment Engineers is responsible for. The user will supply the application with a tool name and the list of all the upgrades that they have installed on the tool so far. The tool name will be used to sort all of this data in the SQL database so that the user can easily put in the tool’s name and find all the upgrades that have been installed on it. An example of how this data will be inputted into the application is provided below. 

**Tool Name:** CFM T1A

**List of Upgrades:** Power Valve Card, UPS, IPA Sniffers

### Objective of the Application

The objective of this project is to develop an application that allows Equipment Engineers to track upgrade information more efficiently and reliably for the tools they are responsible for. In addition, the objective is to develop an application that is user-friendly that allows all Equipment Engineers to learn the application quickly. The last part of the objective is to provide Microchip’s upper management a resource that allows them to better prioritize how they approve capital for the various upgrades that are available on the tools in the fab. 

### Solution

The solution that will be designed for the problem stated earlier is going to be a business application that uses an SQL databases and a GUI that the user can interact with. Each of these components of the application will be broken down in the following paragraphs of the proposal. 
The first portion of the SQL database will be used to take in and store the data that relates to the upgrades that are available to install on the different tools that the Equipment Engineers is responsible for. This portion of the SQL database will store the following data for the available upgrades, which are the name of the upgrade, how much the upgrade costs, the part or parts that are needed for the upgrade, and how much time it will take to install the upgrade. The application will use the name of the upgrade to sort and filter the data within the SQL Database. The SQL database will have functions built in that the GUI will use to search and retrieve the cost, parts, and time data values that are stored in the SQL database. In addition, the SQL database will have functions that will allow the GUI to use to update these data values as well. Lastly, the SQL database will have a function built in that the GUI will use to completely delete a user selected available upgrade that is stored in the database. A class diagram for the first SQL database is provided below for reference. 

# Figure 1 Goes Here

The second portion of the SQL database will be used to take in and store the data that relates to what upgrades have been installed on each of the different tools that the Equipment Engineers is responsible for. The data that will be stored in this portion of the SQL database will be the name of the tool and a running list of the upgrades that have been installed on the tool already, with the tool name being used to sort and filter the data within the SQL database. The SQL database will have a function built in that will allow the GUI to search and retrieve specific installed upgrade data from a tool name within the database. In addition, The SQL database will have a function built in that the GUI will use that allows for the running list of upgrades to be updated and a new upgrade added to the list. Lastly, the SQL database will have a function that the GUI will use to delete a user selected tool name completely from the SQL database. A Class diagram for the second SQL databases is provided below for reference. 

# Figure 2 Goes Here

The GUI or Graphical User Interface will be the main component of the application that the user will interact with directly. Meaning that this is where the user will have the ability to input new data, edit data, or delete data from the SQL database talked about above. The main function of this component is to allow the user to view and change the data that is stored the SQL database, which means that the GUI will have a connection to the SQL database. With this, the GUI will have five buttons designed for the user to click which will allow them to interact with the SQL database, one button that will be designed to close the application, and one button designed to restart the application. The five buttons will be designed to allow the application to select which portion of the database the user wants to view, search and output data to the user, view data from either portions of the database in a popup window, edit data in either portion of the database that the user wants, and for the user to delete data from either portions of the database. Each of the five buttons will have a functions tied to them that will allow the task to be executed when the button is clicked by the user. With this, a class diagram has been provided below for the Graphical User Interface for reference. 

# Figure 3 Goes Here

### Architecture Diagram of the Application

**Component #1 Available Upgrade Portion**

In the figure below, component #1 is the first portion of the SQL database that is used to store the available upgrade data for the tools that the Equipment Engineer is responsible for. The function of this component is to store the data on the upgrades that are available to install on the tools. This component does this by having built in functions that allow the database to add new data to the database and edit the existing data within the database so that all the information is up to date all the time. These functions are the main functions that this component uses, but there is also a partial function built into this component. This partial function is used in conjunction with component #3, which is the Graphical User Interface, which allows for data in this component to be searched for and outputted for the user to view. 

**Component #1 Installed Upgrades Portion**

In the figure below, component #1 is the second portion of the SQL database that is used to store the data for the upgrades that are installed on the tools that the Equipment Engineer is responsible for. The function of this component is to store the data on the upgrades that have been installed on the tools. This component also does this by having built in functions that allow the database to add new data to the database and edit the existing data within the database so that all the information is up to date. These functions are also the main functions that this component uses, but there is also a partial function built into this component. This partial function is used in conjunction with component #3, which is the Graphical User Interface, which allows for data in this component to be search for and outputted for the user to view. 

**Component #2**

In the figure below, component #2 is the Graphical User Interface. The function of this component is  to allow the user to interact with the internal SQL databases. Meaning that the GUI allows the user to select different buttons on the GUI that will execute different commands for adding, editing, deleting, or viewing the data within the SQL databases. In addition, the GUI’s function is to take the data that is stored within the SQL database and display the data to the user in a way that allows the user to easily understand and reference the data. 

**Component #3**

In the figure below, component #3 is the Python IDE Shell/ Compiler. The function of this component is to compile the code to verify that there are no errors within the code of the application. Plus, it allows the code to be executed which allows for the application to start up and run in the way it was designed to. 

**Component #4**

In the figure below, component #4 is windows computer. The function of this component is to give the application all the needed storage and hardware to allow the application to be run so that the Equipment Engineers can use the application. 

# Figure 4 Goes Here

### Inputs to the Application

The data that will be inputted into the system will be what available upgrades there are for the tools that the Equipment Engineer is responsible for. This data will include the name of the upgrade, how much the upgrade costs to purchase, the needed parts of the upgrade, and how long the upgrade will take to install. With this the key or important data that is included is the name of the upgrade because this portion of the inputted data will be used to sort and find grouped data within the SQL database. In addition to this there will be data inputted to the application for the installed upgrades on the tools that the Equipment Engineer is responsible for. This data will include the name of the tool that the upgrade or upgrades were installed on and the running list of upgrades that were installed on the tool. With the name of the tool being the key or important data of the grouped data because the tool name will be used to sort and find the data within the SQL database.

### Outputs to the Application

The output of the application will be which data the user is trying to view that is stored in either portion of the SQL database. When the user requests to view specific data that is stored in either portion of the databases the application will go to the desired portion, find the data by sorting through the database. Once the application finds the data within the database, the application will pull the data from the database and modify the data to be visual appealing and understandable for the user to view. Finally, the application will display the data in a window within the GUI for the user to view and reference the data. The only other outputs that the user will see is an output that tells the user that the data has been successfully added, edited, or deleted from either of the SQL database.

### Key Code Snippets 

In the figure below, it provides a code snippet of how the SQL databases initial connection is created when the application first creates the databases. Plus, this snippet of code is also used every time when the user adds, edits, views, or deletes data from either of the database. This portion of code is important and key to the application working because without it the application would not have the ability to access or interact with the SQL databases. 

# Figure 5 Goes Here 

In figure 6 it shows the code snippet for how the SQL database is created for storing the available upgrades to install on the tools. This portion of code is important and key to the application because it allows for the SQL database to be created allowing the user to store all the data on available upgrades for their tools. In addition, without this snippet of code the application would not be able to meet the objective of storing this data in an efficient and easily reference able manner. 

# Figure 6 Goes Here

The figure below is a code snippet showing how the portion of the SQL database is created for storing the data for what upgrades have been installed on the tools already. This code snippet is important and key to the application because it allows for the other half of the data of the application to be stored in an efficient and reliable way for the user to reference at a moment’s notice. In addition, it shows how easily this SQL database can be modified to allow for more data to be stored within this database. For example, another data field for how much money has been spent on installing the upgrades could be added if there was a need for this data to be tracked. 

### Summary of Solution

The following solution described above meets the objective of this project because it gives the Equipment Engineers a viable option for tracking the upgrade information they have for their tools. This solution is the most viable way for the engineers because it provides them with the ability to track all of this information in once place while also allowing the application to sort and filter through this data internal which decreases the amount of time it takes to find this data. Plus, it gives upper management a resource that they can use to help determine why different tools within the fab run more efficiently and are more reliable than other tools. Leading to upper management having a better understanding on how to invest money on upgrading tools so that the fab is impacted in the best way. 

## Project Controls

# Risk Management Table Goes Here

| Stakeholder Name | Role | Responsiblities |
| :----------------: | :------: | :----: |
| Bryce Vegh | Lead Designer | To draft and finalize all documents pertaining to the project. While also designing all the code for the project |

# Issues Log Table Goes Here

| Stakeholder Name | Role | Responsiblities |
| :----------------: | :------: | :----: |
| Bryce Vegh | Lead Designer | To draft and finalize all documents pertaining to the project. While also designing all the code for the project |

# Change Control Log Table Goes Here

| Stakeholder Name | Role | Responsiblities |
| :----------------: | :------: | :----: |
| Bryce Vegh | Lead Designer | To draft and finalize all documents pertaining to the project. While also designing all the code for the project |

# Role and Responsibilites of End Users Table Goes Here

| Stakeholder Name | Role | Responsiblities |
| :----------------: | :------: | :----: |
| Bryce Vegh | Lead Designer | To draft and finalize all documents pertaining to the project. While also designing all the code for the project |

## Project Cost and Schedule

The project did not require any materials or elements to be purchased to develop the project effectively. This is due to all the materials and elements that are used within the project are free to use for public and/or commercial use. The only cost of the project was developing and testing the project which will be included within the programming work breakdown portion of this section. The cost for engineering time was set at 100 dollars per hour and the cost for testing time was set at 65 dollars per hour. 

# Materials and Elements of Project Table Goes Here

| Stakeholder Name | Role | Responsiblities |
| :----------------: | :------: | :----: |
| Bryce Vegh | Lead Designer | To draft and finalize all documents pertaining to the project. While also designing all the code for the project |

# Figure 8 Goes Here

# Figure 9 Goes Here

## Appendix A - References

JetBrains. (2019). PyCharm: The Python IDE for Professional Developers. JetBrains.com; JetBrains. https://www.jetbrains.com/pycharm/

Pycharm. (2022, December 22). Create and run your first Python project - Help | PyCharm. PyCharmHelp.com; Pycharm. https://www.jetbrains.com/help/pycharm/ creating-and-running-your-first-python-project.html

PySimpleGUI. (2022). Cookbook - PySimpleGUI. Pysimplegui.org; PySimpleGUI. https://www.pysimplegui.org/en/latest/cookbook/

PySimpleGUI. (2021). PySimpleGUI. Www.pysimplegui.org; PySimpleGUI. https://www.pysimplegui.org/en/latest/

Python Software Foundation. (2019, May 29). Welcome to Python.org. Python.org; Python Software Foundation. https://www.python.org/

SQLite. (2022, December 14). Appropriate Uses for SQLite. Sqlite.org. https://www.sqlite.org/whentouse.html#:~:text=SQLite%20is%20often%20used%20as

SQLite Tutorial. (2022). SQLite Tutorial - An Easy Way to Master SQLite Fast. SQLiteTutorial.com; SQLite Tutorial. https://www.sqlitetutorial.net/

SQLite Tutorial. (2018). SQLite Python. SQLiteTutorial.com; SQLite Tutorial. https://www.sqlitetutorial.net/sqlite-python/

## Aprendix A - Copyright Compliance

**Description of PySimpleGUI Library**

The PySimpleGUI library was used to develop the GUI of the business application, which allows the users to interact with the SQL databases to either view, edit, add, or remove data from the databases. Next, this library was not adapted at all for this application, it was just used in a custom way to add the different features that were needed for this application to allow the most functionality for the end users. Plus, there were no modification done to the library because the library already provided all the needed functions in its original state. The development team decided to use this library and not develop our own because developing this library would take a considerable amount of time and significantly increase the development cost due to engineering time. Lastly, a library is used/required because if it is not used then the development team is spending valuable time developing these features from scratch leading to this time being wasted that could have been used to improve the system. 

**PySimpleGUI Library Copyright Reference**

Free Software Foundation, Inc. (2007, June 29). PySimpleGUI License. GitHub.com. https://github.com/PySimpleGUI/PySimpleGUI/blob/master/license.txt

**Description of PyCharm Python IDE Compiler**

JetBrains is the developer for PyCharm that was used in the development process, which PyCharm is a Python IDE compiler that was used to compile and run the Python code that was developed for the application. Next, PyCharm was not adapted for this application because it provides the application with a place to write, test, and compile all the code for the project like it would for any other software development project. Lastly, PyCharm was not modified in any way because the compiler provided all the needed resources for developing the application so there was no need to modify the compiler to add more features. In addition, the development team decided to use the IDE compiler instead of developing our own because this would create a whole second project that would require massive amounts of engineering and testing time that would cost a significant amount of money. 

**PyCharm Copyright Reference**

JetBrains. (2020, October 27). Terms of Use. JetBrains.com. https://www.jetbrains.com/ legal/docs/company/useterms/

**Description of Python Language**

Python was the language that was used to develop the application due to the ease of use that the language provides to the developers. Plus, the Python language is one of the easiest languages to learn due to the number of resources that can be found on the internet. Next, the Python language was adapted by adding two different libraries to it that allowed for more capabilities of the language like creating SQL databases and GUIs. Lastly, the Python language was not modified by anyone on the development team because the language with the libraries added was everything that was needed to develop the application. In addition, the development team did not try to write our own language due to the limited amount of time that was given, and all the time would be used just to develop the new language. 

**Python Copyright Reference**

Python Software Foundation. (2022). Python Copyright Policy. Python.org. https://www.python.org/doc/copyright/#:~:text=A%20few%20files%20have%20a

**Description of SQLite Library**

The SQLite library was used in this capstone project to allow for the databases where all the data was stored to be developed. Meaning the addition of this library added the features that allowed for the developer to design and build the SQL databases. Next, the SQL library was not adapted at all because the library already provided all the needed functionality to design and build different SQL databases for the application. In addition, there was no modifications done to the library due to all the functionality that the library already provided to the development team. This library was used instead of designing our own because the work involved with building this library would have taken away valuable time from developing and refining the application. Lastly, libraries are used/required because it allows for added functionality to be included within the coding language that is being used allowing for more complex and useful software system to be developed at a faster rate. 

**SQLite Library Copyright Reference**

SQLite. (2021, November 10). SQLite Copyright. Sqlite.org. https://www.sqlite.org/copyrigh .html#:~:text=SQLite%20Is%20Public%20Domain&text=Anyone%20is%20free%20to%20copy
