# Pivot Club Website Refinements 
This project is built using the [Django](https://www.djangoproject.com/) web framework. 
It runs on Python 3.9+

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/), run `virtualenv venv` and then activate the virtual environment with the following commands for linux `source venv/bin/activate` and for a Windows machine `<venv>\Scripts\activate.bat`
    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/), run `mkvirtualenv venv`
    <hr>
1. Install the requirements with `pip install -r requirements.txt`
    <hr>
2. Ensure you have postgresql installed in your machine, create a new database and set up `.env` as required
    <hr>
1. Run the migrations with `python manage.py migrate`
    <hr>
1. Optionally create a superuser, to be able to access the Django admin: `python manage.py createsuperuser`
    <hr>
1. Copy the `.env.example` file to `.env`,  and fill in the environment specifics
    <hr>
1. Run the server with `python manage.py runserver`
     <hr>
