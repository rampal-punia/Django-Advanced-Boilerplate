# Django Advance Boilerplate

Django boilerplate for any scalable WebApp project. Equipped with users app, celery, lightbox.js, dropzone.js and cropper.js. 

## What's included

### Project level

1. app folder 
    - to keep all the apps at one place.

2. requirements folder
    Separate for base, development, production & testing

3. secrets.json
    - to store database, email backend credentials and the secret-key

4. Asset/static
    - Local static files with, bootstrap

5. Templates folder
    - base.html
    - partials folder contains _nav, _paginator, _scripts and other html file

### Other Python Packages
1. django-crispy-forms
2. Pillow
3. Django-cleanup

### Task queue manager
1. Celery


### Javascript
1. Ekko-lightbox
2. Dropzonejs
3. Cropperjs



## Requirements
```bash
amqp==5.1.1
asgiref==3.5.2
autopep8==1.6.0
backports.zoneinfo==0.2.1
billiard==3.6.4.0
celery==5.2.7
click==8.1.3
click-didyoumean==0.3.0
click-plugins==1.1.1
click-repl==0.2.0
colorama==0.4.5
Django==4.0.6
django-celery-beat==2.3.0
django-celery-results==2.4.0
django-cleanup==6.0.0
django-crispy-forms==1.14.0
django-debug-toolbar==3.5.0
django-timezone-field==5.0
kombu==5.2.4
Pillow==9.2.0
prompt-toolkit==3.0.30
pycodestyle==2.8.0
python-crontab==2.6.0
python-dateutil==2.8.2
pytz==2022.1
six==1.16.0
sqlparse==0.4.2
toml==0.10.2
tzdata==2022.1
vine==5.0.0
wcwidth==0.2.5

```
