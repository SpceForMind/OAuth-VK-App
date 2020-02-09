pip3 install virtualenv
virtualenv env
source env/bin/activate

pip install -e .
python src/app.py