# Poor Man's Twitter

This is an example Python app that uses
[Django](http://django.org) and [Vue.js](https://vuejs.org).


## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cd app
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Then visit `http://localhost:8000/` to view Application.

Visit `http://localhost:8000/api/` to view REST Api.


## Technical stack

Following stack elements used in this application:

* Django 3.0+ (backend)
* Django Rest Framework
* Vue
* JQuery
* SQLite

## requirements.txt

requirements.txt should have the following three lines:

```
django==3.2.8
djangorestframework==3.12.4
```


## Frontend

Frontend source codes is located under '/frontend' folder. This is single page Application 
and uses only one 'index.html'.


## Get involved!

I am happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[bilaltonga@gmail.com](mailto:bilaltonga@gmail.com).

* `git clone git@github.com:bgunebakan/poormans_twitter.git`

## Licensing

This library is MIT-licensed.
