set up the project need to run following command:

1)create the virtual environment
2)clone the project
3)run >pip install -r requirements.txt
4)set up the DB go to the settings.py file and change the DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_task',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5)python manage.py makemigrations
6)python manage.py migrate
7)run python manage.py runserver

Ready to rock......

