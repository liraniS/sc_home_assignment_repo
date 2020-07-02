release: python manage.py migrate --database=heroku_db

web: gunicorn SC_home_assignment.wsgi --log-file -