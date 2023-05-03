Hello, Reviewers!

See useful info below


On settings.py DATABASES you can change config to point to your mysql database

Initial Run:
cd <project directory>

pipenv shell

pipenv install

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
# JDOSER endpoint, for example, to make POST request and create new user
/auth/users/
# to login and auth get token
/api-token-auth/
# to login using JDOSER endpoint
/auth/token/login

# api urls
/api/booking
/api/menu

