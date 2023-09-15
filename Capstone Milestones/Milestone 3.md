<p align="center">Tool Upgrade Tracking Business Application

<p align="center">Bryce Ryan Vegh

<p align="center">Master of Science in Software Development Capstone Design Specification

<p align="center">Grand Canyon University

<p align="center">Professor Mortoza Abdullah

<p align="center">Revision: B

<p align="center">June 28, 2023

# Abstract

The Tool Upgrade Tracking Business Application is being designed to give Equipment Engineers the ability to track upgrades on semiconductor tools that they are responsible for upgrading and maintaining, which the tools they work on build the different layers of microchips. This application will give the engineers a tool they can use to track what upgrades are available to install on their tools and give them the ability to track the upgrades that they already installed on the tools. The idea of this application came from looking at how inexperienced and experienced Equipment Engineers work to track the available and installed upgrades on the tools they are responsible for. From observing these engineers, it showed that the less experienced Equipment Engineers struggled to track this information and that they could not find a method that worked for them. The main point that was taken from watching the engineers was that the inexperienced engineers struggled due to not having the years of experience of working on the tools they are responsible for. Meaning that creating an application like this will help to bring the inexperienced engineers up to speed, allow them to understand what is going on with their tools better, and to understand what resources they have available to them. 

The application design will include the use of a Structured Query Language (SQL) database for storing the available upgrade and installed upgrade data. Next, the application design will include a Graphical User Interface (GUI) that will allow the user to interact with the data and will be designed to be user-friendly. The design of the GUI will include features that allow the user to initiate tasks that allow the user to add, remove, search, and view the data that is stored in the SQL database. 

The accomplishment of this application is to create a user-friendly application that helps Equipment Engineers on tracking this data. This will be achieved by designing a GUI that is easy to use and navigate while also providing the engineers with training on how to use the features of the application. 

# Design Introduction

The project that is being proposed is to design a business application that Equipment Engineers can use to track the different available and installed upgrades for the tools that they are responsible for. The information that will be tracked for the available upgrades is what parts are needed for the upgrade, how much the upgrade will cost, and how much time it will take to install the upgrade. Then, for the installed upgrades the application will track and organize a list of all the different upgrades that have been installed on each of the tools. Below an Architectural Diagram has been provided for reference to show the physical modules/components of the application are. 

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%203%20Figures/Figure%201.png" />
</p>

<p align="center">Figure 1: Architecture Diagram for the Tool Upgrade Tracking Application

The challenges being addressed are how Equipment Engineers track the available and installed upgrades for their tools that they are responsible to upgrade and maintain. With this, Equipment Engineers were approached and questioned about how they track their available and installed upgrades on their tools. From these discussions the conclusion was made that there is not one way to track the available and installed upgrades effectively. Plus, from the questioning and discussing with these engineers, it was found that many of them track this information by either remembering it in their head, writing it down in a notebook, or logging it in an excel file on their computer. Meaning that a commonality was found, which was that all the engineers felt that their way was not efficient and that it took a decent amount of time to find the information when they needed it. After the discussion was done, the engineers were pitched the idea of creating this application, and they all were eager to hear about the application and would like to the application developed. Leading to the reasons of why this application is being pursued because all the Equipment Engineers feel that it will be an efficient and reliable way for them to track the available and installed upgrades on their tools. 

## Project Deliverables

- Create SQL database that can store and retrieve data for the GUI when a user is asking for the information to be inputted or retrieved. 

- Create a functioning GUI that allows the user a way to add and see the data that the SQL database is either inputting or retrieving. 

- Designing the application to be robust with an 85% uptime when running. (Uptime meaning that the application is fully functional and not having issues or some bug within the application.)

- Have a simple design of the GUI, meaning there is minimal number of features (buttons, tab selection, etc.) within the different portions of the GUI. 

- Create levels of control to the application so that different users have different accesses to what they can do within the application. (An example would be having one level that only allows data to be viewed.)

# Detailed High-Level Solution Design

