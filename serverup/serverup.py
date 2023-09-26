import os

HOST_NAME: str = "192.168.1.1"

# Ping the host five times to be certain
response: int = os.system(f"ping -c 5 {HOST_NAME}")

# if the response is not 0, the host is down
# so we need to restart the server
if response != 0:
    os.system("reboot")
