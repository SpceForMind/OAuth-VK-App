export FLASK_APP=src/app
flask db init
flask db migrate -m "user friend table"
flask db upgrade
flask run
