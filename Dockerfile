FROM anthonyalmarza/alpine-pyenv:cable

MAINTAINER Anthony Almarza <anthony.almarza@gmail.com>

WORKDIR /var/chalk

COPY requirements-dev.txt requirements-dev.txt

VOLUME ['/var/chalk']

RUN pip install -r requirements-dev.txt
