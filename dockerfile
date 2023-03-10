# Using an alpine-linux base image with python installed in it
FROM python:3.11-alpine
# changing directory to an empty directory, /app/ (created automatically)
# copying all the files from the BlankDjango (host file system) to /app/ (container file system)
# note that this command will take .dockerignore into consideration
COPY . .
# Downloading the needed dependencies
RUN pip install -r requirements.txt
# Setting up the DB
RUN python manage.py makemigrations
RUN python manage.py migrate
# Opening port 8000 in container
EXPOSE 8000/tcp
# command to be executed when container is running
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]