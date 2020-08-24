.DEFAULT_GOAL:=help
.PHONY: help

# -- CONFIGS --

APP_NAME=kabum-products-api
VERSION=$(shell cat VERSION.txt)

# -- END CONFIGS --

include .env
export

##@ Setup database environment

setup: db-start db-populate ## Start a local instance of PostgreSQL and populate with mock data

db-start:  ## Start a PostgreSQL docker container and create a database named 'kabum'
	docker run --rm -p 5432:5432 --name postgres_db -e POSTGRES_PASSWORD=secret -d postgres
	sleep 10  # Wait for PostgreSQL startup time, be patient...
	docker exec postgres_db psql --username postgres -c 'CREATE DATABASE kabum'

db-populate: install  ## Insert mocked data into database
	python insert_mock_data.py

##@ Run with Python
dev: install run  ## Setup and start Python server in local environment

install:  ## Install Python module requirements
	pip install --upgrade pip
	pip install -r requirements.txt

run:  ## Start Flask REST API server
	gunicorn products_api.main:app --bind $(HOST):$(PORT) -w 2 --preload

##@ Run with Docker
docker: docker-build docker-run ## Build docker image and run the server inside  a container

docker-build: ## Build Docker Image
	docker build --tag $(APP_NAME):$(VERSION) .

docker-run: ## Run Docker Container
	docker run -ti --rm --env-file .env -p $(PORT):80 --network=host \
	--name $(APP_NAME) $(APP_NAME):$(VERSION)

docker-sh: ## Start Bash session in container
	docker exec -ti $(APP_NAME) bash

##@ Helpers
help:  ## Display help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage:\n  make \033[36m<target>\033[0m\n"} /^[0-9a-zA-Z_-]+:.*?##/ \
		 { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
