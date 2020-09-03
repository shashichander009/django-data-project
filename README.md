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

Go to the dataproject directory where you can see manage.py

Find the .env file. 

Add your database credentials here by updating the values of these values 

DATABASE : Write your DB Name here 

DBUSERNAME : Your DB Username 

DBPASSWORD : Your DB Password 

DBHOST : Your DB Host like localhost etc. 

After you have updated these values, save the file.

Now, go to the helpers folder and run the following command

```bash
python create_db
```
This will create the database if it is not present already. 

Now come back to dataproject folder where you can see manage.py. Run this command

```bash
python manage.py migrate
```
This will add necessary tables. 

### INSERTING DATA INTO DATABASE

Now run the following command, it will add data into your database. Please note that this make take approx 1-2 minutes. Keep patience. 

```bash
python manage.py insertdata
```

### ADMIN STEP UP 

If you want to check the database, you can create a superuser and login into django admin 

```bash
python manage.py createsuperuser
```

### LIVE PROJECT 

Now everything is set up, you can view the project live by running the following command 

```bash
python manage.py runserver
```
Go to the URL : http://127.0.0.1:8000/  to view the project

To Log In as Admin

Go to the URL : http://127.0.0.1:8000/admin/  and use your credentials to log in. 

You can stop the server by pressing Ctrl + C 

### DROP DATABASE

After you are done with checking the project, go to the helpers folder and run this command 

```bash
python drop_db
```
This will remove the database. 

Thank you

