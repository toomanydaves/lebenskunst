# Lebenskunst
Django-based Server with MySQL DB

## System requirements
*   git
*   python3/pip
*   mysql
*   [mysqlclient](https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-db-api-drivers)

# INSTALLATION

## Set up a Database
Create a database. Name it whatever you like.

    mysql -u root -p
    mysql> CREATE DATABASE lebenskunst_dev;

Create a user with a password and full access to the db.

    mysql> GRANT ALL PRIVILEGES ON lebenskunst_dev.* TO 'lebenskunst'@'localhost' IDENTIFIED BY 'dev';

Logging in to db with user to confirm success.

    mysql -u lebenskunst -p lebenskunst_dev

## Create a virtualenv environment with python 3
    virtualenv -p /Library/Frameworks/Python.framework/Versions/3.5/bin/python3 lebenskunst
    source lebenskunst/bin/activate
    (lebenskunst)

## Get and install the source
    git clone https://github.com/toomanydaves/lebenskunst.git
    cd lebenskunst
    (lebenskunst) pip install -r requirements.txt

## Create an .env file in the top-level directory to store your local credentials
    DEBUG=True
    DB_NAME='lebenskunst_dev'
    DB_USER='lebenskunst'
    DB_PASSWORD='dev'
    DB_HOST='localhost'
    DB_PORT=3306

## Migrate the db schema
    (lebenskunst) python manage.py migrate

## Add a superuser
    (lebenskunst) python manage.py createsuperuser

## Run the  server
    (lebenskunst) python manage.py runserver
