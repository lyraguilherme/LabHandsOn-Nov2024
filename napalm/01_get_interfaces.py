from napalm import get_network_driver
import json
import os

username = os.getenv('LAB_USERNAME')
password = os.getenv('LAB_PASSWORD')

Router = {
    "hostname": '192.168.0.253', 
    "username": username,
    "password": password,
    "optional_args": {"transport": "ssh"}
    }

driver = get_network_driver('ios')

napalm = driver(**Router)
napalm.open()
print(f"\n### Conexão estabelecida com {Router['hostname']}")

# napalm get interfaces
output = napalm.get_interfaces()
napalm.close()

output_json = json.dumps(output, indent=4)
print(output_json)