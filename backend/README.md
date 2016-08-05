# Generic API Backend
This repo contains all the required code to run a stateless API backend

## Dependencies:
- PostgreSQL (Primary Data store)
- Redis (MQ for Celery)


## Development

### Setup Development Environment
```
# Install a pre-commit hook to run tests locally before committing
make install_precommit

# Create a virtualenv to work in
virtualenv -p python3.5 venv
```

### Develop
```
# Activate the venv
source venv/bin/activate

# Install Requirements
pip install -r requirements.txt

# Run the server
python run.py runserver

# Run DB Migrations
python run.py db upgrade

# Generate DB Migrations
python run.py db migrate

# Run Tests
make test
```


## Deployment
