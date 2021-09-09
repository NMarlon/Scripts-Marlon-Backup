import json


d="110010011001000011010001111100111100100000101010000110011111100100011000000000111"



class compact:
	def __init__(self):
		isso=True
	def r(valor,numeroDeVezes):#Repetição
		if numeroDeVezes==0:
			return ""
		else: 
			return valor+self.r(self.valor,self.numeroDeVezes-1)
		return 
	def PA(valor_inicial,valor_final,jump):#PA Progressão Aritimética
		if(valor_final<=valor_inicial):
			return
		else:
			return 


def ondeTem(disso):
	print("[",end="")
	first=False
	for i in range(len(d)-1):
		if(d[i+1]==disso):
			print(", "*first +str(i+1),end="")
			first=True

			
	print("]")
	print("")
"""

def delta(disso,repeticao):
	if(repeticao>1):
		valor=int(disso[repeticao])
		valor=str(valor-int(disso[repeticao-1]))
		return valor + ', ' + delta(disso,repeticao-1)
	else:
		return '' #disso[0]
#total: 110010011001000011010001111100111100100000101010000110011111100100011000000000111
#110010011001000011010001111100111100100000101010000110011111100100011000000000111

binario='1100' 
isso=int(len(binario))-1
print(delta(binario,3))
"""





	# for i in range(disso)-1:
	# 	disso[i]-disso[i+1]:


# ondeTem("0")
# ondeTem("1")
