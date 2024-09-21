# FastAPI Boilerplate ![status](https://github.com/pmareke/python-boilerplate/actions/workflows/app.yml/badge.svg)

- This repository is meant to be used as a fast starter point.
- The Python version is the 3.12.
- The project has configured a [Github Action](https://github.com/pmareke/fastapi-boilerplate/actions) which runs on every push to the `main` branch.
- The project has a `Dockerfile` ready to use in order to deploy the app.

## Requirements
- You only need to have [Poetry](https://python-poetry.org) installed.

## Folder structure

- There is a `tests` folder with the tests files.
    - The `unit` folder contains the unit tests, also know as [F.I.R.S.T](https://dzone.com/articles/writing-your-first-unit-tests#:~:text=First%20class%20developers%20write%20their,self%2Dvalidating%2C%20and%20timely.&text=Unit%20tests%20are%20required%20to%20test%20singular%20sections%20of%20code.).
    - The `acceptance` folder contains the tests that validate the app behavior from the outside.
- The production code goes inside the `src` folder.
    - The `delivery` folder contains the `API` logic.
    - The `domain` folder contains the domain classes of the app.
    - The `use_cases` folder contains the business logic.
    - The `common` folder contains the shared logic.
- Inside the `scripts` folder you can find the git hooks files.

## Project commands

The project uses [Makefiles](https://www.gnu.org/software/make/manual/html_node/Introduction.html) to run the most common tasks:

- `add-package package=XXX`: Installs the package XXX in the app, ex: `make install package=requests`.
- `build`: Builds the app.
- `check-typing`: Runs a static analyzer over the code in order to find issues.
- `check-format`: Checks the code format.
- `check-style`: Checks the code style.
- `format`: Formats the code.
- `help` : Shows this help.
- `install`: Installs the app packages.
- `local-setup`: Sets up the local environment (e.g. install git hooks).
- `run`: Runs the app.
- `test`: Run all the tests.
- `update`: Updates the app packages.
- `watch`: Run all the tests in watch mode.

**Important: Please run the `make local-setup` command before starting with the code.**

_In order to create a commit you have to pass the pre-commit phase which runs the check and test commands._

## Packages

This project uses [Poetry](https://python-poetry.org) as the package manager.

### Testing

- [pytest](https://docs.pytest.org/en/7.1.x/contents.html): Testing runner.
- [pytest-xdist](https://github.com/pytest-dev/pytest-xdist): Pytest plugin to run the tests in parallel.
- [expects](https://expects.readthedocs.io/en/stable/): An expressive and extensible TDD/BDD assertion library for Python..

### Code style

- [mypy](https://mypy.readthedocs.io/en/stable/): A static type checker.
- [black](https://black.readthedocs.io/en/stable/): A Python formatter.

