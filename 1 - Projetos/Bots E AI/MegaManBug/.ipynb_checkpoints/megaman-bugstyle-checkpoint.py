"""
MegaMan BugStyle (JARVIS)


O objetivo é fazer algum tipo de IA que me entenda e automatize tudo que for capaz de se ter um input com mouse e teclado. 
 (FUTURAMENTE): Prentendo ampliar isso pra que o bot tenha acesso aos poucos ao código da SO. Permitindo fazer compressões de dados (LINUX), melhorias no desempenho (esse é o foco maior) e ajuste dos mais variados bugs. (anti-virus não é mais meu foco, porque os que se tem hoje são excelentes)


Objetivos e informações:
- Deve ser leve o suficiente pra CPU e RAM pra rodar num Dual-Core
- Não é necessário que tenha uma economia muito alta no HD, basta que caiba dentro de 10~50Gb, porém quanto mais compacto, melhor.




Opciones opcionais que imagino:
- Dividir funções específicas para usar mais tarde
- 





Dar V e F para tudo que é informação que ele ver


"Só é possível de se adquirir verdadeira sabedoria observando todas as possibilidades de um meio"
   

"""

import pyautogui

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'./screenshot_test.png')
