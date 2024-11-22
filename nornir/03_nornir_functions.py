import os
import sys
import json
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get


def get_interfaces(task):

    result = task.run(task=napalm_get, getters=['get_interfaces'])

    interfaces_result = result.result['get_interfaces']

    # obtem hostname do device onde a task esta rodando
    hostname = task.host.name

    # define marcador estilo ------ 
    marcador = "-" * 25

    # exibe resultados do host em questão
    print(f"\n{marcador} Exibindo resultados de: {hostname} {marcador}")
    result_json = json.dumps(interfaces_result, indent=4)
    print(result_json)
    #print(interfaces_result)


def main():

    # importa credenciais
    username = os.getenv('LAB_USERNAME')
    password = os.getenv('LAB_PASSWORD')

    # encerra o script em caso de falha ao importar username
    if username == 'None' or not username:
        print('\nCredenciais não definidas. Utilize: \nexport LAB_USERNAME="usuario"\nexport LAB_PASSWORD="senha"\n')
        sys.exit(1)

    # encerra o script em caso de falha ao importar password
    elif password == "None" or not password:
        print('\nCredenciais não definidas. Utilize: \nexport LAB_USERNAME="usuario"\nexport LAB_PASSWORD="senha"\n')
        sys.exit(1)

    # se username e password foram importados, então segue execução do script
    else:
        # inicializa nornir usando arquivo de configuração
        nr = InitNornir(config_file="config.yaml")
        
        # define as credenciais para o nornir a partir das variaveis de ambiente importadas
        nr.inventory.defaults.username = username
        nr.inventory.defaults.password = password
        print('\nCredenciais importadas com sucesso\n')

        # executa task com nornir
        nr.run(task=get_interfaces)


if __name__ == "__main__":
    main()