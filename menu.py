from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER


def menu():
    tabela_menu = PrettyTable()
    tabela_menu.field_names = ['Opções']
    tabela_menu.add_rows(
        [
            ['[01] Heróis Mais Jogados'],
            ['[02] Meta de Heróis'],
            ['[03] Partidas Recentes'],
            ['[04] Ultimas 100 Partidas'],
            ['[05] Ver Builds Recomendadas'],
            ['[06] Lista de Amigos'],
            ['[07] Counter Picks'],
            ['[08] Fechar Programa'],
        ]
    )
    tabela_menu.align = "l"
    tabela_menu.set_style(DOUBLE_BORDER)
    print(tabela_menu)
