# Variáveis globais de estatística
comps = trocas = passd = None

def quick_sort(lista, ini = 0, fim = None):
    """
    ALGORITMO DE ORDENAÇÃO QUICK SORT
    Escolhe um dos elementos da lista para ser o pivô (na
    nossa implementação, será o último) e, na primeira
    passada, divide a lista a partir da posição final do
    pivô em uma sublista à sua esquerda, contendo apenas
    valores menores do que ele, e outra sublista à sua
    direita, compreendendo apenas valores maiores ou iguais a
    ele. Em seguida, recursivamente, repete o processo para
    cada uma das sublistas, até que toda a lista esteja
    ordenada.
    """
    global comps, trocas, passd

    # Cada chamada à função (inclusive as recursivas) é
    # considerada uma passada
    passd += 1

    # Quando o valor do parâmetro "fim" não tiver sido
    # informado (ou seja, seu valor é igual a None),
    # atribuímos a ele o valor da última posição da lista
    if fim is None: fim = len(lista) - 1

    # Para que seja possível proceder à ordenação, é
    # necessário que a região da lista delimitada pelos
    # parâmetros "ini" e "fim" contenha, pelo menos, DOIS
    # elementos. Caso não seja essa a situação, saímos da
    # função sem fazer nada ("early return")
    if fim <= ini: return

    # Inicialização das variáveis
    pivot = fim     # O pivô será o último elemento da (sub)lista
    div = ini - 1   # O divisor inicia uma posição antes de "ini"

    # Percorre a lista da posição "ini" até a posição "fim" - 1
    for pos in range(ini, fim):
        # Se o elemento da posição "pos" for MENOR do que o
        # elemento da posição "pivot", avança "div" em uma
        # posição e promove a troca entre os elementos das
        # posições "div" e "pos"
        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1
            # Efetua a troca apenas se os valores de "pos" e
            # "div" forem distintos, indicando elementos diferentes
            if pos != div:
                trocas += 1
                lista[pos], lista[div] = lista[div], lista[pos]

    # <~ CUIDADO COM A INDENTAÇÃO AQUI!
    # Após o laço "for" terminar, "div" deve ainda avançar
    # mais uma posição
    div += 1

    # Comparamos os elementos das posições "pivot" e "div"
    # entre si e, caso o primeiro seja MENOR do que o
    # segundo, efetuamos a troca entre eles
    comps += 1
    if lista[pivot] < lista[div]:
        trocas += 1
        lista[pivot], lista[div] = lista[div], lista[pivot]

    # Chamamos recursivamente a função para repetir o processo
    # para as sublistas à esquerda e à direita do pivô
    quick_sort(lista, ini, div - 1)
    quick_sort(lista, div + 1, fim)

##################################################################

# No caso do Quick Sort, não existe um único caso em que os três contadores
# representam o melhor ou o pior caso simultaneamente. Nos testes abaixo,
# consideramos melhores os arranjos em que o número de trocas foi menor,
# embora, ocasionalmente, o de passadas ou o de comparações não o sejam

nums = [7, 0, 9, 2, 8, 4, 6, 1, 5, 3]
print("--- CASO MÉDIO ---")
# BUBBLE: Passadas: 7, comparações: 63, trocas: 26
# SELECTION:  Passadas: 9, comparações: 45, trocas: 6
comps = trocas = passd = 0
print("Antes da ordenação:", nums)
quick_sort(nums)
print("Após a ordenação:  ", nums)
print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}\n\n")

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("--- PIOR CASO ---")
# BUBBLE: Passadas: 10, comparações: 90, trocas: 45
# SELECTION:  Passadas:  9, comparações: 45, trocas:  9
comps = trocas = passd = 0
print("Antes da ordenação:", nums)
quick_sort(nums)
print("Após a ordenação:  ", nums)
print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}\n\n")

nums = [0, 3, 2, 1, 6, 5, 9, 8, 7, 4]
print("--- MELHOR CASO ---")
# BUBBLE: Passadas: 1, comparações:  9, trocas: 0
# SELECTION:  Passadas: 9, comparações: 45, trocas: 0
comps = trocas = passd = 0
print("Antes da ordenação:", nums)
quick_sort(nums)
print("Após a ordenação:  ", nums)
print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}\n\n")

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
comps = trocas = passd = 0
quick_sort(nomes)
duracao = perf_counter() - inicio

# Finaliza a medição de memória
mem_final, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(nomes)

print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}")
print(f"Tempo gasto: {fmt_tempo(duracao)}.")

pico_fmtd, adic_fmtd = fmt_memoria(mem_inicial, mem_final, mem_pico)

print(f"Pico adicional: {pico_fmtd}")
print(f"Memória adicional ao final: {adic_fmtd}")

