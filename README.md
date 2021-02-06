# health-endpoint
Return health status as an API endpoint

## Executing unit tests

python3 manage.py test

## Building docker container

~~~~
   git clone https://github.com/ozacas/health-endpoint.git
   cd health-endpoint
   docker build deploy
   export RELEASE=ozacas/health-endpoint:v0.1.5
   docker tag `docker images -q | head -n 1` $RELEASE
~~~~

## Publish to eg. docker hub

~~~~
   docker push $RELEASE
~~~~

## Running docker container

~~~~
   docker run -p 8000:8000 $RELEASE
   # after a few seconds to start the container, browse to http://localhost:8000/health
~~~~

