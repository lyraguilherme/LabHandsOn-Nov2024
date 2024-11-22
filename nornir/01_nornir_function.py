import os
import sys
import json
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get


def get_interfaces(task):

    result = task.run(task=napalm_get, getters=['get_interfaces'])

    interfaces_result = result.result['get_interfaces']

    hostname = task.host.name
    marcador = "-" * 25
    print(f"\n{marcador} Exibindo resultados de: {hostname} {marcador}")
    #print(interfaces_result)
    result_json = json.dumps(interfaces_result, indent=4)
    print(result_json)


# importa credenciais
username = os.getenv('LAB_USERNAME')
password = os.getenv('LAB_PASSWORD')

if username == 'None' or not username:
    print('\nCredenciais não definidas. Utilize: \nexport LAB_USERNAME="usuario"\nexport LAB_PASSWORD="senha"\n')
    sys.exit(1)

elif password == "None" or not password:
    print('\nCredenciais não definidas. Utilize: \nexport LAB_USERNAME="usuario"\nexport LAB_PASSWORD="senha"\n')
    sys.exit(1)

else:
    # inicializa nornir usando arquivo de configuração
    nr = InitNornir(config_file="config.yaml")

    # define as credenciais para o nornir a partir das variaveis de ambiente importadas
    nr.inventory.defaults.username = username
    nr.inventory.defaults.password = password
    print('\nCredenciais importadas com sucesso\n')

    # executa task com nornir
    nr.run(task=get_interfaces)
