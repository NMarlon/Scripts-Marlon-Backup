"""

Projetos des estudo:

- https://www.quora.com/unanswered/Is-it-possible-to-directly-compare-the-mutual-information-of-weights-representations-by-different-neural-networks-even-if-they-have-different-hyperparameter-architectures?q=weight%20neural%20network%20b

- (PODA SINÁPTICA, peso 0 no cérebro) https://www.quora.com/Apart-from-zero-weights-are-there-any-neural-network-types-that-take-into-account-a-process-similar-to-synaptic-pruning-in-the-human-brain?q=weight%20neural%20network%20brain

-("pesos negativos" no cérbro) https://www.quora.com/What-is-the-physical-significance-of-negative-synaptic-weights-in-neural-networks-How-is-it-implemented-in-the-human-brain?q=weight%20neural%20network%20brain


- (Paul King resposta, Várias coisas que ainda precisam se desenvolver na RNA em relação à biológica) https://www.quora.com/What-do-we-know-about-real-neural-networks-that-hasnt-yet-been-applied-in-Machine-Learning


- Depp Q Learning https://github.com/devsisters/DQN-tensorflow



simular um disparo neural temporal: 
os disparos do frame seguinte sofrem um decréscimo na intensidade.

"""


import random as rd
import json
import math
from math import e
import re



def loading(resource):
    print("Loading... "+resource)


def error(name):
    print("")
    print("ERRO!!! "+name)
    print("")
    print("")

def try_again_error():
    main()


class RNA:    

    def reset_pesos(pesos):
        procura_por_json = json.loads(pesos)
        if "json" in procura_por_json:
            print("Key exist in JSON data")
            print(student["name"], "marks is: ", student["percentage"])
        else:
            print("Key doesn't exist in JSON data")



    def __init__(self, arr_num_nodes_cam, camadas,modo_manual,array_parameters):                                            

        loading("Opening a new RNA")  

        if(len(arr_num_nodes_cam)):
            print("ERRO! Número de camadas da RNA diferente do número de camadas na array descritora de camadas (arr_num_nodes_cam), colocando o padrão do último...")
        
            
        #variaveis
        ##Alteração necessária
        amplitude_pesos=self.array_parameters[0] #default: 10
        shift_amplitude_pesos=self.array_parameters[1] #default: 0
        taxa_de_aprendizado=self.array_parameters[2] #default: 0.05
        alfa=self.array_parameters[3] #default: 0.01
        tipo_do_disparo=self.array_parameters[4] #(default: 0)#ReLU

        #Declaração de variáveis
        #constantes
        ##Não alterar!
        neural_timer=0 



        nodos_posicoes={

        }

        pesos_json= """{
            "json":True,
            {
                "nodo_id":0, #id
                "camada":0,#camado do nodo
                "connect_to":{['']}

                "nod_e":"0",#id nodo de saída
                "nod_s":"1",
                "peso":0.5
            },
            {
                "nod_e":"0",#id nodo de saída
                "nod_s":"2",
                "peso":0.5
            },
        }"""




        pesos=[]
        reset_pesos(pesos)

    def disparo(tipo, entrada):
        #https://en.wikipedia.org/wiki/Activation_function#cite_note-ReferenceA-4
        tipo = tipo.islower()
        tipo = re.sub(r"\s+", "", tipo)
        if(tipo == "relu" || tipo == 0):
            if entrada<0:
                return 0#saida
            else:
                return entrada
        elif (tipo == "identity" || tipo == "indentico" || tipo == 1):
            return entrada
        elif (tipo == "sig" || tipo == "sigmoide"|| tipo == "sigmoid" || tipo == 2):
            return 1/(1+(e**(-entrada)))
        elif (tipo =="tan" || tipo=="tangente" || tipo == 3):
            return ((e**entrada)-(e**(-entrada)))/((e**entrada)+(e**(-entrada)))
        elif (tipo=="gelu" || tipo == 4):
            error("Função ainda não está pronta! pegando a funcao 'identica'")
            return entrada#(entrada*(1+e))/2
            return math.log(1 + (e**entrada),10)
        elif (tipo == "elu" || tipo == 6):
            if(entrada <= 0):
        elif (tipo=="softplus" || tipo == 5):
                return self.alfa*((e**entrada)-1)
            else:
                return entrada
        elif (tipo == "selu" || tipo==7):

            error("Função ainda não está pronta! pegando a funcao 'identica'")
            return entrada#(entrada*(1+e))/2
        elif(tipo == "lrelu" || tipo =="leakyrelu" || tipo==8):
            if(entrada<0)
            else:
                return entrada
        elif(tipo == "prelu" || tipo == 9)::
                return 0.01*entrada
            if (entrada<0):
                return self.alfa*entrada
            else:
                return entrada
        elif(tipo=="silu"||tipo==10):
            return entrada/(1+(e**(-entrada)))
        elif(tipo=="gaussiana"||tipo=="gaussian"|| tipo=="gaus"|| tipo==11):
            return e**((-entrada)**2)         

        else:
            error("Função não encontrada")
            try_again_error()
            return 0



    def erro(saida,entrada,peso_atual):
    	return erro_valor_constante(saida,entrada,peso_atual)

    def erro():
        fix_this=1



    def erro_valor_constante(saida,entrada,peso_atual):#input é uma array porque são os outputs da RNA, como há mais de 1 output, usa-se uma array
	    constante_sd = 1.23123123123123
		return peso_atual + ((((saida - constante_sd)**2))/2) * entrada * self.taxa_de_aprendizado #retorna novo peso


    def train(self):
        loading("Treinando...")
class AI:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        ai_here=RNA([1,2],4,True,[2,0,0.05,0.01,"elu"])

    def start(self):
        print("Hello my name is " +     selfself.name)    
    def rna_turn():asd
        print("rna_think")


    def rna_know():
        write_file()


rna = AI("John", 36)
print("")
rna.start()
print("")