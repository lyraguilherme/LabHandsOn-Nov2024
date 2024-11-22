from netmiko import ConnectHandler
import os


username = os.getenv('LAB_USERNAME')
password = os.getenv('LAB_PASSWORD')


routers = { 'Router': '192.168.0.253' }


minha_config = [
    'interface GigabitEthernet0/0/1',
    'description CONFIGURADO COM NETMIKO'
]


for hostname, ip in routers.items():

    device = {
        'host': ip,
        'port': 22,
        'username': username,
        'password': password,
        'device_type': 'cisco_ios'
    }
    connection = ConnectHandler(**device)
    print(f'\n### Conexão estabelecida com {hostname}\n')
    output = connection.send_config_set(minha_config)
    connection.disconnect()
    print(output)
    print('\n')
