"""


Cynefin


- SIMPLES (Rel. Causa-efeito)
    - É o que é
- COMPLICADO (Rel. Causa-efeito, ordenados)
    - Precisa de um pré-conhecimento, portanto se torna simples sobre esse escopo
- COMPLEXO (Unknow, ordenado)
    - Precisa de Análise
- CAÓTICO (Unknow, impossível conhecer)
    - Não pode ser conhecido, reconhecer isso, mas tentar transformar para um problema caótico





"""
print("Start")

import pyautogui



eye = pyautogui.screenshot()
# eye.save(r'Path to save screenshot\file name.png')




# Find the coordinates of the icon on the desktop
icon_location = pyautogui.locateOnScreen('./img/teste.png')

# Click on the center of the icon
if icon_location is not None:
    icon_center = pyautogui.center(icon_location)
    pyautogui.click(icon_center)
    pyautogui.click(icon_center)
else:
    print("Icon not found") 