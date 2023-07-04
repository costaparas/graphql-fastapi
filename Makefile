run:
	PYTHONPATH=src uvicorn src.main:app --reload

test:
	PYTHONPATH=src pytest -svv tests/

lint:
	isort --atomic --force-single-line-imports --profile=black --line-length=100 .
	black --line-length=100  .
