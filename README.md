# Active Directory Automation Script

## Project 6 of OpenClassrooms Network Administration Class

This script will automate different administration tasks of Active Directory Management.
![img.png](img.png)
## Functionalities :

I have developed these functionalities for this demo project

1. create a group
2. unlock locked users
3. create and activate users using a CSV file
4. delete users using a CSV file
5. activate users using a CSV file

## Prerequisites

1. install Python
2. install needed packages
    1. install pip
   > python -m ensureip --upgrade
    2. install ldap3 package // source : [LDAP3](https://pypi.org/project/ldap3/)
   > pip install ldap3
    3. install python-dotenv package // source : [Python-dotenv](https://pypi.org/project/python-dotenv/)
   > pip install python-dotenv
    4. create a .env file in the root directory with your own data :
   > SERVER=ipAddress or hostName USER=username  
   PASSWORD=YourWonderfulPassword  
   SEARCHDC=,DC=company,DC=com  
   COMPANY=Company  
   DOMAIN=company.com  
   TEMPUSERSPASSWORD=BeautifulTempPassword


3. AD controller must accept SSL/TLS connection otherwise password creation won't work and users will have an empty
   password

## CSV files formats
> You can find csv examples files in the CSV_example_files folder

- csv for user creation:
    * FIRSTNAME, LASTNAME, ADDRESS, PHONE, ORGANISATIONAL UNIT
- csv for user deletion or activation:
    * SAMACCOUNTNAME, OU

## Logs
Log of each operation is in the appropriate text file in "logs" directory.

## Start the script
python main.py
