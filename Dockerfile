FROM python:3.8

ARG DJANGO_ENV

ENV PYTHONUNBUFFERED 1


ONBUILD RUN set -ex && mkdir /app
ONBUILD RUN set -ex && mkdir /static

RUN apt-get update

RUN apt-get install -y swig libssl-dev dpkg-dev netcat locales

RUN mkdir /static

WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN set -ex && pip install pipenv

COPY . /app

RUN set -ex &&  pipenv install `(test "$DJANGO_ENV" = production || echo "--dev")` --deploy --system


RUN locale-gen es_CL.UTF-8
ENV LANG es_CL.UTF-8
ENV LANGUAGE es_CL:es
ENV LC_ALL es_CL.UTF-8

ADD . /app/

COPY . /app/