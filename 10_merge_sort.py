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
    if pos_esq < pos_dir: sobra = sublista_esq[pos_esq:]
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
divs = comps = juncs = 0        # Zerando variáveis de estatística
print("Antes da ordenação:", nums)
nums_ord = merge_sort(nums)
print("Após a ordenação:  ", nums_ord)
print(f"Divisões: {divs}, comparações: {comps}, junções: {juncs}\n\n")