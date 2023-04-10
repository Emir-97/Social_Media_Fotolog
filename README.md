  # Installation and operation guide of the project.
### -First of all, you must have the latest version of Python installed (3.10 or later if possible).
### -Delete the environment attached to the project and create a new one and activate it.
 python3 -m venv "env name" (windows)
 "env name"\Scripts activate
### -Install Django 4.1 onwards into the environment:
 pip install django
### -Libraries to use:
 pip install pillow
### -If you want to delete the files in socialApp/db.sqlite3 to have a new DB so you can add your own records. Then perform the following commands to generate your new database:
  python3 manage.py makemigrations
  python3 manage.py migrate
### -Create your own superuser to manage the project, configure it with your user.name, email and password:
  python manage.py createsuperuser
### -Run the program and copy the URL that comes up (usually localhost unless you modify it to your liking):
  python manage.py runserver

*** That would be all the procedures needed to run this project. In case you can't run it, it's because you missed an install or upgrade of the versions you are using  (always show in the cmd the type of error you might have).***
