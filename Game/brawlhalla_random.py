
num_caracteres_max=3 #no ataque, combinador e tecnica, delimita o número de caracteres para um número padrão. (SE PASSAR IRÁ CORTAR)
#=== COLOQUE AQUI OS VALORES QUE PREFERIR
ataques = ["C","X","Z"]
combinadores = ["->","V","<-","J", "" ] 
tecnica = ["Atk", "Bck", "Trp" ]

show=[True,True,True]#mostrar ou ocultar os Ataques, Combinadores ou tecnicas respectivamente (False para esconder, True para mostrar)

mostrar_divisor=True#Linha divisora, mostra (True) ou esconde (False) um divisor entre as linhas 

contador_max=5 #O máximo por linha


tempo_por_linha=1#EM SEGUNDOS

#=== VISUAL ===
pular_linhas_num=0# PULO DE LINHAS, quantas linhas vai pular (deixe 0 para não pular linha, (Padrão: 0))
pular_linhas_escritas=1#Linhas à manter, número de linhas à repetir antes de pular (padrão: 1)



#=======LINHAS DO SISTEMA============
import random as rd
import time
import sys


#Black        0;30     Dark Gray     1;30
#Red          0;31     Light Red     1;31
#Green        0;32     Light Green   1;32
#Brown/Orange 0;33     Yellow        1;33
#Blue         0;34     Light Blue    1;34
#Purple       0;35     Light Purple  1;35
#Cyan         0;36     Light Cyan    1;36
#Light Gray   0;37     White         1;37

class bcolors:
	OKBLUE='\033[94m'
	HEADER='\033[95m'
	OKCYAN='\033[96m'
	OKGREEN='\033[92m'
	WARNING='\033[93m'
	FAIL='\033[91m'
	ENDC='\033[0m'
	BOLD='\033[1m'
	UNDERLINE='\033[4m'
	PUR='\033[0;35m'
	RED='\033[0;31m'
	YEL='\033[1;33m'
	GRE='\033[0;32m'
	NC='\033[0m'
	CYA='\033[0;36m'
	LGR='\033[0;37m'

pular_linhas_start=0
pular_linhas=pular_linhas_start

contador=1
#==========END LINHAS DO SISTEMA================


#======CODIGO===================== Funções =======

def fill_with_space(num_caracteres_max,array):
	i=0
	array2=[]
	while len(array)>i:
		if len(array[i]) > num_caracteres_max:
			array2.append(array[i][0:num_caracteres_max])
		else:
			array2.append(array[i].ljust(num_caracteres_max))
		i+=1
	return array2

ataque = fill_with_space(num_caracteres_max,ataques)
combinador = fill_with_space(num_caracteres_max,combinadores)
tecnica = fill_with_space(num_caracteres_max,tecnica)

#print(ataque)

print("")


def jogar_dado(dist):
	return round(rd.random()*dist)-1

#=========== FUNCAO PRINCIPAL ===============

while True:

	print("| ",end="")

	dado=jogar_dado(len(ataque))#apenas um número aleatório
	dado2=jogar_dado(len(tecnica))
	dado3=jogar_dado(len(combinador))

	if show[0]:
		print(bcolors.YEL+str(ataque[dado]),end="")
	if show[1]:
		print(str(combinador[dado3]),end="")
	
	print(" ",end="")


	if show[2]:
		print(str(tecnica[dado2])+bcolors.ENDC,end="")


	print(bcolors.FAIL+" | "+bcolors.ENDC,end="")
	#print("enter1")
	if contador == contador_max:
		contador=1
		pular_linhas+=1
		time.sleep(tempo_por_linha)
		print("")
		if mostrar_divisor:
			print("-"*((num_caracteres_max*((show[0]*1)+(show[1]*1)+(show[2]*1))*contador_max)+6*contador_max))
	else:
		contador+=1

	if pular_linhas_escritas  == pular_linhas:
		pular_linhas=pular_linhas_start
		j=0		
		while pular_linhas_num > j:
			print("")
			j+=1
	
		

	