# Using an alpine-linux base image with python installed in it
FROM python:3.11-slim-buster
# changing directory to an empty directory, /app/ (created automatically)
# copying all the files from the BlankDjango (host file system) to /app/ (container file system)
# note that this command will take .dockerignore into consideration
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
# Downloading the needed dependencies
COPY . /code/
RUN pip install -r requirements.txt