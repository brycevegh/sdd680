<p align="center">Tool Upgrade Tracking Business Application

<p align="center">Bryce Ryan Vegh

<p align="center">Master of Science in Software Development Capstone Requirements Specification

<p align="center">Grand Canyon University

<p align="center"Professor Ali Wahid

<p align="center">Revision: B

<p align="center">Feburary 2, 2023

# Abstract

The Tool Upgrade Tracking Business Application is being designed to give Equipment Engineers the ability to track upgrades on semiconductor tools that they are responsible for upgrading and maintaining, which the tools they work on build the different layers of microchips. This application will give the engineers a tool they can use to track what upgrades are available to install on their tools and give them the ability to track the upgrades that they already installed on the tools. The idea of this application came from looking at how inexperienced and experienced Equipment Engineers work to track the available and installed upgrades on the tools they are responsible for. From observing these engineers, it showed that the less experienced Equipment Engineers struggled to track this information and that they could not find a method that worked for them. The main point that was taken from watching the engineers was that the inexperienced engineers struggled due to not having the years of experience of working on the tools they are responsible for. Meaning that creating an application like this will help to bring the inexperienced engineers up to speed, allow them to understand what is going on with their tools better, and to understand what resources they have available to them. 

The application design will include the use of a Structured Query Language (SQL) database for storing the available upgrade and installed upgrade data. Next, the application design will include a Graphical User Interface (GUI) that will allow the user to interact with the data and will be designed to be user-friendly. The design of the GUI will include features that allow the user to initiate tasks that allow the user to add, remove, search, and view the data that is stored in the SQL database. 

The accomplishment of this application is to create a user-friendly application that helps Equipment Engineers on tracking this data. This will be achieved by designing a GUI that is easy to use and navigate while also providing the engineers with training on how to use the features of the application. 

# Functional Requirements

| User Story ID | Feature     | User Story | Acceptance Criteria | Aprroval Date |
| :--------------: | :------: | :--------: | :-----------------: | :-----------: |
| US-1 | Track Available Upgrades | As an Equipment Engineer, I want a hassle-free way to track all the different available upgrades there are to install on the tools I am responsible for in the Fab.  | 1) Ability to Track the different available upgrades there are for the tool. 2) Ability to track the name of the upgrade, the cost of the upgrade, the needed parts for the upgrade, and how long it will take in hours to install the upgrade. | 1/27/2023 |
| US-2 | Tracking of the Installed Upgrades | As an Equipment Engineer, I want an easy way to track all the different upgrades I have installed on the tools I am responsible for. | 1) Ability to track all the upgrades that have been installed on all the different tools within the Fab. 2) Tack the name of the tool that the upgrades have been installed on and the running list of upgrades that have been installed. | 1/27/2023 |
| US-3 | Ability to Interact with Database | As an Equipment Engineer, I want a Graphical User Interface that will allow me to interact with the database. | 1) Create a Graphical User Interface that will allow for the user to interact with the database. 2) Ability to select what data the user wants to view, either the Installed or available upgrade data. | 1/27/2023 |
| US-4 | Low Cost Upgrade | As an Equipment Engineer, I want to find out which upgrades cost the least amount so that I can work to install those upgrades first as they will be the easiest to get approved by management. | 1) Ability to sort available upgrades by "under $10k", "under $25K", and "over $25k ". 2) Ability to find upgrades that are installed in the same module of the tool. | 1/27/2023 |
| US-5 | Low Install Time | As an Equipment Engineer, I want to find out what available upgrades have the shortest install time that will create the least amount of idle time for the tool. | 1) Ability to sort available upgrades by "less than 8 hours", "less than 24 hours", and "over 24 hours". 2) Option to show all available upgrade install times. | 1/27/2023 |
| US-6 | Tool Comparison | As an Equipment Engineer, I want to be able to determine which tools need the same upgrades so that I can order multiple upgrade kits at a cheaper price for ordering multiple. | 1)Determine what tools need the same upgrade to allow the upgrade kits to be purchased together. 2) Determine the discount price of ordering the upgrade kits together. | 1/27/2023 |
| US-7 | Tool Comparison | As an Equipment Engineer, I want to be able to compare the different upgrades that have been installed on two tools. This will help to determine why two tools may run different when compared together. | 1) Ability to determine the difference of what upgrades have been installed on two different tools. 2) Options to compare the amount of money that has been invested into the two different tools. | 1/27/2023 |
| US-8 | Amount to Invest in the Tool | As an Equipment Engineer, I want to be able to determine how much money needs to be invested into the tool to install all available upgrades onto the tool. | 1) Access to the different upgrades that still need to be installed on the tool. 2) Totalized amount of money that will need to be spent to fully upgrade the tool. | 1/27/2023 |
| US-9 | Time Spent Installing | As an Equipment Engineer, I want the ability to determine how much time has been spent on upgrade the tool. | 1) Ability to determine the amount of time that has been spent installing upgrades. 2) Option to compare the amount of time that has been spent installing upgrades to the different tools. | 1/27/2023 |
| US-10 | Investment | As an Equipment Engineer, I want to have the ability to pull the running list of installed upgrades to determine how much money has already been invested into the tool. | 1) Ability to pull all the upgrades that have been installed on a tool. 2) Totalize the amount of money that has been spent on upgrading the tool from the list that was pulled. | 1/27/2023 |

