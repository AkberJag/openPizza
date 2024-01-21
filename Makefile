# Makefile for Alembic Migrations

# Variables
ALEMBIC_DIR := alembic
DOCKER_PATH := docker exec -w /app/src openpizza-backend-1
m := Create new tables # migration message

# Commands
init:
	$(DOCKER_PATH) alembic init $(ALEMBIC_DIR)

revision:
	$(DOCKER_PATH) alembic revision --autogenerate -m "$(m)"

migrate:
	$(DOCKER_PATH) alembic upgrade head

downgrade:
	$(DOCKER_PATH) alembic downgrade -1

clean:
# $(DOCKER_PATH) rm -rf $(ALEMBIC_DIR)/versions/*
	$(DOCKER_PATH) find $(ALEMBIC_DIR)/versions/ -maxdepth 1 -type f -delete

stamp_h:
	$(DOCKER_PATH) alembic stamp head


build:
	docker compose up -d --build

.PHONY: init revision migrate downgrade clean build