start:
	poetry run uvicorn main:app --reload

reset:
	poetry run python -m scripts.reset_db
	poetry run python -m scripts.seed_admin