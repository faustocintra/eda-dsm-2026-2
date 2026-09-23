# Variáveis globais de estatística
divs = comps = juncs = None

def merge_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO MERGE SORT
    Durante o processo de ordenação, este algoritmo "desmonta" a lista
    original, que contém N elementos, até obter N novas listas, cada
    qual contendo apenas um elemento. Em seguida, utilizando a técnica
    de mesclagem ("merging"), "monta" uma nova lista, contendo os 
    elementos já ordenados. A lista original desordenada não é modificada.
    """
    global divs, comps, juncs

    # PARTE 1: DIVISÃO DA LISTA ORIGINAL
    
    # Para que possa haver a divisão da lista, esta deve ter mais de
    # um elemento. Se essa condição não for satisfeita, sai prematuramente
    # da função (early return), retornando a própria lista recebida como
    # parâmetro
    if len(lista) <= 1: return lista

    # Calcula a posição do meio da lista, para fazer a respectiva divisão
    # em duas partes (aproximadamente) do mesmo tamanho
    meio = len(lista) // 2

    # Gera uma cópia da parte esquerda da lista
    sublista_esq = lista[:meio]
    # Faz o mesmo com a metade direita da lista
    sublista_dir = lista[meio:]

    divs += 1

    # Chamamos recursivamente (duas vezes!) a própria função merge_sort()
    # para que ela continue repartindo cada sublista em outras duas,
    # menores
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # PARTE 2: MONTAGEM DE NOVAS LISTAS, COM ELEMENTOS ORDENADOS

    # Ponteiros para percorrer as sublistas esquerda e direita
    pos_esq = pos_dir = 0

    # Inicializando duas listas vazias, que serão preenchidas com
    # os elementos ordenados
    ordenada, sobra = [], []

    # Percorremos as sublistas esquerda e direita comparando elementos
    # entre elas e inserindo na lista ordenada na ordem correta
    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
        comps += 1
        # O menor elemento na comparação está na sublista esquerda
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            # Insere o elemento da sublista esquerda na lista ordenada
            ordenada.append(sublista_esq[pos_esq])
            pos_esq += 1    # Avança o ponteiro da sublista esquerda
        # O menor elemento da comparação está na sublista direita
        else:
            # Insere o elemento da sublista esqueda na lista ordenada
            ordenada.append(sublista_dir[pos_dir])
            pos_dir += 1

    # <~ CUIDADO COM A INDENTAÇÃO AQUI!

    # *SEMPRE* haverá sobra em alguma das sublistas. É necessário
    # determinar em qual delas está a sobra e inseri-la diretamente na
    # lista ordenada

    # A sobra está na sublista esquerda
    # if pos_esq < pos_dir: sobra = sublista_esq[pos_esq:] # BUG!
    if pos_esq < len(sublista_esq): sobra = sublista_esq[pos_esq:]
    # A sobra está na sublista direita
    else: sobra = sublista_dir[pos_dir:]

    # A lista final ordenada é o resultado da junção (concatenação)
    # da lista ordenada com a sobra
    juncs += 1
    return ordenada + sobra

##########################################################################

# OBSERVAÇÕES:
# 1) O Merge Sort usa uma estratégia ("divisão e conquista") diferente dos
#    algoritmos Bubble Sort e Selection Sort, que se valem da técnica de
#    permuta. Por esse motivo, a contagem de passadas, comparações trocas
#    não se aplica ao Merge Sort; em vez disso, contamos divisões,
#    comparações e junções.
# 2) Em algoritmos recursivos (como é o caso do Merge Sort), as variáveis
#    globais de estatística não podem ser zeradas dentro da função, pois
#    a contagem seria resetada a cada chamada recursiva à função. Por causa
#    disso, elas devem ser zeradas do lado de fora, antes de cada teste.

nums = [7, 0, 9, 2, 8, 4, 6, 1, 5, 3]
print("--- CASO MÉDIO ---")
# Divisões: 9, comparações: 21, junções: 9
divs = comps = juncs = 0        # Zerando variáveis de estatística
print("Antes da ordenação:", nums)
nums_ord = merge_sort(nums)
print("Após a ordenação:  ", nums_ord)
print(f"Divisões: {divs}, comparações: {comps}, junções: {juncs}\n\n")

# Um dos piores casos para o Merge Sort ocorre quando a lista inicial
# contém valores que ficam intercalados durante a mesclagem. Assim, 
# nenhuma sublista termina antecipadamente.
nums = [2, 6, 4, 0, 8, 3, 7, 5, 1, 9]
print("--- PIOR CASO ---")
# Divisões: 9, comparações: 25, junções: 9
divs = comps = juncs = 0        # Zerando variáveis de estatística
print("Antes da ordenação:", nums)
nums_ord = merge_sort(nums)
print("Após a ordenação:  ", nums_ord)
print(f"Divisões: {divs}, comparações: {comps}, junções: {juncs}\n\n")

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("--- MELHOR CASO ---")
# Divisões: 9, comparações: 15, junções: 9
divs = comps = juncs = 0        # Zerando variáveis de estatística
print("Antes da ordenação:", nums)
nums_ord = merge_sort(nums)
print("Após a ordenação:  ", nums_ord)
print(f"Divisões: {divs}, comparações: {comps}, junções: {juncs}\n\n")

################################################################################

# TESTE COM 1M+ NOMES

from time import perf_counter
import tracemalloc

import sys

from lib.util import fmt_tempo, fmt_memoria

# Desabilita a criação de cache otimizado de dados
sys.dont_write_bytecode = True  

from data.nomes_desord import nomes

# Inicia a medição de memória
tracemalloc.start()
mem_inicial, _ = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()

inicio = perf_counter()
nomes_ord = merge_sort(nomes)
duracao = perf_counter() - inicio

# Finaliza a medição de memória
mem_final, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(nomes_ord)

print(f"Divisões: {divs}, comparações: {comps}, junções: {juncs}")
print(f"Tempo gasto: {fmt_tempo(duracao)}.")

pico_fmtd, adic_fmtd = fmt_memoria(mem_inicial, mem_final, mem_pico)

print(f"Pico adicional: {pico_fmtd}")
print(f"Memória adicional ao final: {adic_fmtd}")