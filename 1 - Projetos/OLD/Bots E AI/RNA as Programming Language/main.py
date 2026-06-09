"""
Usar Redes Neurais como forma de programação.

A ideia desse projeto é adquirir luz e iluminar a mente para a forma como o cérebro trabalha.

Poderão ser usados modelos OTIMIZADOS matematicamente para o caso e esclarescimento e definição melhor,
    mas ainda é bom que tenha um modelo mais similar ao cérebro para se ter algo autônomo trabalhando por trás dos dados


Também será por meio de INPUTS e os "return" serão os OUTPUTS, o processamento será os próprios neurônios no "tudo ou nada".





BÔNUS:
- Identificar uma forma de visualizar a coisa do começo ao fim e com esse conhecimento usar para saber o fim e começo de algo.
- 

"""




class net:
    def __init__(self):
        print("starting net...")



class brain:
    entrada=[]
    pesos=[]
    numSaidas=1

    def __init__(self,entrada,numSaidas):
        self.entrada=entrada
        self.numSaidas=numSaidas
        print("starting brain... ")

    def action(self):
        entrada=self.entrada
        saida = entrada[0]
        return saida

    def train(WhatAreYouLookingFor):
        print("brain.train() - Start train...")


        print("brain.train() - Ended training.")




agent=brain([0,1],1)
#[0,1] = 1 porque 0 + 1 = 1





#Realoque o seguinte em seu respectivo código:
# Aprendizado

# Aplicação do Aprendizado

# Resposta





#Associar o símbolo à um valor
a = 1
b = 1
w1 = 1
w2 = 1
#funcao = ((a * w1 + b * w2 )>0) * 1 +((a * w1 + b * w2) <= 0) * -1;
funcao = ((a * w1 + b * w2 )>0) * 1 +((a * w1 + b * w2) <= 0) * -1;
while(True):
    print(a)
    print(b)
    w1=float(input("valor de w1: "))
    w2=float(input("valor de w2: "))
    funcao = a * w1 + b * w2 
    print("funcao retorna: "+funcao)
    


print(funcao)
"""
Alguns desafios à vencer:
- Um simples if
    - Se for 'a' faz x()
    - Se for 'a' E 'b' faz x()
    - Se for 'a' OU 'b' faz x()
    - Se não for nem 'a' e nem 'b' faz x()
- If encadeados
- Programar uma calculadora simples (somente com uso da rede neural, sem auxílio de operandos)
- Programar um agente para decidir entre comer um fruto ou tocar no espinho (v1 - decisão de doce-amargo)
    - v2 o espinho é doce, mas é letal, o fruto é amargo, mas mantém a vida.7
- Programar de forma que SOZINHO ele aprenda à vencer os desafios acima 
    - na "Decisão de Doce-amargo" v1 ele se apegar ao doce e fugir do amargo por causa do sabor,
    - na v2 deve ser dada que o espinho->mata e fruto->vive, e ele fica por decidir se vai ou não "cair na armadilha" de se matar pelo falso doce ou suportar o amargo para viver.
- Identificar objetos por imagens
- Identificar objetos por vídeo
- Identificar objetos por áudio
- Executar uma sequência de ações pré-determinadas
- Dias da semana mais 7 https://dev.to/alanfabricio/iniciante-javascript-desafio-avancando-dias-praticando-arrays-loops-e-funcoes-2a8p
- Identificar as coisas que estão acontecendo num momento.
- 

"""