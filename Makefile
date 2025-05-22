.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

pre-requirements:
	@scripts/pre-requirements.sh

.PHONY: local-setup
local-setup: pre-requirements ## Sets up the local environment (e.g. install git hooks)
	scripts/local-setup.sh
	make install

.PHONY: build
build: pre-requirements ## Install the app packages
	docker build -t fastapi-boilerplate .

.PHONY: up
up: pre-requirements build ## Run the app inside docker
	docker run -p 8000:8000 fastapi-boilerplate

.PHONY: install
install: pre-requirements ## Install the app packages
	rye pin 3.12.8
	rye sync

.PHONY: update
update: pre-requirements ## Updates the app packages
	rye lock --upgrade

.PHONY: add-package
add-package: pre-requirements ## Installs a new package in the app. ex: make install package=XXX
	rye add $(package)

.PHONY: run
run: pre-requirements ## Runs the app in production mode
	OPENAPI_URL= rye run fastapi run

.PHONY: dev
dev: pre-requirements ## Runs the app in development mode
	rye run fastapi dev

.PHONY: check-typing
check-typing: pre-requirements  ## Run a static analyzer over the code to find issues
	rye run ty check .

.PHONY: check-lint
check-lint: pre-requirements ## Checks the code style
	rye run ruff check

.PHONY: lint
lint: pre-requirements ## Lints the code format
	rye run ruff check --fix

.PHONY: check-format
check-format: pre-requirements  ## Check format python code
	rye run ruff format --check

.PHONY: format
format: pre-requirements  ## Format python code
	rye run ruff format

.PHONY: checks
checks: pre-requirements check-lint check-format check-typing  ## Run all checks

.PHONY: test-unit
test-unit: pre-requirements ## Run unit tests
	rye run pytest tests/unit -ra -x --durations=5

.PHONY: test-integration
test-integration: pre-requirements ## Run integration tests
	rye run pytest tests/integration -ra -x --durations=5

.PHONY: test-acceptance
test-acceptance: pre-requirements ## Run acceptance tests
	rye run pytest tests/acceptance -ra -x --durations=5

.PHONY: test
test:  ## Run all the tests
	rye test

.PHONY: watch
watch: pre-requirements ## Run all the tests in watch mode
	rye run ptw --runner "pytest -n auto tests -ra -x --durations=5"

.PHONY: coverage
coverage: pre-requirements ## Generates the coverage report
	rye run coverage run --branch -m pytest tests
	rye run coverage html
	@open "${PWD}/htmlcov/index.html"

.PHONY: pre-commit
pre-commit: pre-requirements check-lint check-format check-typing test-unit
	
.PHONY: pre-push
pre-push: pre-requirements test-integration test-acceptance

.PHONY: rename-project
rename-project: ## Rename project make rename name=new-name
	sed -i 's/fastapi-boilerplate/$(name)/' pyproject.toml
	sed -i 's/fastapi-boilerplate/$(name)/' Makefile