<p align="center">Table 1: Functional Requirements - User Stories

# Non-Functional Requirements 

| User Story ID | Feature  | User Story | Acceptance Criteria | Approval Date |
| :-----------: | :------: | :--------: | :-----------------: | :-----------: |
| US-1 | Data Integrity | As an Equipment Engineer, I want to make sure that the application will provide data integrity. This is so that I do not have to worry that the data that I am pulling from the application being incorrect or corrupted. | 1) Provide the user will verification that the data the change in the data has been completed to the correct data. 2) To show the user after they have interacted with the data what changes were made.| 1/27/2023 | 
| US-2 | Durability | As an Equipment Engineer, I want the application to be durable meaning that the application does not require maintenance all the time. | 1) Perform extensive testing on all the features that will be implemented in the application. | 1/27/2023 | 
| US-3 | Efficiency | As an Equipment Engineer, the application should be able to pull data quickly and at a moments notice. This application is supposed to allow us to pull data quickly to solve our current methods that take time. | 1) Design the methods for pulling data from the database in the most efficient way. 2) Perform testing on the different methods for pulling data from the database. | 1/27/2023 | 
| US-4 | Maintainability | As an Equipment Engineer, I want the application to be easily maintainable so that when there is an issue the application is down for a minimal amount of time. | 1) Provide comments for all code that has been written so any developer can understand what each portion of code is supposed to be doing. 2) Provide documentation that helps with what to look at when troubleshooting issues within the application. | 1/27/2023 | 
| US-5 | Performance | As an Equipment Engineer, I want the application to perform well so that I do not have to be waiting for each of the task I want performed to complete. | 1) Design code to break up tasks so that one function is not performing multiple tasks that have the possiblity to slow down the application. 2) Perform testing on all functions to verify they are creating lagging of the application. | 1/27/2023 | 
| US-6 | Testability | As an Equipment Engineer, the application needs to be easy to test to find the issues that are being experience. Meaning that the application needs to be designed to add testing features. | 1) Designing test cases for when testing is being performed to help the developers understand what needs to be tested. 2) Provides tools that will help with testing of the application. | 1/27/2023 |

<p align="center">Table 2: Non-Functional Requirements - User Stories

# Technical Requirements

| Technology or Tool | Approval Date | Justification |
| :----------------: | :-----------: | :-----------: |
| PySimpleGUI Library for Python (Version 4.60.4) | 1/10/2023 | Needed so that the graphical user interface can be designed for the application. |
| PyCharm Python IDE Complier (Version 2022.3.2)| 1/10/2023 | Where all the software will be written and tested in. Gives developer a place to run and compile the code that is written. |
| Python Programming Language (Version 3.11.2)| 1/10/2023 | The programming language that is used for the application. |
| SQLite Library for Python (Version 3.41.0) | 1/10/2023 | Needed so that the SQL databases can be designed and built for the application. |

<p align="center">Table 3: Technical Requirements

# Logical System Design

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%201.png" />
</p>

<p align="center">Figure 1: Logical Architecture Diagram of Upgrade Tracking Application

# User Interface Design

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%202.png" />
</p>

<p align="center">Figure 2: Initial Sitemap of the Upgrade Tracking Application 

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%203.png" />
</p>

<p align="center">Figure 3: Application Screen Flow Diagram of the Upgrade Tracking Application







## Installed UPgrade User Interface Wireframe Diagrams

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%203.png" />
</p>

<p align="center">Figure 4: User Interface Wireframe Diagram for Tool Comparison

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%203.png" />
</p>

<p align="center">Figure 5: User Interface Wireframe Diagram for Time Installing

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%203.png" />
</p>

<p align="center">Figure 6: User Interface Wireframe Diagram for Amount Invested

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%203.png" />
</p>

<p align="center">Figure 7: User Interface Wireframe Diagram for View Installed Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%203.png" />
</p>

<p align="center">Figure 8: User Interface Wireframe Diagram for Add Installed Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%203.png" />
</p>

<p align="center">Figure 9: User Interface Wireframe Diagram for Edit Installed Upgrade

<p align="center">
  <img src="https://github.com/brycevegh/sdd680/blob/main/Milestone%202%20Figures/Figure%203.png" />
</p>

<p align="center">Figure 10: User Interface Wireframe Diagram for Delete Installed Upgrade



## Available Upgrade User Interfaces Wireframe Diagrams


