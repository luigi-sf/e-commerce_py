start:
	poetry run uvicorn main:app --reload

reset-db:
	python reset_db.py