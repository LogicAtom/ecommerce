# Full-Stack Frameworks with Django
E-Commerce Website


### INSTALLS (in terminal):
1. to install django:

pip3 install django
pip3 install django-allauth==0.41.0

2. to create a start project named: ecommerce with the python3 files:

django-admin startproject ecommerce .


3. create a basic .gitignore<br />
touch .gitignore

4. inside .gitignore type this:<br />
*.sqlite3 <br />
*.__pycache__ <br />
*.pyc<br />

5. to run the project in an IDE, in terminal type:

python3 manage.py runserver

and expose port 8000


6. run migrations:

python3 manage.py migrate


7. create a superuser:

python3 manage.py createsuperuser


8. to check git connections:

git remote -v

9. The newest version of Django does not automatically import the os module at the top of the settings.py file. If it does not, then add it to the top of settings.py

import os


10. https://django-allauth.readthedocs.io/en/latest/installation.html


11. AUTHENTICATION_BACKENDS = [
    ...
    ##### Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    ##### `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
]

12. add in settings.py code and urls.py code


13. migrate changes:

python3 manage.py migrate


14. run the server to test it out:

python3 manage.py runserver

navigate to /admin:

https://8000-turquoise-gull-003oak5c.ws-us18.gitpod.io/admin/login/?next=/admin/


15. settings.py, add this to temporarily send emails to console to get confirmation links:

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


16. with Redirects working, its time to create a requirements.txt

pip3 freeze > requirements.txt


17. Set up a templates directory (will hold customized allauth templates)

mkdir templates
mkdir templates/allauth


18. Copy all allauth templates into our templates/auth/ directory

cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/


19. create a bunch of blocks with:

{%  %}

inside base.html

20. create a home app:

python3 manage.py startapp home


21. create a directory inside the home app (-p = create parents)

mkdir -p home/templates/home


22. Extend base.html into templates/home/index.html, load static file, load content into h1 using BootStrap syntax, to ensure its working:

{% extends "base.html" %}
{% load static %}

{% block content %}
<h1 class="display-4 text-success"></h1>
{% endblock %}


23. from step 22, we need a views to render this into(templates/views.py)
initially views.py is this:

from django.shortcuts import render

# Create your views here.


24. views.py with docstrings added for pep8 compliant


""" views.py, for rendering pages """
from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


25. Copy all from project level urls.py to a new file in home app called urls.py
and paste into there. so in my case its:  urls.py ecommerce > urls.py home.


"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]



26. Start up the Development Server:

python3 manage.py runserver


27. BTW, to stop a server:

hold down CTRL and tap C

this creates a break in any code all the time, shown by a ^C

28. (psuedo)/not fake, but its the best way i can describe it so as to not have 5billion steps in my project lol. :)
this step is a bridge to the next sections of my Readme.md as the above steps are learning building blocks, the rest is the actual site.
_______________________________________________________________________

## Making Directories

from psuedo-step 28 on...

mkdir static

mkdir media 
<!-- to hold homepage image, and product images, and the place new products go -->

mkdir static/css
<!-- where CSS, JavaScript, and other static files live -->

+++++++++++++++


## Additional Services (Fonts, Icons, Datasets, etc.)

Google Fonts = https://fonts.google.com/
Font Awesome = https://www.fontawesome.com
Kaggle (free sample data) = https://www.kaggle.com/
JSON Formatter = https://jsonformatter.org/


### mkdir

To place small HTML Snippets to include in the base template using Django. 

mkdir templates/includes

<!-- Fixtures are used to load data very quickly into a Django database -->
mkdir products/fixtures

<!-- create inner products folder so Django knows which app this belongs to -->
mkdir -p products/templates/products


### Start App

python3 manage.py startapp products


### Make Migrations

python3 manage.py makemigrations --dry-run
python3 manage.py migrate --plan <!-- --plan flag, to make sure there is nothing wrong with the models -->
<!-- if not using --plan flag, then its best to specify the app for migrations to not accidently migrate from other apps too -->
python3 manage.py makemigrations
python3 manage.py migrate

### pip3 Installs

pip3 install django

pip3 install django-allauth==0.41.0

pip3 install pillow  <!-- Python Imaging Library for processing images -->


### Register Models

from .models import Product, Category

 Register your models here.<br />
admin.site.register(Product)<br />
admin.site.register(Category)<br />

### Load Data (to use the fixtures)

gitpod /workspace/ecommerce $ python3 manage.py loaddata categories
   <!-- Installed 9 object(s) from 1 fixture(s) -->
gitpod /workspace/ecommerce $ python3 manage.py loaddata products
   <!-- Installed 172 object(s) from 1 fixture(s) -->
   <!-- 172 products fully loaded with images, categories, names, descriptions, prices, ratings -->

to confirm:

python3 manage.py runserver

add "/admin/" to end of url to enter Django Administration panel


## External Documentation

Django - Queries = https://docs.djangoproject.com/en/3.2/topics/db/queries/


### Bootstrap Elements
    text-decoration-none

    p-2

    mt-2

    badge

    badge-white

    rounded-0

    border

    border-dark


### Non-Bootstrap Elements which work with bootstrap

    category-badge

    text-black

    .btt-button

    .btt-link


## Acknowledgements and Credits

Code Institute Tutors (Alan) = Django Admin Model, help :) 


App Coder = Anthony Kozloski