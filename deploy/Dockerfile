FROM python:3.8-slim-buster as base
ARG TARGETPLATFORM

# build up python base
FROM base as builder

RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip3 install --prefer-binary --target=/install -r /requirements.txt 

# multi-stage to reduce final image size
FROM base

RUN useradd --create-home --home-dir /home/app app 
COPY --from=builder /install /usr/local/lib/python3.8/site-packages
RUN apt-get update && apt-get install -y --no-install-recommends git
USER app

WORKDIR /home/app/
RUN git clone https://GITHUB_TOKEN@github.com/ozacas/health-endpoint.git 

WORKDIR /home/app/health-endpoint/health
RUN python3 manage.py migrate
EXPOSE 8000
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
