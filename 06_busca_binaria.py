comps = 0       # Variável de estatística

def busca_binaria(lista, val):
    """
    ALGORITMO DE BUSCA BINÁRIA
    Dados uma lista, que DEVE ESTAR PREVIAMENTE ORDENADA, 
    e também um valor de busca, divide a lista em duas partes,
    procurando pelo valor de busca apenas no lado em que esse
    valor poderia estar. Novas divisões são feitas até que se
    encontre o valor de busca ou que reste apenas uma sublista
    vazia. Nesse caso, conclui-se que o valor de busca não existe
    na lista.
    """
    # global avisa à função para utilizar uma variável que está fora
    # dela
    global comps
    comps = 0

    ini = 0                 # Posição inicial da lista
    fim = len(lista) - 1    # Posição final da lista

    # Para proceder à busca, é necessário que o marcador da
    # posição inicial esteja antes ou no máximo na mesma posição
    # que o marcador da posição final
    while ini <= fim:
        # Calculando a posição do meio da lista (aproximada, se o
        # número de elementos da lista for par)
        # O operador // significa divisão inteira, isto é, se a 
        # divisão resultar em parte fracionária, esta será desprezada
        meio = (ini + fim) // 2

        # Conta o número de comparações
        comps += 1

        # Verifica se o valor que está na posição do meio da lista
        # é igual ao valor de busca. Em caso afirmativo, retornamos
        # a posição do meio, pois o valor de busca foi encontrado nela
        if val == lista[meio]: return meio

        # Senão, caso o valor de busca seja MENOR do que o valor da
        # posição do meio, move o marcador de fim da lista para a
        # posição anterior à do meio e reincia a busca pela sublista
        # à ESQUERDA do meio
        elif val < lista[meio]:
            fim = meio - 1

        # Por fim, se o valor de busca for MAIOR que o valor da
        # posição do meio, move o marcador de início da lista para a
        # posição seguinte à do meio, reiniciando a busca pela 
        # sublista à DIREITA do meio
        else:
            ini = meio + 1

    # <~ CUIDADO COM A INDENTAÇÃO AQUI!
    # Se chegamos a este ponto, significa que o valor de busca não
    # existe na lista
    return -1

######################################################################

nums = [9, 21, 33, 12, 0, 18, -3, 30, -15, 6, 3, 27]

# Vamos definir algumas buscas para fazer
buscas = [-15, 4, 12]

# Loop para fazer a busca sequencial em cada um dos valores acima
for v in buscas:
    pos = busca_binaria(nums, v)
    if pos >= 0:
        print(f"Valor {v} encontrado na posição {pos}.")
    else:
        print(f"Valor {v} NÃO FOI ENCONTRADO, pois a busca retornou -1.")

############################################################################

# TESTE COM 1M+ DE NOMES

import sys

# Por padrão, o Python cria um cache otimizado de dados. Para nosso uso,
# porém, esse cache iria prejudicar nossos testes e comparações. Por isso,
# colocamos esta instrução para desabilitar a criação do cache
sys.dont_write_bytecode = True

from time import time

# Aqui, importamos a lista com 1M+ de nomes que está na pasta data
from data.nomes_completos import nomes

# Alguns nomes para efetuar buscas
buscas = [
    "EDSON PEREIRA",
    "MARIA FERREIRA",
    "VALDIR SILVA",
    "ORKUTILSON OLIVEIRA"
]

# Loop para efetuar as buscas
for n in buscas:
    hora_ini = time()   # Marcamos a hora de início da busca
    pos = busca_binaria(nomes, n)
    hora_fim = time()   # Marcamos a hora de término da busca
    if pos >= 0:
        print(f"Nome {n} encontrado na posição {pos} da lista de nomes.")
    else:
        print(f"Nome {n} NÃO ENCONTRADO na lista de nomes (busca retornou -1).")

    print(f"Comparações realizadas: {comps}")
    print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")

####################################################################################