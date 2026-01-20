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

- To link a microphone to a container, you need to install [PulseAudio](https://github.com/pgaskin/pulseaudio-win32/releases/download/v5/pasetup.exe). At the `Select Additional Tasks` step, check `Add a firewall rule (4713/tcp)` and select `Allow external connections on private networks`. For the other steps, let the default options.

- If you use an SSH key to authenticate with GitHub, execute the following commands in an Administrator terminal :

    1. 
        ```powershell
        Get-Service ssh-agent
        ```

        1.1. If nothing shows :    
        ```powershell
        Add-WindowsCapability -Online -Name OpenSSH.Client
        ```

    2.
        ```powershell
        Set-Service ssh-agent -StartupType Manual
        ```

    3.
        ```powershell
        ssh-add /path/to/your/key
        ```

- If you use Git Credentials Manager (if you logged to your GitHub account using your browser/password/token), you have nothing else to do.

#### On MacOS

- To link a microphone to a container, you need to install [PulseAudio](https://formulae.brew.sh/formula/pulseaudio).

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

- If you use an SSH key to authenticate with GitHub, execute the following command :
 
    ```bash
    ssh-add --apple-use-keychain /path/to/your/key
    ```

- If you use Git Credentials Manager (if you logged to your GitHub account using your browser/password/token), you have nothing else to do.

#### On Linux

> WIP

### Development Environment

This project **MUST BE** developed using the Devcontainer configuration provided.

- [For VSCode](https://code.visualstudio.com/docs/devcontainers/containers#_quick-start-open-an-existing-folder-in-a-container)
- [For PyCharm (and mainly all Jetbrains IDEs)](https://www.jetbrains.com/help/pycharm/start-dev-container-inside-ide.html)
- For any other IDE, search by your own.

With that, you will directly have access to a system that acts similarly to the real implementation.

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