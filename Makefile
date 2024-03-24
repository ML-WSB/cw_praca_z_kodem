install:
	pip install -r requirements.txt

run:
	flask run

lint:
	pylint app.py
