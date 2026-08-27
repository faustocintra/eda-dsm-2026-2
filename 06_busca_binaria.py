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