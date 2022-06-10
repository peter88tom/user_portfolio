# How to setup the repository locally
To get this project up and running you should start by having latest version of Python installed on your computer. Install virtual environment in your computer like this
```
pip install virtualenv
```

Clone or download this repository. Open your terminal and change directory into the cloned directory, run the following command in the base directory of this project to create virtual environment

```
virtualenv env
```

That will create a new folder `env` in your project directory. Activate the virtual environment with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with this command

```
pip install -r requirements.txt
```

Run this command to migrate the migrations, the command will create tables for this project

```
python manage.py migrate
```

Create superuser for the project by running the following command

```
python manage.py createsuperuser
```

Now you can run the project with this command

```
python manage.py runserver
```

Using the above command the project will be running on http://localhost:8000

You can register a new user and update profiles, The map will be visible after user update their profiles.

# Technologies used to build this project
- Python - [https://www.python.org/](https://www.python.org/)
- Django Python Framework - [https://www.djangoproject.com/](https://www.djangoproject.com/)
- Requests - [https://pypi.org/project/requests/](https://pypi.org/project/requests/)
- Bootstrap Frontend framework - [https://getbootstrap.com/](https://getbootstrap.com/)
- JQuery - [https://jquery.com/](https://jquery.com/)
- Leaflet - [https://leafletjs.com/](https://leafletjs.com/)
- PositionStack - [https://positionstack.com/](https://positionstack.com/)
