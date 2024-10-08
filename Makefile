.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup: ## Sets up the local environment (e.g. install git hooks)
	scripts/local-setup.sh
	make install

.PHONY: build
build: ## Install the app packages
	docker build -t fastapi-boilerplate .

.PHONY: install
install: ## Install the app packages
	rm -rf poetry.lock
	poetry install

.PHONY: update
update: ## Updates the app packages
	poetry update

.PHONY: add-package
add-package: ## Installs a new package in the app. ex: make install package=XXX
	poetry add $(package)
	poetry install

.PHONY: run
run: ## Runs the app in production mode
	OPENAPI_URL= poetry run fastapi run

.PHONY: dev
dev: ## Runs the app in development mode
	poetry run fastapi dev

.PHONY: check-typing
check-typing:  ## Run a static analyzer over the code to find issues
	poetry run mypy .

.PHONY: check-lint
check-lint: ## Checks the code style
	poetry run ruff check

.PHONY: lint
lint: ## Lints the code format
	poetry run ruff check --fix

.PHONY: check-format
check-format:  ## Check format python code
	poetry run ruff format --check

.PHONY: format
format:  ## Format python code
	poetry run ruff format

.PHONY: test-unit
test-unit: ## Run unit tests
	poetry run pytest -n auto tests/unit -ra

.PHONY: test-integration
test-integration: ## Run integration tests
	poetry run pytest -n auto tests/integration -ra

.PHONY: test-acceptance
test-acceptance: ## Run acceptance tests
	poetry run pytest -n auto tests/acceptance -ra

.PHONY: test
test: test-unit test-integration test-acceptance ## Run all the tests

.PHONY: watch
watch: ## Run all the tests in watch mode
	poetry run ptw --runner "pytest -n auto tests -ra"

.PHONY: coverage
coverage: ## Generates the coverage report
	poetry run coverage run --branch -m pytest tests
	poetry run coverage html
	@open "${PWD}/htmlcov/index.html"

.PHONY: pre-commit
pre-commit: check-lint check-format check-typing test-unit
	
.PHONY: pre-push
pre-push: test-integration test-acceptance

.PHONY: rename-project
rename-project: ## Rename project make rename name=new-name
	sed -i 's/fastapi-boilerplate/$(name)/' pyproject.toml
