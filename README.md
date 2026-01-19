# Sound Monitoring (node)

This project is designed to handle sound monitoring using `alsaaudio` and sending information periodically to an MQTT broker.

## Stack

- Python 3.14.2
- MQTT Protocol

## Project Structure

````
.
├── docs/
├── requirements/
│   ├── dev.txt
│   └── prod.txt
├── src/
├── tests/
├── docker-compose.yaml
└── Dockerfile
````

## Quickstart

### Development Environment

This project **MUST BE** developed using the given Docker container as one of the main package used **ONLY** works on Linux.

```bash
docker compose up -d
docker exec -it node-dev bash
```

With that, you will directly have access to the container as a normal shell and you will be able to perform any needed command to run tests or code.

### Production Environment

```bash
pip install -r requirements/prod.txt
python src/main.py
```

## Run tests

```bash
pytest
```

Or if it doesn't work

```bash
python -m pytest
```