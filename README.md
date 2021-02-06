# health-endpoint
Return health status as an API endpoint

## Requirements

 * docker (optional)

 * kubernetes (optional)

 * Python 3 (3.8 recommended)

 * Django >= 3.0

 * DjangoRestFramework

## Executing unit tests

~~~~
$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.020s

OK
Destroying test database for alias 'default'...
~~~~

## Start the server

Note that TCP port 8000 is used (assumes it is not already in use):
~~~~
# change directory into the cloned repository
$ cd health-endpoint
$ python3 manage.py migrate # create SQLLite DB
$ python3 manage.py runserver 0.0.0.0:8000
~~~~

## Building docker container (optional)

~~~~
$ git clone https://github.com/ozacas/health-endpoint.git
$ cd health-endpoint
$ docker build deploy
$ export RELEASE=ozacas/health-endpoint:v0.1.8
$ docker tag `docker images -q | head -n 1` $RELEASE
~~~~

## Publish to eg. docker hub (optional)

Note container must have been built by the above step before this:
~~~~
$ docker push $RELEASE
~~~~

## Running docker container

~~~~
$ docker run -p 8000:8000 $RELEASE
~~~~
After a few seconds for the container to start, you can browse to the [health API page](http://localhost:8000/health) or invoke the API endpoint using curl(1):

~~~~
$ curl --header "Accept: application/json" http://localhost:8000/health
{"git hash":"823428e668bca17fcaf59333f05f619f35e8fab4","app name":"health-endpoint","app version":"v0.1.8"}
~~~~

## Running locally using docker (optional)

~~~~
$ docker run -p 8000:8000  `docker images -q | head -n 1`
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 06, 2021 - 08:12:22
Django version 3.1.6, using settings 'health.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
~~~~
