
"""
O objetivo desse projeto é desenvolver um tela impeça de ver o jogo de tempos em tempos, para eu treinar minha previsibilidade durante o jogo

- Útil para quem quer treinar memorizar o mapa ou algum conjunto de ações.
- Pode ser útil para quem quer aumentar o desafio em algum jogo específico
- Ajuda à treinar habilidade específica de reação
- Curiosamente ajuda à treinar para situações onde há lags leves.
a
- (--------------!!! FLASH WARNING !!!--------------) Esse programa tem uma tela piscante e pode não ser ok para todos. Pessoas com epilepsia ou sinais de convulsão não devem tentar usar isso.
- Essa é uma técnica avançada, vai ter melhor proveito quem JÁ CONHECE as mecânicas fundamentais do jogo em questão e já sabe das coisas que ocorrem. É algo para aumentar o desafio, talvez nãoo sirva para quando não se jogou o jogo antes e é um jogo novo


Como funciona:

É um programa que mostra um tela
- Ctrl + C no interpretador interrompe o programa

- Como funciona o tempo:

|--------tempo mínimo blind----------|--------tempo media blind---------|----------- Tempo Visivel ----------|---------- Tempo média visível --------| ---- Refaz o ciclo do começo...

- tempoMediaBlind, tempoMinimoBlind, tempoMediaVisivel e tempoMinimavisivel são as definições de tempo conforme mostrado acima, aumentando ou dimninuindo o mínimo de tempo de aparecimento que fica sempre ligado e o máximo de tempo que pode ser sorteado
	- tempo mínimo blind = 2500 ms é 2,5 segundos com a tela branca (no mínimo).
	- tempo media blind = 1500 ms é sorteado um número de 0 à 1500 que é somado ao "tempoMinimoBlind", ou seja, a duração de cegueira varia de 2,5 segundos à 4 segundos
	- a mesma coisa se aplica ao Tempo mínimo visível e tempo média visível
- Aconselhável deixar algum valor na "média" (pelo menos uns 150 pra não passar despercebido)


BUGS:
- (ainda não funciona com jogos que usam o mouse, somente com o teclado e controle, pois é uma janela normal do windows em fullscreen e não está programado a parte do clique transpassar essa

Melhorias à fazer:
- Ainda falta aarruamr uma forma de PARAR a execução com alguma tecla do teclado
- Opção de mutar o app selecionado quando a janela abrir (evitar feedback através do som)


Dicas:

- Não deixe o contador de blind muito rápido, a ponto de não fazer diferença (ex. Só um frame em blind só faz com que não veja um único frame de blind, isso QUANDO coincidir do blind cair exatamente nesse frame de transição de parado pra ação e esse frame ser fundamental pra alguma ação, fora isso é inútil deixar um tempo tão curto por isso.), experimente também não deixar o contador tão longo à ponto de ser impossível de prever onde o oponente vai estar, deve se encontrar um meio termo entre ambas, que haja momentos que precise de previsão e haja como você saber o resultado se deu certo ou não, isso não precisa ser sempre, mas pelo menos na maioria das vezes saber que conseguiu chegar onde esperava (Ainda vai ocorrer de não saber onde o oponente está, isso vai tornar o jogo mais na defensiva, mas não)

- Seguindo as regras acima, um 'tempo visível' muito curto junto com um 'tempo blind' longo faz com que seja difícil ou até mesmo impossível saber como o inimigo reagiu, isso pode tornar o jogo ou equivalente à completamente cego ou deixar muito na defensiva e pouco reativo. O objetivo é de exercitar a habilidade de PREVER o que está acontecendo

-

Dicas de Jogo:
- Siga em frente, continue tentando, esperar ver pra agir nunca é opção.

- Haverá casos onde não será possível reagir de forma excelente até vir o feedback, você pode deixar o blind mais rápido ou mesmo continuar jogando com isso (alguns caso isso pode ser impossível)
receber onde


- ESTE MÉTODO NÃO FUNCIONA EM JOGOS QUE EXIGAM ADQUIRIR INFORMAÇÃO OU QUE NÃO USAM HABILIDADE ATRAVÉS DO TEMPO (como jogos de TURNO), por exemplo: Se precisa ver as cartas, procurar alguma coisa no cenário, ler qualquer coisa, o movimento é por turno, a tela ocultando o que está procurando só vai atrapalhar.
- ESSE MÉTODO serve pra ajudar no "salto de fé", poder tomar atitudes sob situações onde não há informação disponível ainda. Ele te limita à ver algumas coisas e te força à agir em outras circunstâncias, evitando alguns vícios.



Dicas de apresentação do método:
- É possível gravar uma tela (somente o jogo) e outra com o que você está vendo (piscando). Para mostrar a tela do que as pessoas estão vendovocê pode configurar o gravador para reconhecer pou 


Árvore de Decisão de Uso do método (Blind Game):
- Ele pode ser útil para quem quer treinar algumas habilidades específicas de agilidade e treinar melhor as reações durante o jogo
- Ele pode ser útil pra desenvolver a habilidade de previsão (também conhecida como LEITURA ou READ em alguns jogos (Brawlhalla)
- Ele pode ser útil para memorizar melhor algumas coisas que são previsíveis após se ver
- Ele pode ser útil para quem queira jogar grnades partes do jogo de forma cega (Como forma de desafio ou treinar a memória para algo específico)
- Ele NÃO vai ser útil em jogos que exijam que você adquira um conhecimento específico durante o jogo para avançar (ex.: jogos de cartas, jogos turno
- Ele NÃO vai ser útil em jogos que se tem tempo para pensar na decisão (ex.: Jogos de Turno)


"""


