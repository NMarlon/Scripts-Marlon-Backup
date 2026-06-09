#!/bin/bash
#Autor: Marlon Rebello Viana
#Data: 23/04/2021
#Algoritmo que calcula: soma, subtração, multiplicação,
#divisão, a raiz quadrada 

echo
echo
echo
echo "CALCULADORA UNIP LINUX"
echo "Desenvolvido por:"
echo "Marlon F0965J2"
echo "e Rafael"
echo "Unip Anchieta Campus III - CC4P39"

#Black        0;30     Dark Gray     1;30
#Red          0;31     Light Red     1;31
#Green        0;32     Light Green   1;32
#Brown/Orange 0;33     Yellow        1;33
#Blue         0;34     Light Blue    1;34
#Purple       0;35     Light Purple  1;35
#Cyan         0;36     Light Cyan    1;36
#Light Gray   0;37     White         1;37


#echo -n "teste: "
#read teste
#read teste






PUR='\033[0;35m'
RED='\033[0;31m'
YEL='\033[1;33m'
GRE='\033[0;32m'
NC='\033[0m'
CYA='\033[0;36m'
LGR='\033[0;37m'


valor=""
mc=true
color_mc="${GRE}"
menu ()
{

echo
echo
echo "digite o número correspondente abaixo"
echo -e "${GRE}1${NC} - Simples"
echo -e "${GRE}2${NC} - Científica "
echo -e "${GRE}3${NC} - Salvar última resposta? $color_mc$mc${NC}"
echo -e "${GRE}0${NC} - Sair "

#echo "Escolha uma das opções acima:  "
echo -e "Escolha uma das opções acima:  ${GRE}"
read  opcao
echo -e "${NC}"

case $opcao in
    1) ordem ;;
    2) cientificaStart ;;   
	3) configuracoes ;;
    0) exit ;;
esac


}

configuracoes ()
{
if [ "$mc" == "true" ]
then
	mc=false
	color_mc="${RED}"
else
	mc=true
	color_mc="${GRE}"
fi
menu

}

ordem ()
{
echo 

echo -e  "${GRE}1${NC} - número1 + número2"
echo -e  "${GRE}2${NC} - número1 número2 +"
echo -e  "${GRE}3${NC} - + número1 número2"
echo -e  "${GRE}0${NC} - Voltar"
echo -e  "escolha a ordem padrão de digitação acima: ${GRE}"
read ordem
echo -e "${NC}"

if [ "$ordem" == "0" ]
then
	menu
elif [ "$ordem" != "1" ] && [ "$ordem" != "2" ]  && [ "$ordem" != "3" ] 
then
	ordem
fi

simples
}


operador_verificador ()
{

echo -e  "Digite ${GRE}0${NC} para voltar ou..."
echo -e  "Digite um dos operadores (${CYA}+-/*${NC})"
echo -e " ou use (${CYA}^${NC}) para exponencial (${RED}Somente usar números inteiros no exponte (segundo valor)${NC})"	
echo -e " ou use (${CYA}sqrt${NC}) para raiz quadrada (${RED}O primeiro valor será desprezado${NC}):${CYA}"
read op
echo -e "${NC}"
if [ "$op" != "+" ] &&  [ "$op" != "-" ] &&  [ "$op" != "/" ] &&  [ "$op" != "*" ] &&  [ "$op" != "^" ] &&  [ "$op" != "0" ] && [ "$op" != "sqrt" ]
then
	echo
	echo -e "${RED}Digite um operador váĺido!${NC}"
	operador_verificador
fi

}

