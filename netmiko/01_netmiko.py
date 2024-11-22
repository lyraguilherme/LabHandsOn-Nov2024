from netmiko import ConnectHandler
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


for ip in routers:
    connection = ConnectHandler(host=ip, port='22', username=username, password=password, device_type='cisco_ios')
    output = connection.send_command('show ip interface brief')
    connection.disconnect()
    print(output)


for ip in switches:
    connection = ConnectHandler(host=ip, port='22', username=username, password=password, device_type='cisco_ios')
    output = connection.send_command('show spanning-tree vlan 100')
    connection.disconnect()
    print(output)