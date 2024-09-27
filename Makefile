export 

PROJECT_DIR=app

format:
	ruff format $(PROJECT_DIR)

kraft:
	docker compose -f docker-compose.kraft.yaml up
	
release:
	poetry publish

run:
	docker compose up