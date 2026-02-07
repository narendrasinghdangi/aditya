.PHONY: all init dockerfile_build docker_compose_down docker_compose_up docker_compose_down_and_up docker_build_and_up

# Configurations
DOCKERFILE=Dockerfile
DOCKER_COMPOSE=docker-compose.yml

dockerfile_build:
	@echo 'BUILDING DOCKER IMAGE: ${DOCKERFILE}'
	@docker build --rm -f ${DOCKERFILE} -t aditya .

docker_compose_down:
	@echo 'Running docker compose down'
	docker compose -f ${DOCKER_COMPOSE} down

docker_compose_up:
	@echo 'Running docker compose up'
	docker compose -f ${DOCKER_COMPOSE} up -d

docker_compose_down_and_up:
	@echo 'Running docker compose down and up'
	docker compose -f ${DOCKER_COMPOSE} down
	docker compose -f ${DOCKER_COMPOSE} up -d

docker_build_and_up: dockerfile_build docker_compose_down_and_up