freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

run:
	PYTHONPATH=src uvicorn src.main:app --reload

test:
	PYTHONPATH=src pytest -svv --cov=. tests/

lint:
	isort --atomic --force-single-line-imports --profile=black --line-length=100 .
	black --line-length=100  .
