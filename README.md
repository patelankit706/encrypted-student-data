
# Encrypted Student Data

## Hello Users

This student registration program saves the student details in a encrypted format using following technique
  
  * Encrypting entered data using user password
  * User password is SHA512 encrypted


## Dependencies:

  * 1: MySQLdb library
  * 2: crypt library
  * 3: tkinter library
  * 4: mysql
  * 5: Python 2.7.x

## Pre-Configuration:

  * 1: Login into mysql using command "mysql -u 'your_username' -p" and type password
  * 2: Create database using query "Create database Testdb;"
  * 3: Create table using query "create table Students(rollno varchar(50) primary key,name varchar(100),pass varchar(150),mob varchar(50),sex varchar(50),city varchar(50));"
  * 4: Run configure.py using command 'python configure.py'

## Run : 
  * 1: Run program using command "python main_program.py"
