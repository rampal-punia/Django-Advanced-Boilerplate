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

### Other Pyton Packages
1. django-crispy-forms

### Task queue manager
1. Celery

### Javascript
1. Ekko-lightbox
2. Dropzonejs
3. Cropperjs



## Requirements
```bash
asgiref==3.5.2
backports.zoneinfo==0.2.1
Django==4.0.6
django-crispy-forms==1.14.0
Pillow==9.2.0
sqlparse==0.4.2
tzdata==2022.1
```