import tkinter as tk
import time
import random
from pynput.keyboard import Key, Listener

import time
from pynput import keyboard
from multiprocessing import Process, Queue

from win32api import GetSystemMetrics
import win32con
import win32gui


"""import keyboard  # using module keyboard.6................................................

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' its pressed
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break



"""





##
##def on_press(key):
##         pass
##     #print('{0} pressed'.format(key))



#Brawlhalla Timer Ok
tempoMediaBlind=800#em milisegundos ms
tempoMinimoBlind=150#em milisegundos ms
tempoMediaVisivel=1.1 #em segundos (s)
tempoMinimavisivel=0.55 #em segundos (s)

#Castlevania symphony of the night
# tempoMediaBlind=1500#em milisegundos ms
# tempoMinimoBlind=100#em milisegundos ms
# tempoMediaVisivel=1.8 #em segundos (s)
# tempoMinimavisivel=0.15 #em segundos (s)


# Tony Hawk 2
##tempoMediaBlind=900#em milisegundos ms
##tempoMinimoBlind=330#em milisegundos ms
##tempoMediaVisivel=0.6 #em segundos (s)
##tempoMinimavisivel=0.15 #em segundos (s)

#Metal Gear Solid VR
# tempoMediaBlind=2000#em milisegundos ms
# tempoMinimoBlind=400#em milisegundos ms
# tempoMediaVisivel=1.2 #em segundos (s)
# tempoMinimavisivel=0.15 #em segundos (s)


#Marvel vs Capcom
##tempoMediaBlind=700#em milisegundos ms
##tempoMinimoBlind=150#em milisegundos ms
##tempoMediaVisivel=0.6 #em segundos (s)
##tempoMinimavisivel=0.1 #em segundos (s)

# Mega man X5
##tempoMediaBlind=900#em milisegundos ms (SOMENTE NÚMEROS INTEIROS)
##tempoMinimoBlind=150#em milisegundos ms (SOMENTE NÚMEROS INTEIROS)
##tempoMediaVisivel=0.33 #em segundos (s)
##tempoMinimavisivel=0.100 #em segundos (s)


#Quantas vezes vai rodar
quantasVezes=80 #Loop, quantas vezes vai mostrar a tela  (Se é sua primeira vez com isso use o valor 3, ele só ativará 3 vezes, então você vai testar o sistema antes de ter uma tela piscando indefinidamente, COMECE COM 3) (para ficar infinito coloque: True) (Padrão: 150)


