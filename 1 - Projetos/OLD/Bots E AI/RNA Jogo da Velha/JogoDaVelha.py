import random as rd
import json
import pickle

# obj0, obj1, obj2 are created here...

# Saving the objects:
with open('RNAmind.pkl', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([obj0, obj1, obj2], f)

# Getting back the objects:
with open('RNAmind.pkl') as f:  # Python 3: open(..., 'rb')
    obj0, obj1, obj2 = pickle.load(f)


def menu():
    continuar=1
    while continuar:
        continuar = int(input("0. Sair \n"+
                              "1. Jogar novamente\n"))
        if continuar:
            game() 
        else:
            print("Saindo...")

def game():
    jogada=0

    while ganhou() == 0:
        print("\nJogador ", jogada%2 + 1)
        exibe()
        linha  = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if board[linha-1][coluna-1] == 0:
            if(jogada%2+1)==1:
                board[linha-1][coluna-1]=1
            else:
                board[linha-1][coluna-1]=-1
        else:
            print("Nao esta vazio")
            jogada -=1

        if ganhou():
            print("Jogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas")

        jogada +=1
    
def ganhou():
    #checando linhas
    for i in range(3):
        soma = board[i][0]+board[i][1]+board[i][2]
        if soma==3 or soma ==-3:
            return 1

    for i in range(3):
        soma = board[0][i]+board[1][i]+board[2][i]
        if soma==3 or soma ==-3:
            return 1

    diagonal1 = board[0][0]+board[1][1]+board[2][2]
    diagonal2 = board[0][2]+board[1][1]+board[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1
    return 0

def exibe():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')

        print()
                


def write_file():
    config = open('rna_know.py', 'w')
    config.write(f"""
File has been overwrite
funny = "LOL"
        """)


"""    
    file = open(“testfile.txt”,”w”) 
     
    file.write(“Hello World”) 
    file.write(“This is our new text file”) 
    file.write(“and this is another line.”) 
    file.write(“Why? Because we can.”) 
     
    file.close() 
"""
def write_open():
    print("")

with open("rna_know.py", "r") as txt_file:
        return txt_file.readlines()



print("")

def loading(resource):
    print("Loading... "+resource)


"""
# COMMENTS

Número de Camadas (colocadas manualmente (por enquanto))



"""

class RNA:    
    def __init__(self, arr_num_nodes_cam, camadas,modo_manual):                    
        if(len(arr_num_nodes_cam)):
            print("ERRO! Número de camadas da RNA diferente do número de camadas na array descritora de camadas (arr_num_nodes_cam), colocando o padrão do último...")
        

        amplitude_pesos=2
        shift_amplitude_pesos=0
        

        nodos_posicoes={

        }

        pesos_json= {
            "nod_e":"0",#id nodo de saída
            "nod_s":"1",
            "peso":0.5 
        }

        pesos=[]
        for i in range(0,camadas):
            pesos.append([])
            for j in range(0,arr_num_nodes_cam[i]):
                pesos[i].append(rd.random()*amplitude_pesos+shift_amplitude_pesos)

        
     

    def start(self):
        print("Loading... Opening a new RNA")  


class AI:
    def __init__(self, name, age):
        loading("Starting AI...")
        self.name = name
        self.age = age
        ai_here=RNA([1,2],4,True)

    def start(self):
        print("Hello my name is " + self.name)    
    def rna_turn():
        loading("AI Thinking...")


    def rna_know():
        write_file()



rna = AI("John", 36)
print("")
rna.start()
print("")
print("")
write_file()
write_open()
print(funny)



board= [ [0,0,0],
         [0,0,0],

        ]
menu()

