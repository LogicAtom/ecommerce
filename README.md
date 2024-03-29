# Full-Stack Frameworks with Django

**E-Commerce Website**


### INSTALLS (in terminal):

1. to install django:

pip3 install django
pip3 install django-allauth==0.41.0

2. to create a start project named: ecommerce with the python3 files:

django-admin startproject ecommerce .


3. create a basic .gitignore<br />
touch .gitignore

4. inside .gitignore type this:<br />


`` *.sqlite3 ``

`` *.__pycache__ ``

`` *.pyc ``

<br />

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

<b>pip3 freeze > requirements.txt</b>


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

##### Create your views here.


24. views.py with docstrings added for pep8 compliant


""" views.py, for rendering pages """
from django.shortcuts import render

##### Create your views here.


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

_______________________________________________________________________
<br /><br />

## Making Directories

mkdir static

mkdir media 
<!-- to hold homepage image, and product images, and the place new products go -->

mkdir static/css
<!-- where CSS, JavaScript, and other static files live -->

+++++++++++++++
<br /><br />

## Additional Services (Fonts, Icons, Datasets, etc.)

Google Fonts = https://fonts.google.com/<br />
Font Awesome = https://www.fontawesome.com<br />
Kaggle (free sample data) = https://www.kaggle.com/<br />
JSON Formatter = https://jsonformatter.org/<br />
Temp Email = https://temp-mail.org/en/<br />
Stripe = https://stripe.com<br />

<br /><br />

## mkdir

To place small HTML Snippets to include in the base template using Django. 

mkdir templates/includes

<!-- Fixtures are used to load data very quickly into a Django database -->
mkdir products/fixtures

<!-- create inner products folder so Django knows which app this belongs to -->
mkdir -p products/templates/products

<br /><br />

## Start App

python3 manage.py startapp products


## Create New Apps

python3 manage.py startapp bag

python3 manage.py startapp checkout

python3 manage.py startapp profiles


<br /><br />

profiles app, models.py, null=true, blank=true (means the fields are optional for the user)


## Make Migrations

python3 manage.py makemigrations --dry-run<br />
python3 manage.py makemigrations<br />
python3 manage.py migrate --plan <!-- --plan flag, to make sure there is nothing wrong with the models --><br />
<!-- if not using --plan flag, then its best to specify the app for migrations to not accidently migrate from other apps too -->
python3 manage.py migrate<br />
<br /><br />




## Errors, bugs, fixes

Commenting out code in most of these files will still give errors for the most part. The only way to fix that is to cut the code out and temporarily paste the code into a notepad file.
<br /><br />

## Special files


signals.py = (keeps track of OrderLineItem each time an item is added or updated)., Django includes a “signal dispatcher” which helps decoupled applications get notified when actions occur elsewhere in the framework.<br />Admin, Signals & Forms Part 1 of CI lesson.
<br />
https://docs.djangoproject.com/en/3.2/topics/signals/
<br />
bag.pop(item_id) = .pop function, to remove the item entirely.
<br />
return redirect(reverse('view_bag')) = redirect back to the view_bag using the reverse function. make sure to import reverse at the top of whatever file you use it.
<br />
return HttpResponse(status=200) = used to return a status code 200(OK) for using posting to from a Javascript function. make sure to import HttpResponse.
<br />
except Exception as e:              = to catch any exceptions (variable e)
    return HttpResponse(status=500) = used to return a server error, in case anything goes wrong. make sure to import HttpResponse.
<br />
.session = cookies
<br />
contexts.py<br />
Uses context processors to be available to all templates, and all files, across the entire project.<br />

<code>`${itemId}`</code> = template literal

{{ csrf_token }} = template variable, renders the actual token.
<br />
{{% csrf_token %}} = template tag, renders a hidden input field in a form.
<br />
remove_ = underscore is to be very explicit.
<br />
var size = $(this).data('size'); = use the data method to pull it from the data size attribute.(bag.html, near the bottom of the page)<br />

__________<br />
google research: using data attributes in html elements.<br />
___________<br />
slim version of javascript libraries = does NOT include the various Ajax functions like POST.(use minified versions instead).<br />
<code>__init__.py</code> = used to ensure that the directory is treated as a Python package., to make a module available for imports and to use in templates.<br />
toasts = Bootstrap notifications<br />
{{ block.super }} = used when overriding the post loadjs block., by doing that, it ensures that the Javascript written in the templates that extend to the base.html wont overwrite this call to show all the toasts.
<br /><br />

