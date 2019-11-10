# Django simple REST API example with rest_framework ViewSets

One end point with HEAD, GET, POST ,DELETE and PATCH http methods to a pizza ordering simple logic.
GET and HEAD end points to other data information.

![Alt text](test_images/api_root.png?raw=true "API root")

POST order example:

![Alt text](test_images/order_pizza_berlin.png?raw=true "Example off order creation")

GET examples:

![Alt text](test_images/order_list.png?raw=true "list orders through GET")
![Alt text](test_images/get_order.png?raw=true "get  order through GET")
![Alt text](test_images/filter_order.png?raw=true "filter orders through GET")

Updating order using PATCH:

![Alt text](test_images/update_order_patch.png?raw=true "orders PATCH")

PATCH validation response:

![Alt text](test_images/change_status.png?raw=true "validation in PATCH update")

DELETE order example:

![Alt text](test_images/order_delete.png?raw=true "validation in PATCH update")

### Installing

Installation on ubuntu 18.04

###Install and set up of Postgres:

``` bash
sudo apt update
sudo apt install postgresql postgresql-contrib postgis postgresql-11-postgis-2.5
sudo -u postgres psql -c 'create user pizzaman with encrypted password 'peperoni';'
sudo -u postgres psql -c 'create database pizza WITH OWNER pizzaman;'
sudo -u postgres psql -c CREATE EXTENSION postgis;'
```

##Install and set up virtualenv:

``` bash
# mkdir .virtualenv
# sudo apt install python3-pip
# pip3 install virtualenv
# pip3 install virtualenvwrapper
```

##Insert the following code to you .bashrc file:

``` bash

#Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=/home/goran/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh "

```



```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

python manage.py test

For testing the orders endpoint http methods


## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

