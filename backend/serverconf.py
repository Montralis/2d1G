# configuration file for the server

# server setting
# set modus=dev for development and modus=prod for production
server = {
    "modus": "dev",
    "ip": "0.0.0.0",
    "port": "5000",
}

dev_files = {
    "def": "/website/data/",
    "guess": "/website/data/guess.json",
    "two-idiots": "/website/data/two-idiots.json",
    "different-word": "/website/data/guess.json",
}

prod_files = {
    "guess": "/app/backend/website/data/guess.json",
    "two-idiots": "/app/backend//website/data/two-idiots.json",
    "different-word": "/app/backend//website/data/guess.json",
}

use_anonymous = True
