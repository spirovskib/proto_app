# pull official base image
FROM python:3.8.5-slim-buster

# create the app system user, the app system group and home directory (home/app)

#START set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
# Setup the environment variables for the python application
ENV HOME=/home/app
ENV APP_HOME=/home/app/proto_app
ENV DJANGO_DEBUG=False

# create the appropriate directories
RUN mkdir $HOME
RUN mkdir $APP_HOME

# update the system to latest patchlevel, and add imagemagic libraries, then clean up.
RUN apt-get update && apt-get -y install libmagic1 libopenjp2-7 nginx supervisor
RUN apt-get update && apt-get upgrade -y
RUN apt autoremove -y

# install python pip, linter (flake8), supervisor, copy the requirements file and install requirements
RUN pip install --upgrade pip
RUN pip install flake8
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy runtime config files
COPY ./docker_config_files/nginx.conf /etc/nginx/
COPY ./docker_config_files/nginx_proto_app.conf /etc/nginx/conf.d/
COPY ./docker_config_files/supervisor_nginx_proto_app.conf /etc/supervisor/conf.d/

# chown all the files to the app user
RUN addgroup --system app && adduser --system app --ingroup app

WORKDIR $APP_HOME
# change to the app user

# copy the application code and run linter in the copied folder
COPY . $APP_HOME
### RUN chown -R app:app $APP_HOME
RUN flake8 --ignore=E501,F401,W605 $APP_HOME

# copy entrypoint program
COPY ./docker_config_files/entrypoint.sh $APP_HOME

### USER app

# run entrypoint.sh to do migrations - this needs to be fixed since it wont' work with migrations running on the image if the database is not here
# RUN $APP_HOME/entrypoint.sh

CMD ["/usr/bin/supervisord"]
