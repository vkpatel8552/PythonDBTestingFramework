Pre-requisite 

1) Install Python on your machine (https://www.python.org/downloads/)
2) Install Pycharm on your machine (https://www.jetbrains.com/pycharm/download)
3) Install PostgreSQL on your machine (https://www.postgresql.org/download/) 
	- Keep note of your password as 'admin123' while installing PostgreSQL
	- Don't Install StackBuilder during PostgreSQL installer
4) Open pgAdmin Installer to access/create PostgreSQL DB
	- Connect with DB using above password
	- Create new DB with name FivetranDemoDB
5) Install Git on your local system


How to Run: (If pip command not work use pip3 based on your installation)

To Generate Pytest HTML Report

- Clone the repo into a local repo
- Navigate to the project directory in terminal
- Execute 'pip install -r requirement.txt'. This will install all the dependencies.
- Update the 'configurations/config.ini' file with necessary details about the Postgres server.
- Execute 'pytest --html=report.html' for running all the test files.
- Test Execution HTML report will be generated under the project folder.
        
	
To Generate Allure Report
1) Install Java on your Machine
2) Install NodeJs on your Machine (https://nodejs.org/en/download)
3) Install allure-command line 
	- Open CMD
	- Run Command: npm install -g allure-commandline
4) Check allure installed or not
	- Open CMD
	- Run Command: allure --version
5) Set Execution Policy as Remote signed
	- Open Powershell with Admin Rights
	- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
	- Get-ExecutionPolicy should show Remotesigned
6) Run Test cases by following instruction:
	- Clone the repo into a local repo
	- Navigate to the project directory in terminal
	- Execute 'pip install -r requirement.txt'. This will install all the dependencies.
	- Update the 'configurations/config.ini' file with necessary details about the Postgres server.
	- Execute 'pytest --alluredir="./Reports' for running all the test files.
	- Test Execution HTML report will be generated under the project folder.
7) Navigate to your Project directory in CMD
	Run Command: allure serve ".\Reports"
	
This will generate allure report under tmp directory with all execution details.
	 