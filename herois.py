import requests
import json
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER
from cores import (
    red, green, reset_color,
)


url = ('https://api.opendota.com/api/heroes')
data = requests.get(url)
herois = json.loads(data.text)


def pegar_meta():
    url = ('https://api.opendota.com/api/heroStats')
    data = requests.get(url)
    meta = json.loads(data.text)

    tabela_meta = PrettyTable()
    tabela_meta.field_names = ['Heroi', 'Arauto', 'Guardião', 'Cruzado',
                               'Arconte', 'Lenda', 'Ancestral', 'Divino',
                               'Imortal']

    for i in range(len(meta)):
        arauto = f"{(meta[i]['1_win']/meta[i]['1_pick'])*100:.1f}%"
        guardiao = f"{(meta[i]['2_win']/meta[i]['2_pick'])*100:.1f}%"
        cruzado = f"{(meta[i]['3_win']/meta[i]['3_pick'])*100:.1f}%"
        arconte = f"{(meta[i]['4_win']/meta[i]['4_pick'])*100:.1f}%"
        lenda = f"{(meta[i]['5_win']/meta[i]['5_pick'])*100:.1f}%"
        ancestral = f"{(meta[i]['6_win']/meta[i]['6_pick'])*100:.1f}%"
        divino = f"{(meta[i]['7_win']/meta[i]['7_pick'])*100:.1f}%"
        imortal = f"{(meta[i]['8_win']/meta[i]['8_pick'])*100:.1f}%"

        heroi = f"{meta[i]['localized_name']:<20}"

        if arauto < '50':
            arauto = red + arauto + reset_color
        elif arauto > '50':
            arauto = green + arauto + reset_color
        if guardiao < '50':
            guardiao = red + guardiao + reset_color
        elif guardiao > '50':
            guardiao = green + guardiao + reset_color
        if cruzado < '50':
            cruzado = red + cruzado + reset_color
        elif cruzado > '50':
            cruzado = green + cruzado + reset_color
        if arconte < '50':
            arconte = red + arconte + reset_color
        elif arconte > '50':
            arconte = green + arconte + reset_color
        if lenda < '50':
            lenda = red + lenda + reset_color
        elif lenda > '50':
            lenda = green + lenda + reset_color
        if ancestral < '50':
            ancestral = red + ancestral + reset_color
        elif ancestral > '50':
            ancestral = green + ancestral + reset_color
        if divino < '50':
            divino = red + divino + reset_color
        elif divino > '50':
            divino = green + divino + reset_color
        if imortal < '50':
            imortal = red + imortal + reset_color
        elif imortal > '50':
            imortal = green + imortal + reset_color

        tabela_meta.add_row([f'{heroi:<20}', arauto,
                             guardiao, cruzado, arconte, lenda, ancestral,
                             divino, imortal])

    tabela_meta.set_style(DOUBLE_BORDER)
    tabela_meta.reversesort = False
    tabela_meta.sortby = 'Heroi'

    print(tabela_meta)
