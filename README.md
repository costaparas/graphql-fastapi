# GraphQL FastAPI

Demo [FastAPI](https://fastapi.tiangolo.com/) project utilizing
the [Strawberry](https://strawberry.rocks/) library.

## Project structure

- [src/](src/): source code for the API
- [tests/](tests/): unit tests for the API written with [pytest](https://docs.pytest.org)

## Prerequisites

This project uses:

- [Python 3.9.16](https://www.python.org/downloads/release/python-3100/) or above,
- [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line)
  for package management, and
- [virtualenv](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments)
  for isolation.

Set these up using the linked instructions.

## Local development and testing

```sh
VENV_DIR=.venv

# Create a new virtual environment
python3 -m venv $VENV_DIR

# Enter virtual environment
source $VENV_DIR/bin/activate

# Run Makefile commands
make ...

# Exit virtual environment
deactivate
```

Check out the [Makefile](Makefile) for the commands to run. Description below:

- `make freeze`: refresh latest requirements
- `make install`: install current requirements
- `make run`: run the API server
- `make test`: run the unit tests (+ coverage checking!)
- `make lint`: apply some basic linting over the codebase

Use of the Makefile assumes you are in an environment where
[make](https://www.gnu.org/software/make/manual/make.html) is available. If
you're not, consider switching to one to save yourself some trouble down the
line.

## License

Copyright (C) 2023 Costa Paraskevopoulos

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see http://www.gnu.org/licenses/.
