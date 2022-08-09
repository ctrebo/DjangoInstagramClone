# Django Instagram Application

## The goal of this python project is to have a python Instagram applicaton which can be used like Instagram

## Technologies
The Project is created with:

* Python
* Django
* Pillow
* OS library
* datetime library
* better-profanity library

## Prerequisites

* Python
* git

## Setup

To install this project first install following libraries via pip:
```
pip install django Pillow better-profanity
```

clone repository
```
git clone https://github.com/ctrebo/DjangoInstagramClone
```


open djinsta/settings.py, delete line 17 and 18. Then in settings.py search ```SECRET_KEY``` and replace ```str(os.getenv('SECRET_KEY'))``` with the secret key of your choice


go to the project root and run migrations
```
python manage.py migrate
```

at the end start the server
```
python manage.py runserver
```

## Tests
you can run the tests via:
```
python manage.py test
```
