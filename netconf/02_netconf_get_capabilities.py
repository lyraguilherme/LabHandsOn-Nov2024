from ncclient import manager
import xmltodict
import os


username = os.getenv('LAB_USERNAME')
password = os.getenv('LAB_PASSWORD')


device = {
    "host": "192.168.0.253",
    "port": 830,
    "username": username,
    "password": password,
    "hostkey_verify": False
}


with manager.connect(**device) as conn:
    for capability in conn.server_capabilities:
        print(capability)
