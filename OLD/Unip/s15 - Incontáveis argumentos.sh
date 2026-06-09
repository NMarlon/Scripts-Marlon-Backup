##!/bin/bash
clear
if [ $# -lt 1 ];
	then 
	echo "Precisa fornecer pelo menos 1 argumento!"
	exit 1
fi
	echo "Numero de argumentos passados: $#"
	i=0
	for argumento in $*
	do
	i=$(($i+1))
	echo "Argumento $i passado: $argumento"
	done
	