## Introduction

The application that is being developed will be used by Equipment Engineers in semiconductor fabs to track what available upgrades and installed upgrades on the tools that are used to build microchips. This application will be called the Tool Upgrade Tracking Business Application. The design of the application will be using an SQL database library in python to create the database where the available and installed upgrade data will be stored. Which the available upgrade data will include what parts are needed for the upgrade, how much the upgrade will cost, and how much time it will take to install the upgrade. Then, the installed upgrade data will consist of a running list of the different upgrades that have been installed onto the tool. This is the main section that will be doing most of the work, the other part of the application will be the GUI or Graphical User Interface which is what the user will use to interact with the data. The user will be able to add, edit, view, or delete data from either the available upgrade data or installed upgrade data. With this, this provides an introduction and a brief explanation of what the project design is. 

## Detailed Overview

The approach that will be taken to ensure the non-functional requirements of security is met by this solution is by having the application be run off an onsite server. This means that the application will not be connected to the internet whatsoever, which helps protect the application from cyber-attacks because the application cannot be attacked remotely. In addition, this solution will also have user logins that will be connected to what permission each user has. Doing this will prevent a user from being able to perform a task that they should not be allowed to do. Meaning that these will help strengthen the security of application because users will only have access to what they absolutely need in order to perform their job. 

The approach that will be taken to ensure the non-functional requirement of performance is met by this solution is by having all the task performed in the background to be simplified as much as possible. This will be done by breaking up the tasks as much as possible to allow for simple and quick tasks for the application to run. With breaking down the tasks of the application, it will help to prevent the application from slowing down or freezing due to a complex task being performed. So, in other words, this is how the solution will work to ensure that the non-functional requirement of performance to be met.  

The project is to design a business application that Equipment Engineers will use to track available upgrades and the upgrades that have already been installed on the tools. With the information for the available upgrades to include what parts are needed, how much the upgrade will cost, and how much time it will take to install the upgrade. In addition, the installed upgrade information will be a list of all the different upgrades that a specific tool has installed on it. Tracking the upgrade information will be done using an SQL database because it will allow for adequate storage capacity while also keeping the relationships of all the data safe. This handles the backend of the application, meaning everything that is done in the background. Next, the users will need something that they can use to interact with the database which will be a graphical user interface or GUI. The GUI will need to allow the user to add, view, edit, and delete data from the database so that the user can track all the upgrade information accurately. In addition, to these features the GUI needs to allow the user to allow tools to be compared for what upgrades are installed on them, how much time has been spent installing upgrades on tools, and the amount of money that has been invested into a tool. Then for available upgrades will need to group the available upgrades based on their cost, how much money is needed to invest into the tool, compare the different available upgrades, and group the available upgrades based off of the need time to install the upgrade. These are all the different features that will need to be developed along with the database to make the Tool Upgrade Tracking Application a success. 

## Hardware and Software Technologies

1. Python 3.11.1
2. SQLite Python Library
3. PySimpleGUI Python Library
4. Windows 10 64-bit Computer

| Description | Rationale | Results |
| :---------: | :-------: | :------:|
| Python running the SQL database and GUI at the same time without causing the application to crash. | Python should have no issues running both of these at a time because there is not a ton of processing happen all the time. | Have not completed the initial design of the GUIs yet. Once the GUIs are designed, this work can be done. |
| Creating User level of permission for the application. | This is needed for security of the application and data because it prevents unwanted users from doing anything they are not supposed to. | This will proof of concept will be completed once the SQL database and GUIs are done being developed. |

<p align="center">Table 1: Proof of Concepts

## Logical Solution Design

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%203%20Figures/Figure%202.png" />
</p>

<p align="center">Figure 2: Logical Solution Design Diagram

## Physical Solution Design

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%203%20Figures/Figure%203.png" />
</p>

<p align="center">Figure 3: Physical Solution Design Diagram

# Detailed Technical Design

## General Technical Approach

