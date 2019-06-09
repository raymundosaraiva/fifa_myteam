release: python manage.py migrate --run-syncdb
release: python manage.py migrate --fake appname
release: python manage.py migrate
web: gunicorn fifa_api.wsgi --log-file -
