INSERT INTO transacoes (CodigoClienteEstr, DataCompra, ValorCompra)
 VALUES 
(1,"2020-03-02", 160),
(2,"2020-01-15", 25),
(2,	"2020-01-30",	250),
(3,	"2020-01-13",	40),
(3,	"2020-01-25",	3),
(3,	"2020-01-31",	90),
(3,	"2020-02-01",	80),
(4,	"2020-12-29",	50),
(4,	"2020-01-16",	40),
(4,	"2020-01-20",	90),
(4,	"2020-01-25",	30),
(5,	"2020-02-02",	15),
(5,	"2020-01-25",	70),
(5,	"2020-03-03",	60),
(5,	"2020-02-09",	70);






EXERCÍCIOS 



SELECT * FROM transacoes
WHERE  
CodigoClienteEstr=(SELECT CodigoCliente FROM cliente WHERE  Nome LIKE "%Luis%"#Descobrir o código do Luis
 )#Selecionar todas as compras de Luis (código 2) 
AND 
ValorCompra>10 #verifica todos que são maiores que 10 por conta da promoção
;

#RETORNA 80 e 160. Ele de fato comprou 3 vezes, mas somente duas das vezes passou de 10 o valor da compra, ou seja, 2 vezes apenas ele cumpriu com as condições da promoção, ele não sabe (ou não se lembra) que 10 reais é o mínimo para cada compra valer na promoção... 
#Abaixo pode ser provado qual compra não passou na promoção:
SELECT * FROM transacoes
WHERE  
CodigoClienteEstr=(SELECT CodigoCliente FROM cliente WHERE  Nome LIKE "%Luis%"#Descobrir o código do Luis
 )#Selecionar todas as compras de Luis (código 2) 
;
#Ao executar esse código, será possível ver o valor de 7, que não entra na promoção 

#Só leia isso com tempo livre... (Agora eu... Parando pra pensar, o que impede alguém de sair e entrar na loja pra receber um monte de cupons? No caso, se ele tivesse de fato comprado 240 em produtos de 10 reais, ele poderia ter 24 cupons :D  Mas também não deixa de ser um incentivo pra ele dividir as compras em vários dias e visitar mais a loja, ou principalmente, alguém que só compraria algo de 9 reais ao saber da promoção compraria algo só pra completar 10 e participar da promoção...)

