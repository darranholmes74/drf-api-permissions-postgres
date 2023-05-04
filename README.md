# Project: Permissions & Postgresql and Authentication & Production Server

## Author: Darran Holmes

### How to initialize/run your application
you will need to run pip install -r requirements.txt
docker compose up

#### get request

http get 0.0.0.0:8000/api/v1/snacks/

#### post request

http post 0.0.0.0:8000/api/token/ username=yourUserName password=yourPassword

#### access data

http 0.0.0.0:8000/api/v1/snacks/ 'Authorization: Bearer pasteAccessTokenOverThisString'

## Tests

### How do you run tests?

docker compose run web python manage.py test