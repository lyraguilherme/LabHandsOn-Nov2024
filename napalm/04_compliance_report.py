from napalm import get_network_driver
import json
import sys
import os

username = os.getenv('LAB_USERNAME')
password = os.getenv('LAB_PASSWORD')

device = {
    "hostname": "192.168.0.211",
    "username": username,
    "password": password,
    "optional_args": {"transport": "ssh"}
    }

driver = get_network_driver('ios')

napalm = driver(**device)
napalm.open()
print(f"\n### Conexão estabelecida com {device['hostname']}")

# napalm compliance report
output = napalm.compliance_report(sys.argv[1])
napalm.close()

#print(output)
output_json = json.dumps(output, indent=4)
print(output_json)