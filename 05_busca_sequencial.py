def busca_sequencial(lista, val):
    """
    Função que realiza uma busca sequencial em uma lista com n
    elementos, procurando por val.
    Se o valor for encontrado, retorna a posição (p) de
    val na lista, resultando em p+1 operações de comparação.
    Caso val não exista na lista, retorna o valor convencional
    -1, tendo efetuado n operações de comparação
    """
    # Percorre a lista do início ao fim, usando range() e len(),
    # porque é necessário saber tanto o valor quanto a posição de
    # cada elemento
    for p in range(len(lista)):
        # Se o resultado da comparação de igualdade entre val e 
        # lista[p] der verdadeiro, encontramos a posição de val
        # na lista. Retornamos p e encerramos a busca
        if val == lista[p]: return p
        # Senão, seguimos para o próximo elemento da lista
        # (incrementando o valor de p)
        
    # <~ CUIDADO COM A INDENTAÇÃO AQUI!
    # Se chegamos até aqui, é porque o for percorreu toda a lista
    # e val não foi encontrado nela. Nesse caso, retornamos o valor
    # -1 para indicar essa situação
    return -1

############################################################################
 
nums = [9, 21, 33, 12, 0, 18, -3, 30, -15, 6, 3, 27]

# Vamos definir algumas buscas para fazer
buscas = [-15, 4, 12]

# Loop para fazer a busca sequencial em cada um dos valores acima
for v in buscas:
    pos = busca_sequencial(nums, v)
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
    pos = busca_sequencial(nomes, n)
    hora_fim = time()   # Marcamos a hora de término da busca
    if pos >= 0:
        print(f"Nome {n} encontrado na posição {pos} da lista de nomes.")
    else:
        print(f"Nome {n} NÃO ENCONTRADO na lista de nomes (busca retornou -1).")

    print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")

####################################################################################
