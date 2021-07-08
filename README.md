# Pivot Club Website Refinements 
This project is built using the [Django](https://www.djangoproject.com/) web framework and containerized with [Docker](https://www.docker.com/). 
It runs on Python 3.9+

* Before Running the project, check project [CHANGELOG](/docs/CHANGELOG.md)

### HOW TO RUN THIS PROJECT LOCALLY <hr>
### 1 . Using Python Virtual Environment

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/), run `virtualenv venv` and then activate the virtual environment with the following commands for linux `source venv/bin/activate` and for a Windows machine `<venv>\Scripts\activate.bat`
    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/), run `mkvirtualenv venv`

1. Install the requirements with `pip install -r requirements.txt`


2. Ensure you have postgresql installed in your machine, create a new database and set up `.env` as required


1. Run the migrations with `python manage.py migrate`

1. Optionally create a superuser, to be able to access the Django admin: `python manage.py createsuperuser`

1. Copy the `.env.example` file to `.env`,  and fill in the environment specifics

1. Run the server with `python manage.py runserver`
<hr>

### 2.Using Docker Environment 
To run this project in docker you need to follow the following steps:

   - Install [Docker Desktop](https://desktop.docker.com/win/stable/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&amp;utm_medium=webreferral&amp;utm_campaign=dd-smartbutton&amp;utm_location=module) if you're using Windows machine.
     
      * For linux user following the quickstart in docker docs on how to install docker.
        
      * For users with [windows and windows linux subsystem (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10) installed follow the steps below:
        
         - In Docker Desktop settings>>resources>>wsl integration>>click checkbox to enable wsl integration ,then choose linux distro installed in your machine.
           
         - Clone the project from GitHub 
           
         - In the IDE you're using considering it has wsl support enabled, from wsl terminal run the following commands:
   
            ```docker,bash
           # -d for running the container as a detached mode
           # --build to build images making this project and pull appropriate images required for this project such as postgresql
           # sudo for running as a root user
           
           sudo docker-compose up -d --build 
           ```
           to stop the container run this command
            ```docker
           sudo docker-compose down 
           ```
   
<hr>

## Troubleshooting


1. Read the [FAQ](docs/FAQ.md)
<hr>