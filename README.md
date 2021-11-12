INSTALLS (in terminal):
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


### Start App

python3 manage.py startapp products


### Make Migrations

python3 manage.py makemigrations --dry-run








![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome LogicAtom,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
