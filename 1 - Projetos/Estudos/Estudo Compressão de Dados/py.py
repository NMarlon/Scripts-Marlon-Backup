def isso(valor,dist):
	if(dist==0):
		return ''
	else:
		return valor+isso(valor,dist-1)


print(isso('1',3))



"""





...
"




"""