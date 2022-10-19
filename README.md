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
Create `secrets.py` file in `bank` folder, paste code and fill DB settings.

```python
from django.core.management.utils import get_random_secret_key

HIDDEN_SECRET_KEY = get_random_secret_key()

POSTGRES_DATA = {
        "ENGINE": "django.db.backends.postgresql",   
        "NAME": "",
        "USER": "",         # Your Postgres DB settings
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
```


Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd bank
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/register` or `http://127.0.0.1:8000/wallets`.
