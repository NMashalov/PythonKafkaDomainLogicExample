export 

PROJECT_DIR=app

format:
	ruff format $(PROJECT_DIR)

release:
	poetry publish

run:
	docker compose up