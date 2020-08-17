# Prototype Web application
### Proto_App runs Python 3 and Django 3. The database is local SQLite3 file.

**Important: Not production grade! Run only for educational purposes!**

The ProtoApp application is a very simple application suitable for demo and educational purposes.
This application is a POC

### Functionalities

#### Elements of the ProtoApp:

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

#### Limitations worth noting:

- The superuser created at install is the only one that has access to the admin panel (URL/admin)
- There are NO user facing profile nor password management capabilities.
- By default the users do not have credits and the superuser needs to add credits to the users.
- Uploaded files are limited to 2.5MB per file
- Uploaded images will be proportionally resized to max 800px width or 600px height (whichever side is larger)

### Installation
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

### Running in Docker Image with Persistent Data
#### The following environment variables are set up in the Docker image. Create a host paths for these folders and map the volumes on running the Docker container
- DJANGO_DATABASE_PATH = /home/app/db
- DJANGO_MEDIA_PATH = /home/app/media
- DJANGO_STATIC_PATH = /home/app/static

Example
    docker run -d -p 80:80\
     -v $HOME/Dev/proto_app/app/media:/home/app/media\
     -v $HOME/Dev/proto_app/app/static:/home/app/static\
     -v $HOME/Dev/proto_app/app/db:/home/app/db\
     docker_image_id

#### Default The following environment variables are set up in the Docker image
The default superuser account is: **shodan@trioptimum.com** with password: **RickenbackerVonBraun**
