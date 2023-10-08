# Gaia API

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

## Overview
Gaia API powers all server-side interactions for the Gaia platform. It is a REST-based API that uses [FastAPI](https://fastapi.tiangolo.com/lo/).

See endpoint here https://gaia-api-wpdd2.ondigitalocean.app/docs

## Setting up your development environment
The backend runs on Linux in production so it's expected that you'll be developing on Linux 
or Mac OS X. If you're using Windows, consider using 
[Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install).

Make sure you have the Python 3.10.7 installed. Any minor version will do. If your
system comes with a pre-installed version of Python that is not 3.8, consider using 
[pyenv](https://github.com/pyenv/pyenv) to manage your development version of 
python.

### Managing dependencies
From there, make sure you have [Poetry](https://python-poetry.org/) installed. 
We use `Poetry` rather than `Pip` to install and manage dependencies due to its 
additional features and arguably better developer experience. 
If you haven't installed Poetry, do so using the official installer:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
To check that Poetry is installed:
```bash
poetry --version
```
To updated Poetry:
```
poetry update
```
To uninstall Poetry:
```bash
python install-poetry.py --uninstall
```

### Virtual environments
You can either let Poetry manage the virtual environment for you or you can manage
them manually. 

Note, if you're managing the virtual environment manually, Poetry 
will automatically use it, for example, when installing packages.

For this project, Poetry is configured to automatically create a virtual 
environment at the base in the `.venv/` directory, that is if you do not create 
one.

```bash
python -m venv --prompt venv .venv 
source .venv/bin/activate
```
Once within a virtual environment, install the dependencies:
```bash
poetry install
```
Additional usage is as follows:
```bash
# For production, since we do not need dev dependencies, make sure to add the 
# --no-dev flag:
poetry install --no-dev

# To remove dependencies that are no longer in use, run the following:
poetry install --remove-untracked

# To add a new dependency:
poetry add <dependency>

# To remove a dependency:
poetry remove <dependency>
```
Whenever you modify the `poetry.lock` file, make sure to check it in to git.

### Code Quality
To maintain code quality, a couple of linters and formaters are used:
* [flake8](https://flake8.pycqa.org/en/latest/): use it to check for common
  errors, before committing code, make sure to run `make lint`. To further 
  extend flake8, consider going through
  [Awesome Flake8 Extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensionsf)
  and adding whichever plugin you deem will improve our code quality.
* [black](https://black.readthedocs.io/en/stable/): for code formatting
* [bandit](https://bandit.readthedocs.io): for checking for common security issues
Note, when running in production, do not install development dependencies. Some
development dependencies have licensing that conflicts with liberal proprietary
usage.

### Running the app
```
uvicorn api.main:app --reload
```
