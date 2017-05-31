# eCIP - an efficient Cleaning-in-Place web app built on Django
This is my first web app.

The documentation is very thorough and includes every step taken as much for my future benefit as anything else. This complete guide may also be useful for other beginning developers.

## General Setup
* code organised using github
* /docs folder is used for all documentation which is rendered by github pages (https://nickjstevens.github.io/eCIP/)
* i'm using a Mac
* i use PyCharm as my IDE
* I use sqlitestudio to directly interface with sqlite database for development



## Django Setup
* I followed the instructions here: https://tutorial.djangogirls.org/en/installation/
  - create folder for the project
  - setup virtual environment in this project folder: virtualenv venv
  - activate virtual environment: source venv/bin/activate
  - pip install django
  - pip install djangorestframework
  - pip install markdown (for markdown support for hte browsable API
  - pip install django-filter
  - django-admin startproject app
* Now add the new app and rest-framework to installed apps in settings.py
* update main urls.py to:
    from django.conf.urls import url, include
    from django.contrib import admin

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^/', include('app.urls')),
    ]
* create a urls.py in the app folder, with:
    from django.conf.urls import url
    from . import views

    urlpatterns = [
        url(r'^$', views.index, name = "index"),
    ]
* create static/app directory for css, js, fonts etc
* create templates/app directory for html templates
* create views in views.py, referring to templates in the templates directory
* add any models to the admin.py file so that you can see them in the admin interface
* create models in models.py, including any visible to the admin panel
* python manage.py makemigrations and python manage.py migrate to initialise the database
* python manage.py runserver to start development server
* python manage.py createsuperuser to create a super user with admin access
* add in rest framework settings to settings.py:
    REST_FRAMEWORK = {
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ]
    }
* add this to urls.py in root for rest:
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
* create serializers.py file that serializes are models using hte rest framework

