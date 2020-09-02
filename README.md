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

Create a postgres Database and go the follow file 

dataproject/dataproject/settings.py

Search for DATABASES and replace the following values and save it. 

NAME, USER and PASSWORD

Once you are done, come back to following directory where you can see manage.py

Run the following command

```bash
python manage.py migrate
```
This will create your database with necessary tables as well as Union and Region Data. 

### INSERTING DATA INTO DATABASE

Now run the following command, it will add data into your database. Please note that this make take approx 1-2 minutes. Keep patience. 

```bash
python manage.py insertdata
```

### LIVE PROJECT 

Now everything is set up, you can view the project live by running the following command 

```bash
python manage.py runserver
```
Go to the URL : http://127.0.0.1:8000/  to view the project

You can stop the server by pressing Ctrl + C 

### OPTIONAL STEP

If you want to check the database, you can create a superuser and login into django admin 

```bash
python manage.py createsuperuser
```

Go to the URL : http://127.0.0.1:8000/admin/  and use your credentials to log in. 


Thank you