The general approach to developing this application is to develop the SQL database portion of the application first. This is to allow time and detail to be put into this portion of the application, plus the database development is going to be the most complicated part to develop. After the SQL database portion is developed, the focus will be put on developing the different GUIs next. The best approach to developing the GUIs is to develop the main home page GUI and then slowly work to develop the GUIs that are for the specific tasks. This approach to developing the application is the best because it allows for the most complicated portion of the application to be worked on first, giving the developer the most possible amount of time to work on it. 

## Database ER Diagram

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%203%20Figures/Figure%204.png" />
</p>

<p align="center">Figure 4: Entity Relation Diagram

## Database Dictionary

| Column | Description | Datatype | Null |  PK   |
| :-----:| :----------:| :-------:| :---:| :---: |
| Installed Upgrade - Tool Name | The name of the tool for the installed upgrades that are trying to be tracked by the application. | String | No | Yes |
| Installed Upgrade - Upgrades | Running list of all the upgrades that are installed on the tool. | String | No | No |
| Available Upgrade - Upgrade Name | The name of the upgrade that is being tracked by the application. | String | No | Yes |
| Available Upgrade - Cost | The total cost of purchasing the upgrade that is being tracked by the application. | Float | No | No |
| Available Upgrade - Part | A list of all needed parts to complete the upgrade on the tool. | String | No | No |
| Available Upgrade -  Time | Amount of time it will take to fully install the upgrade onto a tool. | Float | No | No |

<p align="center">Table 2: Database Dictionary for Tool Upgrade Tracking Business Application

## FlowChats/Process Flows 

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%203%20Figures/Figure%205.png" />
</p>

<p align="center">Figure 5: Application Screen Flow Diagram of the Upgrade Tracking Application

## Sitemap Diagram

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%203%20Figures/Figure%206.png" />
</p>

<p align="center">Figure 6: Initial Sitemap of the Upgrade Tracking Application

## User Interface Diagrams

## Installed UPgrade User Interface Wireframe Diagrams

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%204.png" />
</p>

<p align="center">Figure 7: User Interface Wireframe Diagram for Tool Comparison

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%205.png" />
</p>

<p align="center">Figure 8: User Interface Wireframe Diagram for Time Installing

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%206.png" />
</p>

<p align="center">Figure 9: User Interface Wireframe Diagram for Amount Invested

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%207.png" />
</p>

<p align="center">Figure 10: User Interface Wireframe Diagram for View Installed Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%208.png" />
</p>

<p align="center">Figure 11: User Interface Wireframe Diagram for Add Installed Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%209.png" />
</p>

<p align="center">Figure 12: User Interface Wireframe Diagram for Edit Installed Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%2010.png" />
</p>

<p align="center">Figure 13: User Interface Wireframe Diagram for Delete Installed Upgrade

## Available Upgrade User Interfaces Wireframe Diagrams

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%2011.png" />
</p>

<p align="center">Figure 14: User Interface Wireframe Diagram for Add Available Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%2012.png" />
</p>

<p align="center">Figure 15: User Interface Wireframe Diagram for Edit Available Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%2013.png" />
</p>

<p align="center">Figure 16: User Interface Wireframe Diagram for Delete Available Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%2014.png" />
</p>

<p align="center">Figure 17: User Interface Wireframe Diagram for View Available Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%2015.png" />
</p>

<p align="center">Figure 18: User Interface Wireframe Diagram for Low-Cost Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%2016.png" />
</p>

<p align="center">Figure 19: User Interface Wireframe Diagram for Low Install Time

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%2017.png" />
</p>

<p align="center">Figure 20: User Interface Wireframe Diagram for Tool Comparison

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%2018.png" />
</p>

<p align="center">Figure 21: User Interface Wireframe Diagram for Needed Investment

## UML Diagrams

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%203%20Figures/Figure%2022.png" />
</p>

<p align="center">Figure 22: UML Class Diagram of the SQL Database for Upgrades Available to Install

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%203%20Figures/Figure%2023.png" />
</p>

