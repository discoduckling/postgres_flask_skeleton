# postgres + flask + sqlalchemy skeleton
## stack
* docker
* sqlalchemy
* postgres
* flask

## to use
First, create a virtual environment and start it.

Install requirements
```shell script
pip install -r requirements
```

start dockerized postgres server
```shell script
./docker_up.sh
```

initialize db data
```shell script
python initialize_db.py
```

run flask app
```shell script
python app.py
```

## postgres server
login info for postgres server:
* password: `pass`
* username: `usr`
* db table: `work_org`
* accessible via `localhost:5001`

login info for pgadmin4
* passwoord: `SuperSecret`
* user: `user@domain.com`
* host/name: `postgres`
* port: `5432`
