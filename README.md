## Django 1.9

## Virtual Env

	$ virtualenv env
	$ source bin/activate

## Cloning project
	$ git clone https://github.com/marcosvicente/ProjectMaps.git

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate


## Further Reading
- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)

## Admin
username = admin
senha = logistica
