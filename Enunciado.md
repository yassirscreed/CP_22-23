O objetivo deste projeto é estudar a evolução de um ecossistema de bactérias utilizando a simulação discreta estocástica, implementada em Python.

Para tal começa por considerar-se o habitat das bactérias como uma grelha de duas dimensões, de lado $N$, tal que no total existem $N^{2}$ células na grelha. As células da grelha estão numerados de 0 a $N-1$ na horizontal e na vertical (cf. Fig. 1). É de notar que o número de bactérias em cada célula não pode exceder um número $Q$ e que a grelha é inicializada com uma unidade de alimento em cada célula.

![](https://cdn.mathpix.com/cropped/2023_04_12_fb06018b8eda26748114g-1.jpg?height=425&width=434&top_left_y=730&top_left_x=797)

Figura 1: Exemplo de grelha de lado $N=8$ com $L^{2}=64$ células

A simulação começa com três espécies de bactérias A, B e C. As bactérias da espécie A alimentam-se das bactérias da espécie B ou $\mathrm{C}$ enquanto que as bactérias da espécie B e C alimentam-se de comida que se encontra distribuída pelas células da grelha. Para além disso, os indivíduos das bactérias B e C têm ainda a possibilidade de se fundirem de modo a criarem um indíviduo da espécie BC. A espécie BC é imune aos ataques das bactérias da espécie A e alimenta-se também da comida que se encontra na grelha. Cada bactéria possui um identificador (número natural único para cada indivíduo) e começa a simulação com uma quantidade de comida armazenada $F$.

Os indivíduos de cada espécie de bactérias podem reproduzir-se quando se encontram na mesma célula com outro indivíduo da mesma espécie. Aquando desta reprodução, um novo indivíduo é colocado no mesmo lugar da grelha que os seus progenitores se não exceder Q, o número máximo de bactérias por célula (caso contrário a reprodução não acontece). Os indivíduos deslocam-se na grelha e podem morrer de morte natural.

A simulação é constituída pelos seguintes passos:

1. Inicialização do sistema: $\mathrm{O}$ sistema é inicializado com $N_{A}, N_{B}$ e $N_{C}$ indivíduos da espécie A, B e C respetivamente, adicionados aleatoriamente à grelha, seguindo uma distríbuição uniforme. Cada indivíduo é inicializado com uma quantidade individual de alimento armazenado $F$, que pode utilizar para se alimentar (ver 2.(d)). Esta quantidade é igual para todas as espécies de bactérias. É de notar novamente que o número de bactérias em cada célula não pode exceder um número $Q$.

2. Evolução do sistema: Cada bactéria evolui de acordo com os seguintes mecanismos aleatórios até ser atingido o tempo limite de simulação $T_{S}$

(a) Deslocamento de Bactérias: O tempo médio entre o deslocamento de cada bactéria é dado por uma variável aleatória de distribuição exponencial e tempo médio $T_{D}$. As bactérias deslocam-se uma distância arbitrária $\Delta d$, escolhida de acordo com uma distribuição uniforme. Desta forma, é escolhido um $-K \leq$ $\Delta d \leq K$ na direção $x$ e outro na direção $y$, onde $K$ é o limite de deslocamento para as bactérias. A grelha tem condições fronteira periódicas: ao atingir uma parede da grelha, a bactéria continua o seu deslocamento a partir da parede oposta.

Além disto, se a célula de destino já estiver ocupada com o número máximo de bactérias $Q$, o deslocamento não acontece.

(b) Reprodução de Bactérias: O tempo médio entre a reprodução de bactérias da mesma espécie é dado por uma variável aleatória de distribuição exponencial e valor médio $T_{R}$. Esta reprodução ocorre sempre que dois indivíduos da mesma espécie se encontrem na mesma célula. A bactéria resultante da reprodução aparece na mesma célula desde que não exceda o número máximo de bactérias por célula, Q.

(c) Fusão entre Bactérias B e C: O tempo médio entre a fusão de uma bactéria da espécie B com uma da C é dado por uma variável aleatória de distribuição exponencial e valor médio $T_{F}$. Esta fusão ocorre sempre que um indivíduo de cada espécie se encontre na mesma célula, e da mesma resulta um novo indivíduo da espécie BC. Os dois indivíduos originais são removidos do sistema (d) Alimentação das bactérias: O tempo médio entre a alimentação das bactérias é uma variável aleatória de distribuição exponencial e valor médio $T_{A}$.

- Da espécie A: A alimentação da espécie A ocorre sempre que uma destas bactérias se encontre na mesma célula com um indivíduo da espécie B ou C. Se na célula existe mais do que um indivíduo da espécie B ou C, a bactéria A escolhe uniformemente qual o indivíduo do que se vai alimentar e este é retirado ao sistema. Se não existe nenhuma bactéria $\mathrm{B}$ ou C na célula, a bactéria A pode alimentar-se de uma unidade de alimento armazenado. Em último caso, se já não tiver alimento armazenado, é retirada do sistema.

- Da espécie B, C ou BC: Para as restantes espécies, a alimentação consiste em retirar uma unidade de alimento à célula da grelha em que a bactéria se encontra. No caso de esta célula não possuir alimento, a bactéria pode alimentar-se de uma unidade de alimento armazenado. Em último caso, se também não houver alimento armazenado, a bactéria é retirada do sistema.

(e) Reposição de Alimento na Grelha: O tempo médio entre reposição de alimento na grelha é uma variável aleatória de distribuição exponencial e valor médio $T_{R P}$. A quantidade de alimento em cada célula da grelha não deve exceder uma unidade.

(f) Morte Natural: O tempo de morte natural é dado por uma variável aleatória com distribuição exponencial de valor médio $T_{M}$

3. Observação do resultado: O simulador deve produzir como output um gráfico que mostre a evolução da quantidade de bactérias de cada espécie desde o tempo 0 até ao tempo $T_{S}$

O simulador deve ser desenvolvido seguindo o método da programação modular por camadas centrado nos dados.

1. Comece por identificar os tipos de dados relevantes, incluindo a grelha bidimensional, as bactérias, os eventos, e a CAP, e desenvolva os respectivos módulos;

2. Desenvolva o simulador sobre a camada que disponibiliza estes tipos de dados;

3. Considere o seguinte conjunto de dados, apresentando os respectivos resultados, e indicando explicitamente que se trata dos resultados para o conjunto de dados fornecido pelo enunciado:

- $N=10$ - Número de células da aresta da grelha bidimensional onde decorre a simulação

- $N_{A}=30$ - Número inicial de bactérias da espécie $\mathrm{A}$

- $N_{B}=50$ - Número inicial de bactérias da espécie B

- $N_{C}=50$ - Número inicial de bactérias da espécie C

- $T_{S}=20$ - Tempo total de simulação

- $T_{D}=2$ - Valor médio da distribuição dos tempos de deslocamento

- $K=5$ - Limite de cada deslocamento individual das bactérias, em cada direção

- $T_{R}=1$ - Valor médio da distribuição dos tempos de reprodução

- $T_{A}=5$ - Valor médio da distribuição dos tempos de alimentação

- $T_{M}=5$ - Valor médio da distribuição dos tempos de morte natural das bactérias

- $T_{F}=1$ - Valor médio da distribuição dos tempos de fusão entre bactérias da espécie B e bactérias da espécie C

- $T_{R P}=2$ - Valor médio da distribuição dos tempos de reposição de comida na grelha

- $F=2$ - Quantidade de comida armazenada inicialmente por cada bactéria inicializada

- $Q=4$ - Número máximo de bactérias em cada célula da grelha

De seguida são apresentados dois exemplos de gráficos de resultados obtidos para o conjunto de dados apresentado anteriormente:

![](https://cdn.mathpix.com/cropped/2023_04_12_fb06018b8eda26748114g-2.jpg?height=543&width=702&top_left_y=2153&top_left_x=200)

Figura 2: Exemplo 1 de gráfico de resultados

![](https://cdn.mathpix.com/cropped/2023_04_12_fb06018b8eda26748114g-2.jpg?height=528&width=709&top_left_y=2169&top_left_x=1119)

Figura 3: Exemplo 2 de gráfico de resultados Experimente também o simulador com diversos conjuntos de dados à sua escolha, apresentando os respectivos resultados.

\section{Entrega do projeto:}

O projecto é entregue através do sistema Fenix, após a inscrição do respectivo grupo na plataforma.

A entrega deve consistir num único ficheiro (zip ou rar) contendo:

- o simulador

- os módulos

- um relatório explicando as principais opções tomadas para a implementação dos módulos e do simulador, incluindo exemplos que ilustrem e permitam analisar o comportamento dos módulos e do simulador propostos.

\section{Formato dos ficheiros:}

- o simulador e os módulos devem ser desenvolvidos em ficheiros IPYNB ou PY, e cada um deles apresentado também no formato PDF ou HTML.

- o relatório pode ser feito em processador de texto (submetido em PDF) ou no Jupyter (submetido em IPYNB e também em PDF ou HTML).

O prazo de entrega é: 14/04/2022, às 18:00.

Modulos disponiveis:
```python
# bacteria.py
class Bacteria:
    def __init__(self, id , species , food):
        self.id = id
        self.species = species
        self.food = food


def create_bacteria(id, species, food):
    return Bacteria(id, species, food)

def move_bacteria(grid, bacteria, x, y, Q):
    new_x = (x + bacteria.x) % len(grid)
    new_y = (y + bacteria.y) % len(grid[0])

    if len(grid[new_x][new_y]['bacteria']) >= Q: # se tiver mais que Q bactérias na célula, não se move
        return
    
    grid[bacteria.x][bacteria.y]['bacteria'].remove(bacteria)
    grid[new_x][new_y]['bacteria'].append(bacteria)
    bacteria.x, bacteria.y = new_x, new_y

def reproduce(grid, bacteria, Q):
    if len(grid[bacteria.x][bacteria.y]['bacteria']) < Q:
        new_bacteria = create_bacteria(bacteria.species, bacteria.food)
        grid[bacteria.x][bacteria.y]['bacteria'].append(new_bacteria)

def consume_food(bacteria, amount):
    bacteria.food -= amount

def die(grid, bacteria):
    grid[bacteria.x][bacteria.y]['bacteria'].remove(bacteria)

# grid.py
def create_grid(N):
    return [[{'food': 1, 'bacteria': []} for _ in range(N)] for _ in range(N)]

def add_food_to_cell(grid, x, y, amount):
    grid[x][y]['food'] += amount

def consume_food_in_cell(grid, x, y, amount):
    grid[x][y]['food'] -= amount
    if grid[x][y]['food'] < 0:
        grid[x][y]['food'] = 0

def remove_food_from_cell(grid, x, y, amount):
    grid[x][y]['food'] -= amount

def add_bacteria_to_cell(grid, x, y, bacteria):
    grid[x][y]['bacteria'].append(bacteria)

def remove_bacteria_from_cell(grid, x, y, bacteria):
    grid[x][y]['bacteria'].remove(bacteria)


# Modulo cap
# Disponibiliza as operacoes necessarias para a criacao e
# manipulacao da Cadeia de Acontecimentos Pendentes

import event

def newc():
    return []
    
def addE(c, e):
    return [e1 for e1 in c if event.time(e1) < event.time(e)] + [e] + \
           [e1 for e1 in c if event.time(e1) > event.time(e)]


def delE(c):
    if len(c)>0:
        return c[1:]
    else:
        print("Erro de delE! A cap está vazia")

def nextE(c):
    if len(c)>0:
        return c[0]
    else:
        print("Erro de nextE! A cap está vazia")
        
def showE(c):
    for e in c:
        print(event.time(e), event.kind(e))   

# Modulo event
# Disponibiliza as operacoes necessarias para a criacao e
# manipulacao de eventos

def evt(t, k, counts):
    return [t, k, counts]

def time(e):
    return e[0]

def kind(e):
    return e[1]

def counts(e):
    return e[2]
```