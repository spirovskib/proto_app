# Prototype Web application

Proto_App runs Python 3 and Django 3. The database is local SQLite3 file.

**Important: Not production grade! Run only for educational purposes!**

The ProtoApp application is a very simple application suitable for demo and educational purposes.
This application is a POC

## Functionalities

### Elements of the ProtoApp:

- The ProtoApp allows the creation of projects and posts within each project.
- Access to the projects is restricted. The creator of the project needs to add the other users to the respective project.
- Ability to create a project is controlled by a credits field in the user profile.
- Each project has two permission roles: User and Admin. The Admin role can add or remove users. The User role can create posts within the Project.
- The posts in the application allow for upload of an image as well as PDF attachment. Both file objects are validated using extensions and mimetype (magic numbers).
- The users are self-registering to the application.
- Each user can be a member of multiple projects at the same time.
- There is a general message board that is visible by all registered users on the home page, named Notes.
- Every registered user can add a note to the general message board.
- Automatic cleanup of files on delete of post (currently only from admin interface)

### Limitations worth noting:

- **Important, change immediately:** In DOCKER initial install the default superuser account is: *shodan@trioptimum.com* with password: *RickenbackerVonBraun*
- The superuser created at install is the only one that has access to the admin panel (URL/admin)
- There are NO user facing profile nor password management capabilities.
- By default the users do not have credits and the superuser needs to add credits to the users.
- Uploaded files are limited to 2.5MB per file
- Uploaded images will be proportionally resized to max 800px width or 600px height (whichever side is larger)

## Installation

### Docker Installation

#### Prepare the DJANGO_SECRET_KEY for the container

In order for the container to run properly it must have the DJANGO_SECRET_KEY variable populated with a random string. This string MUST NOT BE SHARED to other users, so it's created before running the container.

Create the DJANGO_SECRET_KEY env file.

    LC_ALL=C </dev/urandom tr -dc 'A-Za-z0-9!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' | head -c 50 > secret.txt
    echo DJANGO_SECRET_KEY='"'`cat secret.txt`'"' > django_env.txt
    rm secret.txt

### Running Non-Persistent data Docker Container

If you just want to see how the application works, you can run it without persistent data. This means that the data (media and database) is stored within the container and will be lost when the container stops.

#### Run the non-persistent data container
You can run the ProtoApp docker container with the following command. You can access the application on your localhost on port 80.

    docker run -d -p 80:80\
     --env-file django_env.txt\
     beyondmachines/proto_app:latest

### Running Persistent Data Docker Container

In order to create persistence of data (media and database) outside of the container you need to create the folders for volume mapping on the host.
The following instructions and created patsh are an example only but they are compatible with the container running script below. If you want to change the paths make sure that you also change them in the docker run path below.

##### For the database

    mkdir $HOME/Dev/proto_app/app/db
this maps to the path /home/app/db in the container, defined by the DJANGO_DATABASE_PATH

##### For the media (uploaded files)

    mkdir $HOME/Dev/proto_app/app/media
this maps to the path /home/app/media in the container, defined by the DJANGO_MEDIA_PATH

##### For the static content (css, javascript and similar)

    mkdir $HOME/Dev/proto_app/app/static
this maps to the path /home/app/media in the container, defined by the DJANGO_MEDIA_PATH

#### Run the persistent data container
You can run the ProtoApp docker container with the following command. You can access the application on your localhost on port 80.

    docker run -d -p 80:80\
     --env-file django_env.txt\
     -v $HOME/Dev/proto_app/app/media:/home/app/media\
     -v $HOME/Dev/proto_app/app/static:/home/app/static\
     -v $HOME/Dev/proto_app/app/db:/home/app/db\
     beyondmachines/proto_app:latest

### Running from source

#### Create a folder and create virtual environment

    mkdir proto_application
    cd proto_application
    virtualenv -p python3 .

#### To run setup as well as the app always activate the virtual env
    source bin/activate

#### Download the repo:
while in proto_application folder run:

    git clone https://github.com/spirovskib/proto_app

#### Initial setup (in the folder where the git clone stored the code):
    pip install -r requirements.txt
    LC_ALL=C </dev/urandom tr -dc 'A-Za-z0-9!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' | head -c 50 > secret_key.txt
    python manage.py makemigrations accounts
    python manage.py migrate accounts
    python manage.py makemigrations
    python manage.py migrate
    python manage.py makemigrations application
    python manage.py migrate

    python manage.py createsuperuser

*Important: the python-magic is a wrapper around the libmagic C library, and that must be installed as well. More details on installation of libmagic here:*

    https://pypi.org/project/python-magic/

### Running of the app (on localhost at port 8000)
    python manage.py runserver