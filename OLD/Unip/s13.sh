#!/bin/bash
clear
# echo
echo 
echo "Informe até que valor positivo e maior que zero contar:"
	read valor;
	i=1
	while [ $i -le $valor ];
	do 
		echo "$i"
		((i=$i+1))
	done
