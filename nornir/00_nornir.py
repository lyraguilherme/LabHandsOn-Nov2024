import os
import json
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get


def get_interfaces(task):

    # define a task a ser executada com napalm_get -> get_interfaces
    result = task.run(task=napalm_get, getters=['get_interfaces'])

    # obtem hostname do device onde a task será sendo executada
    hostname = task.host.name

    # cria marcador no estilo ------------
    marcador = "-" * 25

    print(f"\n{marcador} Exibindo resultados de: {hostname} {marcador}")

    # exibe resultados
    #print(interfaces_result)
    result_json = json.dumps(result.result['get_interfaces'], indent=4)
    print(result_json)


# importa credenciais
username = os.getenv('LAB_USERNAME')
password = os.getenv('LAB_PASSWORD')

# inicializa nornir usando arquivo de configuração
nr = InitNornir(config_file="config.yaml")

# define as credenciais para o nornir a partir das variaveis de ambiente importadas
nr.inventory.defaults.username = username
nr.inventory.defaults.password = password
print('\nCredenciais importadas com sucesso\n')

# executa task com nornir
nr.run(task=get_interfaces)