###########
# BUILDER #
###########

# pull official base image, using the latest available from the Python repo with Alpine Linux
FROM python:3.8.5-slim-buster as builder

# set work directory
WORKDIR /usr/src/app

#START set environment variables
## Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
## Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
# libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
# libharfbuzz-dev libfribidi-dev libxcb1-dev
# update and install dependencies
RUN apt-get update && apt-get -y install libmagic1 libopenjp2-7
RUN apt-get update && apt-get upgrade -y

# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . .
RUN flake8 --ignore=E501,F401,W605 .

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.8.5-slim-buster

# create directory for the app user
# RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system app --ingroup app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/proto_app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get -y install libmagic1 libopenjp2-7 nginx
RUN apt-get update && apt-get upgrade -y
RUN apt autoremove -y
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh to run migrations
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/proto_app/entrypoint.sh"]