simples ()
{
sqrtC=""
space=" "
#valor1="$valor"
if [ "$ordem" ==  "1" ]
then
	echo
	echo -e "Digite o primeiro valor: ${CYA}"
	

	if [ -z $valor  ] || [ "$mc" == false ]
	then
		read valor1
	else
		read -e -p "" -i "$(echo "$valor + 0.0" | bc -l)" valor1
	fi

	echo -e  "${NC}"
	operador_verificador
	if [ "$op" == "0" ]
	then
		echo
		echo -e  "${NC}"
		menu
	fi
	echo -e  "${NC}"
	echo -e  "Digite o segundo valor: ${CYA}"
	read valor2
	echo -e  "${NC}"
elif [ "$ordem" ==  "2" ]
then
	echo
	echo -e  "Digite o primeiro valor: ${CYA}"
	
	if [ -z $valor  ] || [ "$mc" == false ]
	then
		read valor1
	else
		read -e -p "" -i "$(echo "$valor + 0.0" | bc -l)" valor1
	fi

	echo -e  "${NC}"
	echo -e  "Digite o segundo valor: ${CYA}"
	read valor2
	echo -e  "${NC}"
	echo -e  "Digite ${GRE}0${NC} para voltar ou..."
	echo -e  "Digite um dos operadores (${CYA}+-/*${NC}) ou use (${CYA}^${NC}) para exponencial :${CYA} "	
	read op
	if [ "$op" == "0" ]
	then
		echo
		echo -e  "${NC}"
		menu
	fi
	echo -e  "${NC}"
else
	echo

	operador_verificador
	if [ "$op" == "0" ]
	then
		echo
		echo -e  "${NC}"
		menu
	fi
	echo -e  "${NC}"

	if [ "$op" != "sqrt" ]
	then
		echo -e "Digite o primeiro valor: ${CYA}"
		if [ -z $valor  ] || [ "$mc" == false ]
		then
			read valor1
		else
			read -e -p "" -i "$(echo "$valor + 0.0" | bc -l)" valor1
		fi
	fi
	echo -e  "${NC}"
	
	
	echo -e  "Digite o segundo valor: ${CYA}"
	read valor2
	echo -e  "${NC}"

fi

if [ "$op" == "sqrt" ]
then
	valor1=""
	op="sqrt("
	sqrtC=")"
	space=""
fi
valor=$valor1$op$valor2$space$sqrtC
#echo -e "${RED}$valor${NC}"
echo -e -n "${LGR} $valor1 $op$space$valor2$sqrtC = ${NC}${YEL}"
echo "$valor1 $op $valor2 $sqrtC" | bc -l
#if [ (( "$valor1 $op $valor2" | bc -l)) ]
echo -e -n "${NC}"
echo


simples

}







cientificaStart ()
{
echo
echo -e "${PUR}CALCULADORA CIENTÍFICA${NC}"
echo -e "${YEL}Caracteres aceitos:${NC}" 
echo -e "${GRE}+${NC} (soma) ex. 1+2="
echo -e "${GRE}-${NC} (subtração) ex. 1-2="
echo -e "${GRE}*${NC} (multiplicação) ex. 1*2="
echo -e "${GRE}/${NC} (divisão) ex. 1/2"
echo -e "${GRE}^${NC} (elevado) ex. 3^3 (${RED}USE SOMENTE NÚMERO INTEIROS no expoente${NC}) ex. '20.5${YEL}^2${NC} ${GRE}(certo!)${NC}', '20${YEL}^2.5${NC} ${RED}(ERRO!)${NC}'"
echo -e "(${RED}NÃO use os números pequenos${NC} como: ${RED}3¹${NC} ou ${RED}3²${NC} USE ${YEL}3^1${NC} ou ${YEL}3^2${NC} etc)"
echo
echo -e "você também pode usar:"
echo -e "${GRE}(${NC}2-1${GRE})${NC}*3 (parênteses)"
echo -e "${GRE}sqrt(${NC}num${GRE})${NC} (raiz quadrada) ex. ${YEL}sqrt(2)${NC} ou ${YEL}sqrt(10)${NC}"
echo
echo -e "${GRE}menu${NC} (para voltar ao menu)"
echo -e "${GRE}sair${NC} (para sair da calculadora)"
echo 
echo

cientifica
}

cientifica (){
#echo "Digite a fórmula: "
echo
#valor="2"
#echo "$valor"
if [ -z $valor  ] || [ "$mc" == false ]
then
	read -e -p "Digite a fórmula: " conta
else
	read -e -p "Digite a fórmula: " -i "$(echo "$valor + 0.0" | bc -l)" conta
fi

i=0
MEU_ARRAY=()	
#Separar todos
#echo "$i"
echo -e -n "${GRE}$conta${NC} = "
if [ "$conta" == *"sair"* ] || [ "$conta" == "sair" ]  || [ "$conta" == "sair"* ]  || [ "$conta" == *"sair" ] 
then
	#echo "ok"
	echo
	exit 
		
fi
if [ "$conta" == *"menu"* ] || [ "$conta" == "menu" ]  || [ "$conta" == "menu"* ]  || [ "$conta" == *"menu" ] 
then
	#echo "ok!"
	echo
	menu
	break
fi

valor=$conta
echo -e -n "${YEL}"
zeropontozero=0.0
echo -e "$conta + $zeropontozero" | bc -l

#read -e -p "Enter Your Name:" -i "Ricardo" NAME

#echo $NAME

echo -e "${NC}"

#echo -e "$valor" | bc -l

cientifica
}

menu
sair ()
{
exit
}


#BUGS À CONSERTAR:
