'''from pyautogui import locateOnScreen
import os'''
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER


def counter_pick():
    tabela_counters = PrettyTable()
    tabela_counters.field_names = ['Qual herói deseja saber o counter pick? ']
    tabela_counters.align = "l"
    tabela_counters.set_style(DOUBLE_BORDER)

    print(tabela_counters)

    heroi = input()

    tabela_counters.field_names = [
        f'Os melhores picks contra {heroi.title()} são:'
    ]

    with sync_playwright() as playwright:
        browser = playwright.webkit.launch(headless=True)
        context = browser.new_context()

        page = context.new_page()

        page.goto("http://dotapicker.com/counterpick")

        page.fill("[placeholder=\"Search Hero\"]", heroi)

        with page.expect_navigation():
            page.press("[placeholder=\"Search Hero\"]", "Enter")

        html = page.content()

        context.close()
        browser.close()

    soup = BeautifulSoup(html, 'html.parser')
    span = soup.select_one('div.row')

    lista_completa = []

    for span in soup.select("span.inlineBlock.vAlignMid.ng-binding"):
        lista_completa.append(
            span.text.lstrip().rstrip().replace('\n\n', ' '))

    lista_melhores = []

    for c in lista_completa:
        if '+3' in c:
            lista_melhores.append(c)
        if '+2' in c:
            lista_melhores.append(c)

    for h in lista_melhores:
        tabela_counters.add_row([h])

    print(tabela_counters)


"""lista_todas_imagens = []
lista_counters = []
const = 0

local = os.listdir()

for file in local:
    if file.endswith('.png'):
        lista_todas_imagens.append(file)

while True:
    for i in lista_todas_imagens:
        imagens = locateOnScreen(i, grayscale=True, confidence=.7)
        if imagens is not None:
            if i.replace('.png', '') not in lista_counters:
                lista_counters.append(i.replace('.png', ''))
                const += 1
                print(lista_counters)
    if const > 4:
        break"""
