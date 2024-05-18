# Django Advance Boilerplate With Different Image Upload Apps

Django boilerplate for any scalable WebApp project.

This boilerplate is equipped with __users app__, __celery__, __django-debug-toolbar__, __lightbox.js__, __dropzone.js__ and __cropper.js__.

## Overview

### Login

<img src="static\img\login.png" height=auto width=450 />

### Register

<img src="static\img\register.png" height=auto width=450>

### Registration under approval

- Login through django admin after createsuperuser command, in users model check active box.
- Logout from django admin
- Restart app and login again.

<img src="static\img\reg_under_approve.png" height=auto width=450>

### Main page

<img src="static\img\dashboard.png" height=auto width=450>

### Upload single image app

<img src="static\img\single.png" height=auto width=450>

### Cropperjs

<img src="static\img\cropperjs.png" height=auto width=450>

### Images uploaded via dropzone

<img src="static\img\dropzone.png" height=auto width=450>

## Why this boilerplate?

- To avoid the repetitive tasks of setting up a new Django Web App project. If a project requires image upload, and user login/register functionalities, this boilerplate can be used for easy start up.

## Project Structure

- Separate app folder containing all apps
  - Apps details:
    - singleimages: To upload single image at a time using django forms and models.

    - multipleimages: To upload multiple images using django forms and models.

    - croppedimages: To upload single original image using django forms and models, and then cropping that image(using cropperjs) and storing all cropped images corresponding to the orig image.

    - dropzoneimages: To upload multiple images using dropzonejs.

    - Users: A users app with login, logout and sign up pages.

- Reusable/Pluggable Apps
  - All apps can be added to other projects with tweaking a little.(Yes few lines need to be added or deleted from settings, urls, and views if an app is removed.)

- Settings.py
  - base.py
  - development.py
  - production.py
  - test.py

- Secrets.json (For boilerplate only. Preferably add in .gitignore)
  - To store database, email backend credentials and the secret-key

- static
  - Local static files with, bootstrap

- Templates folder
  - base.html
  - partials folder contains _nav,_paginator, _scripts and other html file

- Requirements folder
  - Separate for base, development, production & testing

## Other Python Packages
- django-crispy-forms
- crispy-bootstrap4
- Pillow
- Django-cleanup
- OpenCV

```bash
# install dependencies
pip install django-crispy-forms crispy-bootstrap4 Pillow Django-cleanup opencv-python

pip install celery django-celery-beat django-celery-results

pip install django-debug-toolbar
```

## Task queue manager

- Celery

## Javascript

- Ekko-lightbox: To display images in a lightbox.

- Dropzonejs: To upload multiple images

- Cropperjs: To crop an image at front-end

## Used dependencies

This boilerplate relies on the following plugins, libraries and frameworks:

- [Bootstrap](https://getbootstrap.com/)
- [Django](https://www.djangoproject.com/)
- [django-registration](https://github.com/ubernostrum/django-registration)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Pillow](https://github.com/python-pillow/Pillow)
- [Opencv2](https://opencv.org/)
- [Dropzone](https://www.dropzone.dev/js/)
- [CropperJs](https://fengyuanchen.github.io/cropperjs/)
- [Ekko-lightbox-BS5](https://github.com/trvswgnr/bs5-lightbox)
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)

## Hit star ⭐ if you find this helpful! 
