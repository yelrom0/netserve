# NetServe

## Description

This is a multi-faceted project with the intention to replace Cloudflare tunnels with a few extra tools to confirm the server is up and running, and to provide a simple way to manage the tunnels.

### ServerUp

This is a simple tool that will check if a server is up and running. It will send a request to the designated gateway and check if the response is the expected response. If there is a failed response more than 5 times, the server will reboot.

I plan on adding more tools to this to check if the server is up and running, but for now this is all it does.

### TunnelManager

This is a simple tool that will manage the tunnels. It will check if the tunnels are up and running, and if they are not, it will start them. It will also add a tunnel to the remote server if it's not already running.

Later I plan on adding a way to manage self-hosted DNS servers, failover for tunnels and DNS servers, and auto-connection to the closest gateways based on availability.

## Installation

### Setup

1. Install [Python 3.9](https://www.python.org/downloads/) or higher.
2. Create a virtual environment with `python -m venv venv` and activate it with `venv\Scripts\activate.bat` on Windows or `source venv/bin/activate` on Linux.
3. Install the dependencies with `pip install -r requirements.txt`.

## Credits

- [selfhosted-gateway](https://github.com/fractalnetworksco/selfhosted-gateway) by Fractal Networks - The inspiration for this project, I am not using any of their code in this project, but I am using parts of their idea.

- [pretty-yaml](https://github.com/mk-fg/pretty-yaml) - used for config files.

- [pulumi-docker](https://github.com/pulumi/pulumi-docker) - used for deploying to the remote gateway.