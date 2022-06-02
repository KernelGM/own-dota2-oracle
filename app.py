from os import system
from ids import conferir_id
from menu import menu
from itens import pegar_itens
from herois import pegar_meta
from counters import counter_pick
from partidas import amigos
from partidas import pegar_resumo
from partidas import pegar_todas_partidas
from partidas import pegar_partidas_recentes


conferir_id()

while True:
    menu()
    escolha = input()
    if escolha in '01':
        system("cls")
        pegar_resumo()
    elif escolha in '02':
        system("cls")
        pegar_meta()
    elif escolha in '03':
        system("cls")
        pegar_partidas_recentes()
    elif escolha in '04':
        system("cls")
        pegar_todas_partidas()
    elif escolha in '05':
        system("cls")
        pegar_itens()
    elif escolha in '06':
        system("cls")
        amigos()
    elif escolha in '07':
        system("cls")
        counter_pick()
    elif escolha in '08':
        system("cls")
        break
    else:
        system("cls")
        print('Escolha uma das opções!')