## Dictionaries

<code>['items_by_size']</code><br />
from bag>views.py
<br /><br />


## PIP3 INSTALLS  

 
pip3 install django


pip3 install django-allauth==0.41.0


pip3 install pillow  <!-- Python Imaging Library for processing images -->


pip3 install django-crispy-forms 
 <!-- Allows formatting of all the forms using bootstrap styling automatically. Simple setup, just add     'crispy-forms' into the installed apps in settings.py, and    CRISPY_TEMPLATE_PACK = 'bootstrap4'    also in settings.py -->
 <!-- this goes in settings.py too right under 'context_processors section' -->

pip3 install django-countries
<!-- used in checkout app, models.py, so the Country field can auto-populate as a drop-down menu -->

<br />
    <code>
        'builtins': [
            'crispy_forms.templatetags.crispy_forms_tags',
            'crispy_forms.templatetags.crispy_forms_field',
        ]
    </code>
<br />
"""
Which will give us access to everything we need from crispy forms across all templates by default.
"""
<br /><br />
    <code>
        pip3 freeze > requirements.txt
    </code>
<br />
"""
Freeze the new requirements to make sure we have crispy forms in there as well as pillow.
"""
<br /><br /><br />

## Register Models

from .models import Product, Category

 Register your models here.<br />
admin.site.register(Product)<br />
admin.site.register(Category)<br />
<br /><br />


## Webhooks

webhooks are like the Django models each time a model is saved or deleted.
except they are sent securely from Stripe to a URL we specify.

<br /><br />

create a superuser:

python3 manage.py createsuperuser

<br /><br />

to confirm:

python3 manage.py runserver

add "/admin/" to end of url to enter Django Administration panel
<br /><br />

## Testing


<br /><br />

## Preventative Measures

To prevent people from manually accessing the URL by typing /checkout, use the below code in, checkout>views.py (checkout/views.py):<br />
<code>
def checkout(request):<br />
    bag = request.session.get('bag', {})<br />
    if not bag:<br />
        messages.error(request, "There's nothing in your bag at the moment")<br />
        return redirect(reverse('products'))<br />
</code>
<br /><br />


## External Documentation

Django - Queries = https://docs.djangoproject.com/en/3.2/topics/db/queries/
<br /><br />


## ERROR Definitions

Pascal case -- or PascalCase -- is a programming naming convention where the first letter of each compound word in a variable is capitalized. No spaces used, including _underscores.
<br />

## Make Migrations

python3 manage.py makemigrations --dry-run<br />
python3 manage.py makemigrations<br />
python3 manage.py migrate --plan <!-- --plan flag, to make sure there is nothing wrong with the models --><br />
<!-- if not using --plan flag, then its best to specify the app for migrations to not accidently migrate from other apps too -->
python3 manage.py migrate<br />
<br /><br />

profiles > apps.py = django.db.models.BigAutoField


## Load Data (to use the fixtures)

python3 manage.py loaddata categories
   <!-- Installed 9 object(s) from 1 fixture(s) -->
python3 manage.py loaddata products
   <!-- Installed 172 object(s) from 1 fixture(s) -->
   <!-- 172 products fully loaded with images, categories, names, descriptions, prices, ratings -->


### SECURITY FEATURES


#### ADDITIONAL RESOURCES/REFERENCES

1. Safety and Security Information for everyday coding - https://cwe.mitre.org/data/definitions/601.html
2. profiles app didn't automatically make a urls.py file, so you must add it manually.
3. JSON Formatter - https://jsonformatter.org/

#### DEPLOYMENT
Heroku 
create your app, then choose Resources, then in addons: type in postgres, choose Hobby free,

then in GitPod, 

pip3 install dj_database_url
pip3 install psycopg2-binary
pip3 freeze > requirements.txt


## Acknowledgements and Credits

Code Institute Tutors (Alan) = Django Admin Model and Project Migrations.  :) <br />
Code Institute Tutors (Ed) = Django and Site Views and Templates.  :) 
<br /><br />
App Coder = Anthony Kozloski