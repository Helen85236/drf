# drf
<h3>What does this project do.</h3>
Self Learning Platform service
<h3>How to prepare.</h3>
Be sure that you are going use it under linux-compatible operation system.
this program use next external components:
- cron
- postgresql database
- redis-server
- sending emails through smtp protocol 
<h3>How to install.</h3>
- clone project to own disk in new directory
- activate virtual environment (python -m venv venv)
- install all needs packages (pip install -r requirements.txt)
- see next step for configure
<h3>How to configure.</h3>
Please pay your attention to configure .env file
you can find example in root of your project directory
please fill all parameters with your data and save the changed file as .env
after that you need create empty database 
you may use command
>psql -U postgres
and then
>CREATE DATABASE <database_name>
alternatively you can use pgadmin or other interface app.
use next commands for tables creation
>python manage.py migrate
and next for create default users
>python manage.py create_default_group
<h3>Ноw it works.</h3>
Start the server with
>python manage.py runserver

