# Variáveis de estatística
passd = comps = trocas = None

def selection_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO SELECTION SORT
    Isola (seleciona) o primeiro elemento da lista e, em seguida,
    determina o elemento de menor valor dentre os restantes. Se o
    valor mínimo encontrado for MENOR do que o valor previamente
    selecionado, efetua a troca entre eles. Continua selecionando
    o segundo elemento da lista e buscando o valor mínimo nas
    posições subsequentes. O processo se repete até que o penúltimo
    elemento da lista seja comparado com o último e feita a troca
    entre eles, caso necessário.
    """
    global passd, comps, trocas
    passd = comps = trocas = 0

    # Loop que vai da primeira até a PENÚLTIMA posição para
    # selecionar o elemento que será comparado com os demais. Este
    # laço também determina a quantidade de passadas que serão
    # executadas (número constante para o algoritmo: n-1)
    for pos_sel in range(len(lista) - 1):
        passd += 1

        # Inicia supondo que a posição do elemento de menor valor
        # dentre os remanescentes é aquela imediatamente seguinte
        # à do valor selecionado
        pos_menor = pos_sel + 1

        # Percorre os elementos remanescentes, em BUSCA SEQUENCIAL,
        # de pos_menor+1 até a última posição
        for pos in range(pos_menor + 1, len(lista)):
            # Caso o valor do elemento que se encontra na posição
            # atual (pos) seja MENOR do que o valor do elemento
            # apontado por pos_menor, ajusta pos_menor para a mesma
            # posição de pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        # <~ CUIDADO COM A INDENTAÇÃO AQUI!
        # Neste ponto, já terminamos de percorrer o remanescente da
        # lista e sabemos a posição do elemento de menor valor ali
        # existente. Comparamos o valor dos elementos nas posições
        # pos_menor e pos_sel. Se o PRIMEIRO for MENOR do que o 
        # SEGUNDO, efetuamos a troca entre eles
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            # Troca:
            lista[pos_sel], lista[pos_menor] = lista[pos_menor], lista[pos_sel]
            trocas += 1

################################################################################

nums = [7, 0, 9, 2, 8, 4, 6, 1, 5, 3]
print("--- CASO MÉDIO ---")
# BUBBLE: Passadas: 7, comparações: 63, trocas: 26
# Agora:  Passadas: 9, comparações: 45, trocas: 6
print("Antes da ordenação:", nums)
selection_sort(nums)
print("Após a ordenação:  ", nums)
print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}\n\n")

# Obs: o pior caso do Selection Sort é DIFERENTE do pior caso do Bubble Sort
nums = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
print("--- PIOR CASO ---")
# BUBBLE: Passadas: 10, comparações: 90, trocas: 45
# Agora:  Passadas:  9, comparações: 45, trocas:  9
print("Antes da ordenação:", nums)
selection_sort(nums)
print("Após a ordenação:  ", nums)
print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}\n\n")

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("--- MELHOR CASO ---")
# BUBBLE: Passadas: 1, comparações:  9, trocas: 0
# Agora:  Passadas: 9, comparações: 45, trocas: 0
print("Antes da ordenação:", nums)
selection_sort(nums)
print("Após a ordenação:  ", nums)
print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}\n\n")

################################################################################

# TESTE COM 100K NOMES

from time import perf_counter

import sys

from lib.util import fmt_tempo

# Desabilita a criação de cache otimizado de dados
sys.dont_write_bytecode = True  

from data.nomes_desord import nomes

# Apesar de a lista nomes_desord ter 1M+ de itens,
# vamos dar ao Selection Sort só os primeiros 100K
nomes = nomes[:100000]

inicio = perf_counter()
selection_sort(nomes)
duracao = perf_counter() - inicio

print(nomes)

print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}")
print(f"Tempo gasto: {fmt_tempo(duracao)}.\n\n")
