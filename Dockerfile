# Pull base image
FROM python:3.10-slim as builder

# Set environment variables
WORKDIR /pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY requirements.txt requirements.txt 

#Install libcairo
RUN apt-get update
RUN apt-get upgrade -y

# Upgrade pip
RUN set -ex && pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip --upgrade

# Install pipenv
RUN set -ex && pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pipenv --upgrade

# Install dependencies
# RUN set -ex && pipenv lock -r > requirements.txt
RUN set -ex && pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# copy files
FROM builder as final
WORKDIR /app
COPY ./reactions_api/ /app/reactions_api/
COPY ./tests/ /app/tests/