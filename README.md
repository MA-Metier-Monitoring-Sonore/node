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

### Prerequisites for development

To develop on this project, you need to have [Docker](https://www.docker.com/) installed on your machine.

#### On Windows

To link a microphone to a container, you need to install [PulseAudio](https://github.com/pgaskin/pulseaudio-win32/releases/download/v5/pasetup.exe). No special configurations to make here, follow the setup and continue following this guide.

#### On MacOS

To link a microphone to a container, you need to install [PulseAudio](https://formulae.brew.sh/formula/pulseaudio).

On MacOS, you need a little more configurations to make it accessible. For this,
```bash
nano /opt/homebrew/etc/pulse/default.pa
```

Find these lines :
```bash
### Network access (may be configured with paprefs, so leave this commented
### here if you plan to use paprefs)
load-module module-esound-protocol-tcp
load-module module-native-protocol-tcp
```

And replace them to this :
```bash
### Network access (may be configured with paprefs, so leave this commented
### here if you plan to use paprefs)
load-module module-esound-protocol-tcp auth-anonymous=1
load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;192.168.0.0/16
```

#### On Linux

To link a microphone to a container, update the `docker-compose.yml` file and add the following lines under `python` :

```yml
volumes:
    - /dev/snd:/dev/snd
```

Please **DO NOT** push modifications for this file !

### Development Environment

This project **MUST BE** developed using the given Docker container.

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