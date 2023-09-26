#!/bin/bash

# copy python script to /usr/local/bin and make executable
sudo cp ./serverup.py /usr/local/bin
sudo chmod 744 /usr/local/bin/serverup.py

# copy systemd service and timer files to /etc/systemd/system
sudo cp ./serverup.service /etc/systemd/system
sudo cp ./serverup.timer /etc/systemd/system

# install the systemd timer and service
sudo systemctl enable serverup.timer
sudo systemctl start serverup.timer
