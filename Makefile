DOCKER_COMPOSE = docker-compose
ALEMBIC = alembic

install:
	poetry install

format:
	black . && isort .

lint:
	flake8 . && mypy .

test:
	pytest --cov=core --cov=apps

logs:
	@$(DOCKER_COMPOSE) logs -f

build-dev:
	@$(DOCKER_COMPOSE) --profile dev build

down-dev:
	@$(DOCKER_COMPOSE) --profile dev down

up-dev:
	@$(DOCKER_COMPOSE) --profile dev up

build-prod:
	@$(DOCKER_COMPOSE) --profile prod build

down-prod:
	@$(DOCKER_COMPOSE) --profile prod down

up-prod:
	@$(DOCKER_COMPOSE) --profile prod up

restart-dev:
	make down-dev && make build-dev && make up-dev

restart-prod:
	make down-prod && make build-prod && make up-prod

create-migration:
ifndef name
	$(error "name parametresi eksik. Örnek: make create-migration name=add_users_table")
endif
	$(ALEMBIC) revision --autogenerate -m "$(name)"

upgrade:
	$(ALEMBIC) upgrade head

downgrade:
	$(ALEMBIC) downgrade -1

current:
	$(ALEMBIC) current

revision:
ifndef name
	$(error "name parametresi eksik. Örnek: make revision name=create_empty_migration")
endif
	$(ALEMBIC) revision -m "$(name)"

install-pre-commit-hooks:
	poetry run pre-commit install
	poetry run pre-commit install --install-hooks --hook-type commit-msg