<p align="center">Figure 23 : UML Class Diagram of the SQL Database for Upgrades Installed

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%203%20Figures/Figure%2023.png" />
</p>

<p align="center">Figure 24: UML Class Diagram for Graphical User Interface (GUI)

## Non-Functional Requirements

| Non-Functional Requirements | Feature | Justification |
| :-------------------------: | :------:| :-----------: |
| NFR-1 | Data Integrity | 1) Provide the user will verification that the data the change in the data has been completed to the correct data. 2) To show the user after they have interacted with the data what changes were made. |
| NFR-2 | Durability | 1) Perform extensive testing on all the features that will be implemented in the application. |
| NFR-3 | Efficiency | 1) Design the methods for pulling data from the database in the most efficient way. 2) Perform testing on the different methods for pulling data from the database. |
| NFR-4 | Maintainability | 1) Provide comments for all code that has been written so any developer can understand what each portion of code is supposed to be doing. 2) Provide documentation that helps with what to look at when troubleshooting issues within the application. |
| NFR-5 | Performance | 1) Design code to break up tasks so that one function is not performing multiple tasks that have the possiblity to slow down the application. 2) Perform testing on all functions to verify they are creating lagging of the application. |
| NFR-6 | Testability | 1) Designing test cases for when testing is being performed to help the developers understand what needs to be tested. 2) Provides tools that will help with testing of the application. |

<p align="center">Table 3: Non-Functional Requirements Justification

## Security 

The one security issue that will be relevant to the Tool Upgrade Tacking application is the level of permission each of the users will have within the application. This is a security issue because you do not want all users to have the same permissions because not all users need to have the ability to modify or add new data to the database. This issue is handled by adding in a user login that will have different levels of permissions depending on what username and password you enter into the login. Meaning that this solves the issues of all users having the same permissions because you will just give the correct login and password to the users depending on what level of permissions you want them to have. 

# Appendix A – Technical Issue and Risk Log

| ID    | Description | Project Impact | Action Plan/Resolution | Owner | Importance | Date to Review | Date Resolved | 
| :---: | :---------: | :------------: | :--------------------: | :---: | :--------: | :------------: | :-----------: |
| 1 | SQL Database not connecting to add, edit, delete, or view data. | Increase development time due to making changes to the code of the application. | To change the code to have the application reestablish connection to the SQL Database every time a task is done that involves the SQL Databases. | Bryce Vegh | High | 11/9/22 | 11/11/22 |
| 2 | The wrong button being selected on the Graphical User Interface for which database the user wants to interact with. | The user selects an incorrect database to add, view, edit, or delete data from. | Designing the tasks that the Graphical User Interface uses as simple as possible. Doing this allows for a lowered possibility of the Graphical User Interface from freezing or lagging until a task is completed. | Bryce Vegh | Medium | 1/9/23 | 1/13/23 |
| 3 | The need for the Graphical User Interface to have more functions and features. | The application not being as custom to the user’s needs. Making the application not as useful for the user. | To talk with as many Equipment Engineers to determine what the most needed functions and features that the application will need. Add more specific functions and features later on. | Bryce Vegh | Low | 3/6/23 | 3/10/23 |

<p align="center">Table 4: Technical Issue and Risk Log

# Appendix B – References

JetBrains. (2019). PyCharm: The Python IDE for Professional Developers. JetBrains.com; JetBrains. https://www.jetbrains.com/pycharm/

Pycharm. (2022, December 22). Create and run your first Python project - Help | PyCharm. PyCharmHelp.com; Pycharm. https://www.jetbrains.com/help/pycharm/ creating-and-running-your-first-python-project.html

PySimpleGUI. (2022). Cookbook - PySimpleGUI. Pysimplegui.org; PySimpleGUI. https://www.pysimplegui.org/en/latest/cookbook/

PySimpleGUI. (2021). PySimpleGUI. Www.pysimplegui.org; PySimpleGUI. https://www.pysimplegui.org/en/latest/

