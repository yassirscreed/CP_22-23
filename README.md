O objetivo deste projeto e estudar a evolucao de um ecossistema de bacterias utilizando a simulacao discreta estocastica, implementada em Python.

Para tal comeca por considerar-se o habitat das bacterias como uma grelha de duas dimensoes, de lado N, tal que
no total existem N^2 celulas na grelha. As celulas da grelha estao numerados de 0 a N  1 na horizontal e na vertical. 
E de notar que o numero de bacterias em cada celula nao pode exceder um numero  Q e que a grelha e
inicializada com uma unidade de alimento em cada celula.
Figura 1: Exemplo de grelha de lado N = 8 com L^2 = 64 celulas

A simulacao comeca com tres especies de bacterias A, B e C. As bacterias da especie A alimentam-se das bacterias
da especie B ou C enquanto que as bacterias da especie B e C alimentam-se de comida que se encontra distribuida
pelas celulas da grelha. Para alem disso, os individuos das bacterias B e C tem ainda a possibilidade de se fundirem
de modo a criarem um individuo da especie BC. 
A especie BC e imune aos ataques das bacterias da especie A e alimenta-se tambem da comida que se encontra na grelha. Cada bacteria possui um identificador (numero natural
unico para cada individuo) e comeca a simulacao com uma quantidade de comida armazenada F.

Os individuos de cada especie de bacterias podem reproduzir-se quando se encontram na mesma celula com outro
individuo da mesma especie. Aquando desta reproducao, um novo individuo e colocado no mesmo lugar da grelha
que os seus progenitores se nao exceder Q, o numero maximo de bacterias por celula (caso contrario a reproducao nao
acontece). Os individuos deslocam-se na grelha e podem morrer de morte natural.

A simulacao e constituida pelos seguintes passos:
	1. Inicializacao do sistema: O sistema e inicializado com NA, NB e NC individuos da especie A, B e C respetivamente, adicionados aleatoriamente a grelha, seguindo uma distribuicao uniforme. Cada individuo e inicializado
		com uma quantidade individual de alimento armazenado F, que pode utilizar para se alimentar (ver 2.(d)). Esta
		quantidade e igual para todas as especies de bacterias. E de notar novamente que o numero de bacterias em 
		cada celula nao pode exceder um numero Q.
	2. Evolucao do sistema: Cada bacteria evolui de acordo com os seguintes mecanismos aleatorios ate ser atingido
	    	o tempo limite de simulacao TS
		(a) Deslocamento de Bacterias: As bacterias deslocam-se uma distancia arbitraria d, escolhida de 
         acordo com uma distribuicao uniforme. Desta forma, e escolhido um K  d  K na direcao x e 
         outro na direcao y, onde K e o limite de deslocamento para as bacterias.
        A grelha tem condicoes fronteira periodicas:
                 ao atingir uma parede da grelha, a bacteria continua o seu deslocamento a partir da 
                 parede oposta.
			Alem disto, se a celula de destino ja estiver ocupada com o numero maximo de bacterias Q, o 
            deslocamento nao acontece.
		(b) Reproducao de Bacterias: O tempo medio entre a reproducao de bacterias da mesma 
         especie e dado por uma variavel aleatoria de distribuicao exponencial e valor medio TR.
         Esta reproducao ocorre sempre que dois individuos da mesma especie se encontrem na mesma 
         celula. 
         A bacteria resultante da reproducao
			aparece na mesma celula desde que nao exceda o numero maximo de bacterias por celula, Q.
		(c) Fusao entre Bacterias B e C: O tempo medio entre a fusao de uma bacteria da especie B com uma da C
			e dado por uma variavel aleatoria de distribuicao exponencial e valor medio TF . Esta fusao ocorre sempre
			que um individuo de cada especie se encontre na mesma celula, e da mesma resulta um novo individuo da
			especie BC. Os dois individuos originais sao removidos do sistema
		(d) Alimentacao das bacterias: O tempo medio entre a alimentacao das bacterias e uma variavel aleatoria
			de distribuicao exponencial e valor medio TA.
			 Da especie A: A alimentacao da especie A ocorre sempre que uma destas bacterias se encontre na
				mesma celula com um individuo da especie B ou C. Se na celula existe mais do que um individuo da
				especie B ou C, a bacteria A escolhe uniformemente qual o individuo do que se vai alimentar e este e
				retirado ao sistema. Se nao existe nenhuma bacteria B ou C na celula, a bacteria A pode alimentar-se
				de uma unidade de alimento armazenado. Em ultimo caso, se ja nao tiver alimento armazenado, e
				retirada do sistema.
 			 Da especie B, C ou BC: Para as restantes especies, a alimentacao consiste em retirar uma unidade de
				alimento a celula da grelha em que a bacteria se encontra. Se isto ocorrer, o alimento e eventualmente
				reposto a celula atraves da reposicao de alimento na grelha. No caso de esta celula nao possuir alimento,
				a bacteria pode alimentar-se de uma unidade de alimento armazenado. Em ultimo caso, se tambem
				nao houver alimento armazenado, a bacteria e retirada do sistema.
		(e) Reposicao de Alimento na Grelha: O tempo medio entre reposicao de alimento na grelha e uma variavel
			aleatoria de distribuicao exponencial e valor medio TRP .
		(f) Morte Natural: O tempo de morte natural e dado por uma variavel aleatoria com distribuicao exponencial
			de valor medio TM

	3. Observacao do resultado: O simulador deve produzir como output um grafico que mostre a evolucao da
		quantidade de bacterias de cada especie desde o tempo 0 ate ao tempo TS

O simulador deve ser desenvolvido seguindo o metodo da programacao modular por camadas centrado nos dados.
1. Comece por identificar os tipos de dados relevantes, incluindo a grelha bidimensional, as bacterias, os eventos, e a CAP, e desenvolva os respectivos modulos;
2. Desenvolva o simulador sobre a camada que disponibiliza estes tipos de dados;
3. Experimente o simulador com diversos conjuntos de dados `a sua escolha, apresentando os respectivos resultados.
Considere tambem o conjunto de dados a ser fornecido pela cadeira.
Sem usar classes