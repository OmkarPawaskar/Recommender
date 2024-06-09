FROM python:3.11-alpine3.19

# set environment variables'
ENV PWD ''

# set work directory

WORKDIR /src

# install dependencies
COPY requirements_dev.txt /src/
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements_dev.txt

# Copy PROJECTS
COPY . /src/