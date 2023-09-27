#add virtual environment named .venv
python3 -m venv .venv

#enter virtual environment
source .venv/bin/activate

for windows virtual env
.venv/Scripts/activate

#install requirements to the virtual environment
pip install -r requirements.txt

#run app locally on localhost:8000 (127.0.0.1:8000)
python3 manage.py runserver
