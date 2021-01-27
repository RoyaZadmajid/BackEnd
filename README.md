#  Happiness Level

Happiness is a Django app to recieve and gather data about team member's happiness levels. 

Detailed documentation is in the "docs" directory.

Quick start
-----------
1. This project currently has three apps called core, happiness, and teams which were listed under the INSTALLED_APPS within settings.py as follow: 

    INSTALLED_APPS = [
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  'rest_framework',
      &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;   'teams',
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  'happiness',
    ]

2. To install and setup the project and its required packages, a virtual environment should be created and activated, before installing the packages through running the following command:
  &nbsp;&nbsp;&nbsp;&nbsp;   ``pip install -r requirements.txt`` 

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit &nbsp; http://127.0.0.1:8000/admin/ &nbsp; to create a team, member, and/or submit a happiness level through the Django Admin suite. 

5. Visit &nbsp; http://127.0.0.1:8000/api/v1/happiness_level/ &nbsp; to call an internal API which returns statics on teams and user's happiness levels.


### Installation Summary
The following languages and frameworks are currently used:

* [Python] - Python 3.6.9
* [Django] - Django 3.1.5
* [Django REST framework] - Django REST framework 3.12.2

Create a Virtual Environment, install the dependencies and devDependencies and start the server.
 1. create separate directory for virtual environment within the project directory
 2. cd into venv directory
	 
     &nbsp;&nbsp;&nbsp;&nbsp;    ``$  cd venv``
	
     &nbsp;&nbsp;&nbsp;&nbsp;    ``$  virtualenv -p python3 .`` 
 3. Install the packages
 
	 &nbsp;&nbsp;&nbsp;&nbsp;    ``$ pip install -r requirements.txt`` 

 
