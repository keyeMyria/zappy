# Zappy

A simple serivce that retrives and stores twitter feeds to mongodb

## Getting started

these instructions will help you get this project up and running using docker containers.
you can also use good old virtualenv, it's really up to you.


## Settings:

the following ENV variables are required
you can set them in the serivce/env file

```
TWITTER_CONSUMER_KEY - your twitter app consumer key
TWITTER_CONSUMER_SECRET - your twitter app consumer secret

```

## Running the project

### using a virtualenv

you will need both ```redis``` and ```mongodb``` installed in order for it to work

create a virualenvirnoment using any of your favorite tools
I personally prefer virtualenvwrapper.

```
$ mkvirtualenv zappy --python=/usr/bin/python3.6

$ pip install -r serivce/requirements/local.txt

$ ./manage.py runserver
```

this will run the django project, but you also need celery up and running
in order for the update_twitter_feed task to work

```
$ celery -A conf.celery_app worker --loglevel=debug
```

### Using Docker and Docker Swarm:

you need docker-ce installed for this to work, there's a docker-compose.yml
which you can use to run the project locally, it's also near production ready,
so it's up to you to take the risk.

after initiating a swarm on you'r machine using
```
$ docker swarm init
```

run a service stack using the following command

```
$ docker stack deploy -c docker-compose.yml <stack-name>
```
don't forget to replace <stack-name> with your own

the previous steps will pull the needed images from docker hub
and run them including this project's images.


