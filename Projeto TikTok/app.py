# Passos manuais em sequência, depois tornar cada passo em um codigo
# Quais são os passos manuais

# navegar até o site https://www.tiktok.com/
import webbrowser
import pyautogui
from time import sleep

webbrowser.open('https://www.tiktok.com/')
sleep(5)

# #clicar em login
pyautogui.click(1796, 179, duration=2)
sleep(5)

# clicar em logar com email
pyautogui.click(1365, 471, duration=2)
sleep(2)


# Clicar em logar com email e senha
pyautogui.click(1518, 408, duration=2)
sleep(2)

#


# clicar no campo do email e Digitar acesso
pyautogui.click(1346, 443, duration=2)
sleep(2)
pyautogui.write()
sleep(2)
pyautogui.click()  # colocar cordenada da senha
sleep(2)
pyautogui.write()
sleep(2)

pyautogui.click()  # colocar a posição do log in


# Navegar até a pagina (https://www.tiktok.com/@017.noc)
webbrowser.open('https://www.tiktok.com/@017.noc')

# cliccar na postagem mais recente
pyautogui.click()  # passa a coordenada do primeiro video


# Verificar se video já foi curtido
# faz um print somente do coração
# Deixar na mesma pasta
imagem = pyautogui.locateOnScreen('')  # colocar o nome da imagem

for video in range(15):
    if imagem:
        # pule para o proximo video
        pyautogui.press('down')
    else:
        # codigo para curtir o video
        pyautogui.click()  # Passar a coordenada do like
        pyautogui.press('down')


# Se foi curtido passar para próximo video=
# Se não foi curtido, curtir este video e passar para próximo video
# Repetir por quantas vezes quiser


# https://www.youtube.com/watch?v=AFffT1qmuGs
