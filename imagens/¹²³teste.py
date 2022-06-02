import os
from pyautogui import locateOnScreen

lista_todas_imagens = []
lista_counters = []
const = 0

local = os.listdir()

for file in local:
    if file.endswith('.png'):
        lista_todas_imagens.append(file)

while True:
    for i in lista_todas_imagens:
        imagens = locateOnScreen(i, grayscale=True, confidence=.8)
        if imagens is not None:
            if i.replace('.png', '') not in lista_counters:
                lista_counters.append(i.replace('.png', ''))
                const += 1
                print(lista_counters)
    if const > 4:
        break