#Outras Variáveis principais: 
useRefresh=False#Se True, habilita um Tempo de Descanso por loop (Padrão: True)
refreshRepeatFor=20 #Quantas vezes vai repetir até o próximo Refresh (Padrão de jogo: 10)
randomTimeRefreshInitial=40#Quanto vai variar pra mais em segundos o timeRefresh (deixe 0 para não variar; Padrão: 20)
timeRefresh=20#tempo em segundos de pausa (para refrescar a mente do esforço) (Padrão: 25)
#Segue abaixo o cálculo dessas variáveis:




#Processamento de variáveis:
randomTimeRefresh=randomTimeRefreshInitial*random.random()
randomTimeRefresh=int(randomTimeRefresh)
#print(randomTimeRefresh)
timeRefresh+= randomTimeRefresh
##timeRefresh*=1000




fetchKeyPress = 10
def on_release(key):
    global fetchKeyPress
    fetchKeyPress = key
    print("here!")
    if key == keyboard.Key.f8:
        fetchKeyPress = 0
        print('Exiting...')
        stop=True
        # Stop listener
        return False
    
def keyboardListener(q):
    print("aqui2")
    global fetchKeyPress
    prevKeyFetch = 10    # Keep track of the previous keyPress
    keyboard.Listener(on_release=on_release).start()
    while (fetchKeyPress):
        print ('Last Key Pressed was ', fetchKeyPress)
        # Fill the Queue only when a new key is pressed
        if (not (fetchKeyPress == prevKeyFetch)):
            q.put(fetchKeyPress)
        # Update the previous keyPress
        prevKeyFetch = fetchKeyPress
        time.sleep(0.25)
    print('Keybord Listener Terminated!!!')
    q.put('Terminate')


def oneSecondTimer(q):
    runner = True   # Runs the while() loop
    starttime = time.time()
    while (runner):
        print('\ttick')
        if (not q.empty()):
            qGet = q.get()
            print ('\tQueue Size ', q.qsize())
            print ('\tQueue out ', qGet)
            # Condition to terminate the program
            if (qGet == 'Terminate'):
                # Make runner = False to terminate the While loop
                runner = False
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))
    return False

##q = Queue()
##p1 = Process(target=oneSecondTimer, args=(q,),stop=False)
##?
refreshRepeatForCount=0

stop= False
##while(True and not stop):
while(not stop and (quantasVezes>0  or useRefresh)):
        try:
                root = tk.Tk()
                root.attributes("-fullscreen", True, "-topmost", True, "-disable", True)
                root.title('Blind Game')
		# hwnd = win32gui.FindWindow(None, "Blind Game") # Getting window handle
		# #hwnd = root.winfo_id() getting hwnd with Tkinter window
		# #hwnd = root.GetHandle() getting hwnd with wx windows
		# lExStyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
		# lExStyle |=  win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED
		# win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE , lExStyle
                duracaoBlind=int(random.random()*tempoMediaBlind+tempoMinimoBlind)
                time_interrupt = duracaoBlind # Time screen is active in ms

                root.after(time_interrupt, root.destroy)


                root.mainloop()
                duracaoVendo = (random.random()*tempoMediaVisivel+tempoMinimavisivel)
                time.sleep(duracaoVendo)
                if useRefresh and refreshRepeatFor<=refreshRepeatForCount:
                    randomTimeRefresh=randomTimeRefreshInitial*random.random()
                    randomTimeRefresh=int(randomTimeRefresh)
                    time.sleep(timeRefresh)
                    refreshRepeatForCount=0
                else:
                    refreshRepeatForCount+=1
##                def on_release(key):
##                        print('{0} release'.format(key))
##                        if key == Key.f8:
##                                stop=True
##                        if key == Key.esc:
##                        # Stop listener
##                                return False
##
##                # Collect events until released
##                with Listener(
####                         on_press=on_press,
##                         on_release=on_release) as listener:
##                     listener.join()



                quantasVezes+=1


        except KeyboardInterrupt:
                print("sys: exit by user interrupting")
                root.after(time_interrupt, root.destroy)
                root.mainloop()
                break
print("Exit Blind Game")
