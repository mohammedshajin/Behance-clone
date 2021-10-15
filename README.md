# Behance-clone
Behance clone with Django

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/mhdshjn/Behance-clone.git
$ cd Behance-clone
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Settings.py:

Add your email and password to send welcome mail

```sh
EMAIL_HOST_USER = 'yourmail@mail.com'
EMAIL_HOST_PASSWORD = 'ivcsyarovlaikbd'
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
