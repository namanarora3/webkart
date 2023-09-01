Steps to run this Repo Locally
To start the backend server
Go to the project directory


We recommend you to use virtual environment

  python -m venv venv
Activate virtual environment

  For Windows PowerShell

    venv/Scripts/activate.ps1
  For Linux and MacOS

    source venv/bin/activate
Install dependencies

  pip install -r requirements.txt
Create .env file in project's root directory(base directory), and add SECURITY_KEY, EMAIL_HOST_USER, and EMAIL_HOST_PASSWORD

Run Migrations

 python manage.py makemigrations
 python manage.py migrate
Start the server

  python manage.py runserver