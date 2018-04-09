# Zappy

A simple serivce that retrives and stores twitter feeds to mongodb

## Getting started

these instructions will help you get this project up and running using docker.
you can also use good old virtualenv, it's really up to you.

**Note:** you will need to create a twitter app in order for this to work.


## Running the project

### Using Docker and Docker Swarm:

**with docker-ce version 17.12.1**

Initiate a swarm on your machine using.

```
$ docker swarm init
```

run the services stack using the docker-compose.yml file.

```
$ docker stack deploy -c docker-compose.yml <stack-name>
```
don't forget to replace ```stack-name``` with your own stack name

the previous steps will pull the needed images from docker hub.

You can also build the needed images locally using both the frontend and service docker files.

if so you'll need to change the image names in docker-compose.yml to the image names you choose,
for the ```django```,```celery``` and ```web``` services.

**
don't forget to setup the needed environment variables
check the settings section for more info.
**



##### building the frontend image
the docker image for the web service is a simple nginx server that serves static files
from the build artifacts [ dist ], so you will need to build the app before building the image

you can specifiy the ```baseUrl``` for the api in the environments/environment.prod.ts file
before building.

```
$ ng build -prod
```

### Using virtualenv and ng serve

##### First running the backend service

you will need both ```redis``` and ```mongodb``` installed in order for it to work

create a virtual envirnoment using your favorite method.
I personally prefer virtualenvwrapper.

```
$ mkvirtualenv zappy --python=/usr/bin/python3.6

$ pip install -r serivce/requirements/local.txt

$ export TWITTER_CONSUMER_KEY=<your-twitter-app-consumer-key>
$ export TWITTER_CONSUMER_SECRET=<your-twitter-app-consumer-secret>

$ ./manange.py runserver
```

this will run the django project, but you also need celery up and running
in order for background tasks to work.

```
$ celery -A conf.celery_app worker --loglevel=debug
```

##### Second Running the frontend app

After installing the needed packages

```
$ npm install
$ ng serve
```

## Settings:

An example of the env file for use with docker

```
DJANGO_SETTINGS_MODULE=conf.settings.production
DJANGO_SECRET_KEY=<your-django-secret-key>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=<your-allowed-hosts-list>

DJANGO_CORS_ORIGIN_ALLOW_ALL=True
DJANGO_CORS_ALLOW_CREDENTIALS=True

MONGO_URI=mongodb://mongodb:27017/
MONGO_DATABASE_NAME=twitter

CELERY_REDIS_BROKER=redis://redis:6379/0

TWITTER_CONSUMER_KEY=
TWITTER_CONSUMER_SECRET=
MAX_TWEETS_COUNT=200
```

the ```TWITTER_CONSUMER_KEY``` and ```TWITTER_CONSUMER_SECRET``` env variables are required
all other variables will take a default value if not specified

### Notes:
this project was a test task for an interview process, so don't take seriously.