Python Software Foundation. (2019, May 29). Welcome to Python.org. Python.org; Python Software Foundation. https://www.python.org/

SQLite. (2022, December 14). Appropriate Uses for SQLite. Sqlite.org. https://www.sqlite.org/whentouse.html#:~:text=SQLite%20is%20often%20used%20as

SQLite Tutorial. (2022). SQLite Tutorial - An Easy Way to Master SQLite Fast. SQLiteTutorial.com; SQLite Tutorial. https://www.sqlitetutorial.net/

SQLite Tutorial. (2018). SQLite Python. SQLiteTutorial.com; SQLite Tutorial. https://www.sqlitetutorial.net/sqlite-python/

# Appendix C – Copyright Compliance 

## Description of PySimpleGUI Library

The PySimpleGUI library was used to develop the GUI of the business application, which allows the users to interact with the SQL databases to either view, edit, add, or remove data from the databases. Next, this library was not adapted at all for this application, it was just used in a custom way to add the different features that were needed for this application to allow the most functionality for the end users. Plus, there were no modification done to the library because the library already provided all the needed functions in its original state. The development team decided to use this library and not develop our own because developing this library would take a considerable amount of time and significantly increase the development cost due to engineering time. Lastly, a library is used/required because if it is not used then the development team is spending valuable time developing these features from scratch leading to this time being wasted that could have been used to improve the system. 

**PySimpleGUI Library Copyright Reference**

Free Software Foundation, Inc. (2007, June 29). PySimpleGUI License. GitHub.com. https://github.com/PySimpleGUI/PySimpleGUI/blob/master/license.txt

## Description of PyCharm Python IDE Compiler

JetBrains is the developer for PyCharm that was used in the development process, which PyCharm is a Python IDE compiler that was used to compile and run the Python code that was developed for the application. Next, PyCharm was not adapted for this application because it provides the application with a place to write, test, and compile all the code for the project like it would for any other software development project. Lastly, PyCharm was not modified in any way because the compiler provided all the needed resources for developing the application so there was no need to modify the compiler to add more features. In addition, the development team decided to use the IDE compiler instead of developing our own because this would create a whole second project that would require massive amounts of engineering and testing time that would cost a significant amount of money. 

**PyCharm Copyright Reference**

JetBrains. (2020, October 27). Terms of Use. JetBrains.com. https://www.jetbrains.com/ legal/docs/company/useterms/

## Description of Python Language 

Python was the language that was used to develop the application due to the ease of use that the language provides to the developers. Plus, the Python language is one of the easiest languages to learn due to the number of resources that can be found on the internet. Next, the Python language was adapted by adding two different libraries to it that allowed for more capabilities of the language like creating SQL databases and GUIs. Lastly, the Python language was not modified by anyone on the development team because the language with the libraries added was everything that was needed to develop the application. In addition, the development team did not try to write our own language due to the limited amount of time that was given, and all the time would be used just to develop the new language. 

**Python Copyright Reference**

Python Software Foundation. (2022). Python Copyright Policy. Python.org. https://www.python.org/doc/copyright/#:~:text=A%20few%20files%20have%20a

## Description of SQLite Library

The SQLite library was used in this capstone project to allow for the databases where all the data was stored to be developed. Meaning the addition of this library added the features that allowed for the developer to design and build the SQL databases. Next, the SQL library was not adapted at all because the library already provided all the needed functionality to design and build different SQL databases for the application. In addition, there was no modifications done to the library due to all the functionality that the library already provided to the development team. This library was used instead of designing our own because the work involved with building this library would have taken away valuable time from developing and refining the application. Lastly, libraries are used/required because it allows for added functionality to be included within the coding language that is being used allowing for more complex and useful software system to be developed at a faster rate. 

**SQLite Library Copyright Reference**

SQLite. (2021, November 10). SQLite Copyright. Sqlite.org. https://www.sqlite.org/copyrigh .html#:~:text=SQLite%20Is%20Public%20Domain&text=Anyone%20is%20free%20to%20copy
