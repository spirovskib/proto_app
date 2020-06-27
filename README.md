# Proto_App is a demo Web application  
## Proto_App runs Python 3 and Django 3. The database is local SQLite3 file.  
  
**Important: Not production grade! Run only for educational purposes!**   

There is no attempt at visual aesthetics (no CSS nor any advanced HTML)  
  
### Functionalities  
- Creation of simple posts with title, text, image and PDF upload
- Listing of created posts
- Viewing of individual post
- Automatic Image resize on upload
- File size and format verification on upload (checking extension, size and mimetype)
- Automatic cleanup of files on delete of post
- Django Admin Interface (available after creating superuser during installation)

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
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser


### Running of the app (on localshost at port 8000)  
    python manage.py runserver
