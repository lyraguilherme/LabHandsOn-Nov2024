from napalm import get_network_driver
import json
import os

username = os.getenv('LAB_USERNAME')
password = os.getenv('LAB_PASSWORD')

routers = [
    '192.168.0.211',
    '192.168.0.212',
    '192.168.0.213',
    '192.168.0.214'
    ]

switches = [
    '192.168.0.201',
    '192.168.0.202',
    '192.168.0.203',
    '192.168.0.204'
    ]

driver = get_network_driver('ios')

for r in routers:
    device = {
        "hostname": r, 
        "username": username,
        "password": password,
        "optional_args": {"transport": "ssh"}
        }

    napalm = driver(**device)
    napalm.open()
    print(f"\n### Conexão estabelecida com {device['hostname']}")

    # napalm get facts
    output = napalm.get_facts()
    napalm.close()

    #print(output)
    output_json = json.dumps(output, indent=4)
    print(output_json)