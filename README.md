# Transaction system app

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/dmitryhaishun/bank-system.git
$ cd bank-system
```

Create a virtual environment to install dependencies in and activate it:

```sh
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
# You can also use py -3 -m venv .venv
python -m venv .venv
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd bank
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/register` or `http://127.0.0.1:8000/wallets`.
