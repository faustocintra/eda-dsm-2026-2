def merge_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO MERGE SORT ITERATIVO
    Começa com sublistas de um elemento e, a cada rodada, mescla pares
    de sublistas já ordenadas. O tamanho das sublistas dobra até que
    toda a lista esteja ordenada. A lista original é modificada.
    """

    # PARTE 1: DEFINIÇÃO DO TAMANHO DAS SUBLISTAS

    # Inicia com o menor tamanho de partição de 2^0 = 1
    tam_part = 1
    n = len(lista)
    
    # Enquanto o tamanho da partição for menor que o da lista, ainda
    # haverá sublistas a serem mescladas
    while (tam_part < n):
        # Inicia a rodada pelo começo da lista original
        esq = 0

        # PARTE 2: MESCLAGEM DOS PARES DE SUBLISTAS

        # Percorre a lista em blocos de até duas partições, mesclando
        # as sublistas esquerda e direita de cada bloco
        while (esq < n):
            # Calcula o último índice do bloco, sem ultrapassar a lista.
            # O último bloco pode ter menos de 2 * tam_part elementos
            dir = min(esq + 2 * tam_part - 1, n - 1)

            # A sublista esquerda ocupa até tam_part posições; os
            # elementos restantes, se houver, formam a sublista direita
            meio = min(esq + tam_part - 1, dir)

            # Calcula os tamanhos das duas sublistas. A direita pode
            # ficar vazia quando o bloco final estiver incompleto
            tam_esq = meio - esq + 1
            tam_dir = dir - meio

            # Cria vetores auxiliares para preservar os valores que
            # serão sobrescritos na lista original durante a mesclagem
            lista_esq = [0] * tam_esq   # Vetor auxiliar
            lista_dir = [0] * tam_dir   # Vetor auxiliar

            # Copia os elementos das sublistas para os vetores auxiliares
            for pos_esq in range(0, tam_esq):
                lista_esq[pos_esq] = lista[esq + pos_esq]
            for pos_esq in range(0, tam_dir):
                lista_dir[pos_esq] = lista[meio + pos_esq + 1]

            # Ponteiros para percorrer os vetores auxiliares e indicar
            # onde será escrito o próximo elemento na lista original
            pos_esq, pos_dir, i = 0, 0, esq

            # Compara os elementos das duas sublistas e copia o menor
            # deles para a próxima posição da lista original
            while pos_esq < tam_esq and pos_dir < tam_dir:
                # O menor elemento está na sublista direita
                if lista_esq[pos_esq] > lista_dir[pos_dir]:
                    lista[i] = lista_dir[pos_dir]
                    pos_dir += 1  # Avança o ponteiro da direita
                # O menor elemento está na esquerda; em caso de
                # igualdade, ela vem primeiro, preservando a ordem
                else:
                    lista[i] = lista_esq[pos_esq]
                    pos_esq += 1  # Avança o ponteiro da esquerda
                i += 1

            # Quando uma sublista terminar, copia os elementos que
            # sobraram na esquerda, se houver
            while pos_esq < tam_esq:
                lista[i] = lista_esq[pos_esq]
                pos_esq += 1
                i += 1

            # Copia os elementos que sobraram na direita, se houver
            while pos_dir < tam_dir:
                lista[i] = lista_dir[pos_dir]
                pos_dir += 1
                i += 1

            # Avança para o próximo par de sublistas
            esq += tam_part * 2

        # Dobra o tamanho das sublistas para a próxima rodada
        tam_part *= 2

    # Retorna a própria lista, agora ordenada
    return lista

############################################################

nums = [7, 0, 9, 2, 8, 4, 6, 1, 5, 3]

# Esta versão iterativa MODIFICA a lista original
merge_sort(nums)

print(nums)
