[![Python application build test](https://github.com/Montralis/2d1G/actions/workflows/python-app.yml/badge.svg?branch=add-tests)](https://github.com/Montralis/2d1G/actions/workflows/python-app.yml)
[![Python CodeCov test](https://github.com/Montralis/2d1G/actions/workflows/codeCov.yml/badge.svg?branch=add-tests)](https://github.com/Montralis/2d1G/actions/workflows/codeCov.yml)

# 2d1G

> Repository for some funny party drinking games.
> The user can choose between 3 games. A game guide is available for each game.

# Flask backend

## Setup & Installation

Make sure you have the latest version of Python installed and use it.
Tested with Python 3.8.2 64-Bit Windows 10 Enterprise.

```bash
pip install -r backend/requirements.txt
```

Add an `.env` file in the `backend` directory with the following content:

```dotenv
SECRET_KEY="<random key for encrypting>"
USER_PASSWORD="<password for admin login>"
```

## Running the app
Run the app from backend, first nav to backend folder:

```bash
cd backend
```
Then run the app with:

```bash
python main.py
```

If your not sure which python version you are using:

```bash
python3 main.py
```

## Viewing the app

Go to `http://127.0.0.1:5000`
