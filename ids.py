import os
import requests
import json
from bs4 import BeautifulSoup
from fake_headers import Headers
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER


def id_existe(id):
    try:
        a = open(id, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo_id(id):
    a = open(id, 'wt+')
    a.close


def ler_id(id):
    a = open(id, 'rt')
    global idsteam
    for linha in a:
        idsteam = linha


def deletar_id(id):
    os.remove(id)


if not id_existe(r'./arquivos/id.txt'):
    criar_arquivo_id('id.txt')
    global idsteam
    idsteam = input('Digite o seu Steam ID: ')
    a = open(r'./arquivos/id.txt', "w")
    a.write(idsteam)
else:
    ler_id(r'./arquivos/id.txt')
url = f'https://steamid.xyz/{idsteam}'
headers = Headers().generate()
resp = requests.get(url, headers=headers)
site = BeautifulSoup(resp.content, 'html.parser')
idsteam = site.find('input', type="text",
                    value=True).find_next().find_next().attrs

nome = site.find('input', type="text", value=True).find_next(
).find_next().find_next().find_next().attrs

idsteam = idsteam['value']
nome = nome['value']


def conferir_id():
    url = (f'https://api.opendota.com/api/players/{idsteam}/wl')
    data = requests.get(url)
    perfil = json.loads(data.text)
    tabela_apresentacao = PrettyTable()
    tabela_apresentacao.field_names = [f'Olá {nome}, bem-vindo ao Oracle!']
    win = perfil["win"]
    lose = perfil["lose"]
    try:
        winrate = (perfil['win']/(perfil['win']+perfil['lose']))*100
        tabela_apresentacao.add_row(
            [f'Atualmente você está com {win} vitórias e {lose} derrotas o que'
             f' resulta em {winrate:.2f}% de winrate.'])
    except ZeroDivisionError:
        print('Ocorreu um erro ao calcular o seu winrate.')
    tabela_apresentacao.align = "l"
    tabela_apresentacao.set_style(DOUBLE_BORDER)
    print(tabela_apresentacao)
