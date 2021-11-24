# ras-rm-mock-eq
Mock EQ for rasrm dev testing

## Setup
Based on python 3.9

Use [Pyenv](https://github.com/pyenv/pyenv) to manage installed Python versions

Install dependencies to a new virtual environment using [Pipenv](https://docs.pipenv.org/)

```bash
pip install -U pipenv
pipenv install
```

## Run the Application
```
pipenv run python run.py
```

## Configuration
Environment variables available for configuration are listed below:

| Environment Variable            | Description                                                   | Default
|---------------------------------|---------------------------------------------------------------|-------------------------------
| JSON_SECRET_KEYS                | SECRET used for decrypting frontstage payload                 | 'testsecret'
| FRONTSTAGE_URL                  | Url pointed at frontstage in dev environment                  | 'http://localhost:8082/surveys/todo'
| PUBSUB_TOPIC                    | Pub/Sub topic where `Mock EQ` publishes the receipt to mark as survey as completed| 'localhost'
| GOOGLE_CLOUD_PROJECT            | GCP Project where the app exists                              | 8083

These are set in [config.py](config.py)
