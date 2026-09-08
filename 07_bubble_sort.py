def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    TROCANDO entre si dois elementos adjacentes sempre que
    o SEGUNDO for MENOR do que o PRIMEIRO. Efetua tantas
    passadas quanto necessárias, até que, na última delas,
    nenhuma troca tenha sido necessária.
    """
    # Loop eterno; não há como determinar antecipadamente
    # quantas passadas serão necessárias
    while True:
        # Variável que controla se houve trocas na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso à cada posição
        for pos in range(len(lista) - 1):
            # Se o valor que está à frente (pos + 1) da posição
            # atual (pos) for MENOR do que este, é necessário
            # efetuar uma troca entre eles
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]

                # Marcamos que houve uma troca na passada ("passada suja")
                trocou = True

        # <~ CUIDADO COM A INDENTAÇÃO AQUI
        # Se não houve trocas na passada (ou seja, a passada está "limpa"),
        # significa que a lista está ordenada, podemos sair do loop eterno
        # e encerrar a função
        if not trocou: break

############################################################################

