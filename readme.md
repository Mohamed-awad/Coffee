# My E-Commerce Website

this an e-commerce django back-end service for line of coffee machines and custom coffee pods that return json data

## you can do 

* you can get Coffee machines filtered by (product_type, water_line_compatible)
* you can get Coffee pods filtered by (product_type, coffee_flavor, pack_size)

## Install

* you need to install python3
* you need to install pip or pip3 package

## Run the project

* download the project 
* open the project in terminal by press `Ctrl-Alt+T`
* install virtualenv `pip3 install virtualenv` 
* init your virtualenv `virtualenv coffee_env`
* active virtualenv `source coffee_env/bin/activate`
* install required packages on virtualenv `pip3 install -r requirements.txt`
* migrate models to create tables in db `python3 manage.py migrate`
* run server `python3 manage.py runserver`
* open browser on this link `http://127.0.0.1:8000/coffee/api/pods/` to get data from first endpoint
* open browser on this link `http://127.0.0.1:8000/coffee/api/machines/` to get data from second endpoint
