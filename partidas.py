import requests
import json
import time
from ids import idsteam
from herois import herois
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER
from cores import (
    red, green, cyan, yellow, reset_color, bold
)


def pegar_resumo():
    url = (f'https://api.opendota.com/api/players/{idsteam}/heroes')
    data = requests.get(url)
    resumo = json.loads(data.text)

    tabela_resumo = PrettyTable()
    tabela_resumo.field_names = ['Heroi', 'Winrate', 'Vitorias', 'Derrotas',
                                 'Total', 'Ultima Partida']
    tabela_resumo.set_style(DOUBLE_BORDER)

    for i in range(len(resumo)):
        try:
            winrate = f"{(resumo[i]['win']/resumo[i]['games'])*100: .1f}"
        except ZeroDivisionError:
            # Apenas ignorar o erro de divisão por 0
            ...
        vitorias = green + str(resumo[i]['win']) + reset_color
        derrotas = red + str(resumo[i]['games']-resumo[i]['win']) + reset_color
        total = bold + str(resumo[i]['games']) + reset_color
        ultima_partida = time.strftime(
            '%d-%m-%Y', time.localtime(resumo[i]['last_played']))
        for x in range(len(herois)):
            if int(resumo[i]['hero_id']) == herois[x]['id']:
                heroi = herois[x]['localized_name']
        if i > 19:
            break

        tabela_resumo.add_row(
            [f'{heroi:<20}', winrate, vitorias,
             derrotas, total, ultima_partida])

    print(tabela_resumo)


def pegar_partidas_recentes():
    url = (f'https://api.opendota.com/api/players/{idsteam}/recentMatches')
    data = requests.get(url)
    partidas = json.loads(data.text)

    tabela_recentes = PrettyTable()
    tabela_recentes.field_names = ['Herói', 'Resultado', 'K', 'D', 'A',
                                   'XP/min', 'G/min', 'DMG-Heróis',
                                   'DMG-Torres', 'Cura', 'Creeps',
                                   'Grupo', 'Tempo', 'ID Partida',
                                   'Hora e Data']

    for i in range(len(partidas)):
        xpmin = partidas[i]['xp_per_min']
        goldmin = yellow + str(partidas[i]['gold_per_min']) + reset_color
        dano_em_herois = partidas[i]['hero_damage']
        dano_em_torres = partidas[i]['tower_damage']
        cura_em_herois = partidas[i]['hero_healing']
        last_hits = partidas[i]['last_hits']
        tamanho_grupo = partidas[i]['party_size']
        id_partida = partidas[i]['match_id']
        duracao = int(partidas[i]['duration']/60)
        kills = partidas[i]['kills']
        deaths = partidas[i]['deaths']
        assists = partidas[i]['assists']
        data_horario = time.strftime(
            '%H:%M %d-%m-%Y', time.localtime(partidas[i]['start_time']))
        for x in range(len(herois)):
            if partidas[i]['hero_id'] == herois[x]['id']:
                heroi = herois[x]['localized_name']
        if partidas[i]['player_slot'] <= 127\
                and partidas[i]['radiant_win'] is True:
            resultado = green + 'Vitória' + reset_color
        elif partidas[i]['player_slot'] <= 127\
                and partidas[i]['radiant_win'] is False:
            resultado = red + 'Derrota' + reset_color
        elif partidas[i]['player_slot'] > 127\
                and partidas[i]['radiant_win'] is False:
            resultado = green + 'Vitória' + reset_color
        elif partidas[i]['player_slot'] > 127\
                and partidas[i]['radiant_win'] is True:
            resultado = red + 'Derrota' + reset_color

        tabela_recentes.add_row([f'{heroi:<20}', resultado, kills, deaths,
                                 assists, xpmin, goldmin, dano_em_herois,
                                 dano_em_torres, cura_em_herois, last_hits,
                                 tamanho_grupo, duracao, id_partida,
                                 data_horario])

    tabela_recentes.set_style(DOUBLE_BORDER)
    print(tabela_recentes)


def pegar_todas_partidas():
    url = (f'https://api.opendota.com/api/players/{idsteam}/matches')
    data = requests.get(url)
    partidas = json.loads(data.text)

    tabela_recentes = PrettyTable()
    tabela_recentes.field_names = ['Heróis', 'Resultados', 'K', 'D', 'A',
                                   'Grupo', 'Duração', 'ID da Partida',
                                   'Data e Horário']

    for i in range(len(partidas)):
        id_partida = partidas[i]['match_id']
        duracao = int(partidas[i]['duration']/60)
        kills = partidas[i]['kills']
        deaths = partidas[i]['deaths']
        assists = partidas[i]['assists']
        tamanho_grupo = partidas[i]['party_size']
        data_horario = time.strftime(
            '%d-%m-%Y %H:%M:%S', time.localtime(partidas[i]['start_time']))

        for x in range(len(herois)):
            if partidas[i]['hero_id'] == herois[x]['id']:
                heroi = herois[x]['localized_name']

        if partidas[i]['player_slot'] <= 127\
                and partidas[i]['radiant_win'] is True:
            resultado = green + 'Vitória' + reset_color
        elif partidas[i]['player_slot'] <= 127\
                and partidas[i]['radiant_win'] is False:
            resultado = red + 'Derrota' + reset_color
        elif partidas[i]['player_slot'] > 127\
                and partidas[i]['radiant_win'] is False:
            resultado = green + 'Vitória' + reset_color
        elif partidas[i]['player_slot'] > 127\
                and partidas[i]['radiant_win'] is True:
            resultado = red + 'Derrota' + reset_color

        if i > 100:
            break

        tabela_recentes.add_row([f'{heroi:<20}', resultado, kills, deaths,
                                 assists, tamanho_grupo, duracao, id_partida,
                                 data_horario])

    tabela_recentes.set_style(DOUBLE_BORDER)
    print(tabela_recentes)


def amigos():
    url = (f'https://api.opendota.com/api/players/{idsteam}/peers')
    data = requests.get(url)
    amigos = json.loads(data.text)

    tabela_amigos = PrettyTable()
    tabela_amigos.field_names = ['Nome', 'Total', 'Winrate',
                                 'Vitórias', 'Derrotas', 'ID', 'Última Juntos']

    for i in range(len(amigos)):
        nome = cyan + amigos[i]['personaname'] + reset_color
        winrate = f"{(amigos[i]['win']/amigos[i]['games'])*100: .1f}"
        total = amigos[i]['games']
        win = green + str(amigos[i]['win']) + reset_color
        lose = red + str(amigos[i]['games'] - amigos[i]['win']) + reset_color
        id_conta = amigos[i]['account_id']
        ultima_juntos = time.strftime(
            '%H:%M %d-%m-%Y', time.localtime(amigos[i]['last_played']))

        tabela_amigos.add_row(
            [nome, total, winrate, win, lose, id_conta, ultima_juntos])

        if i > 19:
            break

    tabela_amigos.align = "l"
    tabela_amigos.set_style(DOUBLE_BORDER)
    print(tabela_amigos)
