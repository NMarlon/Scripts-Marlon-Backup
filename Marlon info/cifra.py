"""
A ideia aqui era pra desenvolver uma cifra para cifrar alguns textos como calendário que gostaria de adicionar aqui
Mas procurando sobre a cifra encontrei um site que já faz isso:
https://www.stringencrypt.com/ (String to Crypt) Ele converte uma string para um dado cifrado que só pode ser decifrado com um código específico

Exemplo:
"""
# # encrypted with https://www.stringencrypt.com (v1.4.0) [Python]
# # Róban = "Marlon"
# Róban = [ 0x004D, 0x0060, 0x0070, 0x006F, 0x006B, 0x006B ]
 
# for AvwUG in range(6):
#   UpiJZ = Róban[AvwUG]
#   UpiJZ ^= AvwUG
#   Róban[AvwUG] = UpiJZ
 
# Róban = ''.join(chr(UpiJZ & 0xFFFF) for UpiJZ in Róban)
 
# del AvwUG, UpiJZ
"""
Pesquise:
- Encrypt text online


"""


paraCifrar="""


"""
arquivoPadraoName="somentePessoaltorizado"

def decisao(caracteresEAcoes,frase):	
	cifraDecifra="?###?###?"
	#print(cifraDecifra in caracteresEAcoes)
	while(True):
		cifraDecifra = input(frase)
		for i in range(len(caracteresEAcoes)):
			if(cifraDecifra==caracteresEAcoes[i][0]):
				if(callable(caracteresEAcoes[i][1])):
					return caracteresEAcoes[i][1]()
				else:
					return caracteresEAcoes[i][1]
			
		print("Por favor digite '"+caracteresEAcoes[0][0]+"' ou '"+caracteresEAcoes[1][0]+"'")


def cifrar():
	print("")
	print("Em qual arquivo salvar")	
	nomeArquivo = input("Usar o arquivo padrão?(s) ou senão digite o nome do arquivo: ")
	adicionar= decisao([['s',True],['n',False]],"\nadicionar dados no mesmo aquivo?(s)\nou senão sobescrever os dados(n)? \n")


	if(len(nomeArquivo)<=1):
		print('arquivo usado: '+ )
	if(adicionar):
		add=input("\nO que deseja adicionar? \n")
		print("\n\nok!\n")


def decifrar():
	print("deu certo!")


decisao([['c',cifrar],['d',decifrar]],"você deseja cifrar(c) ou decifrar(d)? ")
