# UN Population Data Analysis - Django Project 

Do you want to understand how the world population has grown over the years? This project will show you the world population growth story through beautiful charts.


## Language and Libraries

This project is built with 

Backend : Python 3.7.4

Web Framework : Django 2.2

Database : PostgresSQL

Frontend : HTML, CSS

Charting : HighCharts

## Installation

clone this repo 

create a virtual env

activate the virtual env 

install all dependencies

```bash
pip install -r requirements.txt
```

## Usage

### DATABASE SETTING UP

Create a postgres Database and replace the link of SQLALCHEMY_DATABASE_URI in config.py folder. It should be of the format 

postgresql://username:password@localhost:5432/db-name

Once you are done, run the following command 

```bash
flask db upgrade
```
This will create Admin and Employee DB in your database

### PROJECT USAGE

Finally, after all the steps run the following command

```bash
flask run
```

Go to the URL : http://127.0.0.1:5000/  to view the project


### First Steps at the Website

Click Sign Up button and create an Admin. 

Now go to add Employee and create an employee. Important points 
 *  Phone Number should be 10 digits 
 *  Salary can't be zero

On the home page, you can find employee list. 

Click on any Employee to view Details of Employee

If you are logged in you can edit and delete employees. 


