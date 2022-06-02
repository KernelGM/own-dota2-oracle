import requests
import json
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER


def pegar_itens():
    url = ('https://api.opendota.com/api/heroes')
    data = requests.get(url)
    herois = json.loads(data.text.lower())

    with open(r'./arquivos/item_ids.json', 'r', encoding='utf8') as t:
        tabela_itens = json.load(t)

    tabela = PrettyTable()
    tabela.field_names = ['Melhores itens para cada herói!']
    tabela.add_row(['De qual herói você deseja saber a build? '])
    tabela.set_style(DOUBLE_BORDER)
    print(tabela)

    selecionado = input('').lower()

    for x in range(len(herois)):
        if selecionado in herois[x]['localized_name']:
            id = herois[x]['id']
            nome = herois[x]['localized_name']
            tabela = PrettyTable()
            tabela.field_names = ['Você escolheu o herói:']
            tabela.add_row([f'{nome.title()}'])
            tabela.set_style(DOUBLE_BORDER)
            print(tabela)

    url_itens = (f'https://api.opendota.com/api/heroes/{id}/itemPopularity')
    data_itens = requests.get(url_itens)
    itens = json.loads(data_itens.text)

    start = []
    early = []
    mid = []
    late = []

    for i in itens['start_game_items'].keys():
        start.append(i)

    for i in itens['early_game_items'].keys():
        early.append(i)

    for i in itens['mid_game_items'].keys():
        mid.append(i)

    for i in itens['late_game_items'].keys():
        late.append(i)

    itens_start = []
    itens_early = []
    itens_mid = []
    itens_late = []

    for keys in tabela_itens.keys():
        for valor in range(len(start)):
            if start[valor] == keys:
                itens_start.append(
                    tabela_itens[keys].title().replace('_', ' '))

    for keys in tabela_itens.keys():
        for valor in range(len(early)):
            if early[valor] == keys:
                itens_early.append(
                    tabela_itens[keys].title().replace('_', ' '))

    for keys in tabela_itens.keys():
        for valor in range(len(mid)):
            if mid[valor] == keys:
                itens_mid.append(tabela_itens[keys].title().replace('_', ' '))

    for keys in tabela_itens.keys():
        for valor in range(len(late)):
            if late[valor] == keys:
                itens_late.append(tabela_itens[keys].title().replace('_', ' '))

    tabela_itens_start = PrettyTable()
    tabela_itens_start.add_column("Itens Iniciais", itens_start)
    tabela_itens_start.align = "l"
    tabela_itens_start.set_style(DOUBLE_BORDER)

    tabela_itens_early = PrettyTable()
    tabela_itens_early.add_column("Itens Começo", itens_early)
    tabela_itens_early.align = "l"
    tabela_itens_early.set_style(DOUBLE_BORDER)

    tabela_itens_mid = PrettyTable()
    tabela_itens_mid.add_column("Itens Meio", itens_mid)
    tabela_itens_mid.align = "l"
    tabela_itens_mid.set_style(DOUBLE_BORDER)

    tabela_itens_late = PrettyTable()
    tabela_itens_late.add_column("Itens Final", itens_late)
    tabela_itens_late.align = "l"
    tabela_itens_late.set_style(DOUBLE_BORDER)

    print(tabela_itens_start)
    print(tabela_itens_early)
    print(tabela_itens_mid)
    print(tabela_itens_late)
