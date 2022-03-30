# Redis Cache
This is a POC to implement the Redis cache with Django.

# About Project
This repo contains some products and a frontend to intract with.
Whenever you try to search a product then it will store the product's information on the RAM for faster accessing.


## All About Redis Cache
Redis is a type of NoSQL database. It stores the information as a KEY:VALUE pair like JSON.
Redis stores the data on the RAM which makes it faster.

## Drawback
It has a drawback: "Whenever system crash then all the data will be lost because it stores the data on system's RAM".

### Install
The project uses Linux(Ubuntu) Operating System.
So For linux, you have to run the following command:

>sudo apt-get install redis

To run the server:

>redis-server

##Run the project
For running this project, you have to run the following commands:

Make an environment

> python3 -m venv venv

Activate the environment

> source venv/bin/activate

Install all the dependencies to the environment

> pip install -r requirements.txt

make the migrations:

> python3 manage.py makemigrations

> python3 manage.py migrate

run the django server:

> python3 manage.py runserver





