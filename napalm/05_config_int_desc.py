from napalm import get_network_driver
import json
import os

username = os.getenv('LAB_USERNAME')
password = os.getenv('LAB_PASSWORD')

device = {
    "hostname": "192.168.0.211",
    "username": username,
    "password": password,
    "optional_args": {"transport": "ssh"}
    }

minha_config = '''
interface GigabitEthernet0/0/1
description CONFIGURADO COM NAPALM
'''

driver = get_network_driver('ios')

napalm = driver(**device)

napalm.open()
print(f"\n### Conexão estabelecida com {device['hostname']}")
napalm.load_merge_candidate(config=minha_config)
compare = napalm.compare_config()
napalm.commit_config()
napalm.close()

print(compare)