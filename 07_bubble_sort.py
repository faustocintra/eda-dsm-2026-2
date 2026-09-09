# Variáveis de estatística
passd = comps = trocas = None

def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    TROCANDO entre si dois elementos adjacentes sempre que
    o SEGUNDO for MENOR do que o PRIMEIRO. Efetua tantas
    passadas quanto necessárias, até que, na última delas,
    nenhuma troca tenha sido necessária.
    """
    # Avisa à função para usar as variáveis globais definidas
    # na linha 2
    global passd, comps, trocas

    # Reseta o valor das variáveis
    passd = comps = trocas = 0

    # Loop eterno; não há como determinar antecipadamente
    # quantas passadas serão necessárias
    while True:
        # Cada iteração do loop corresponde a uma nova passada
        passd += 1

        # Variável que controla se houve trocas na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso à cada posição
        for pos in range(len(lista) - 1):
            # Se o valor que está à frente (pos + 1) da posição
            # atual (pos) for MENOR do que este, é necessário
            # efetuar uma troca entre eles

            # Cada if faz uma nova comparação
            comps += 1

            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]

                # Computamos a troca feita acima
                trocas += 1

                # Marcamos que houve uma troca na passada ("passada suja")
                trocou = True

        # <~ CUIDADO COM A INDENTAÇÃO AQUI
        # Se não houve trocas na passada (ou seja, a passada está "limpa"),
        # significa que a lista está ordenada, podemos sair do loop eterno
        # e encerrar a função
        if not trocou: break

############################################################################

nums = [7, 0, 9, 2, 8, 4, 6, 1, 5, 3]
print("--- CASO MÉDIO ---")
# Passadas: 7, comparações: 63, trocas: 26
print("Antes da ordenação:", nums)
bubble_sort(nums)
print("Após a ordenação:  ", nums)
print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}\n\n")

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("--- PIOR CASO ---")
# Passadas: 10, comparações: 90, trocas: 45
print("Antes da ordenação:", nums)
bubble_sort(nums)
print("Após a ordenação:  ", nums)
print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}\n\n")

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("--- MELHOR CASO ---")
# Passadas: 1, comparações: 9, trocas: 0
print("Antes da ordenação:", nums)
bubble_sort(nums)
print("Após a ordenação:  ", nums)
print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}\n\n")

################################################################################

# TESTE COM 10K NOMES

from time import time

import sys

# Desabilita a criação de cache otimizado de dados
sys.dont_write_bytecode = True  

from data.nomes_desord import nomes

# Apesar de a lista nomes_desord ter 1M+ de itens,
# vamos dar ao Bubble Sort só os primeiros 100K
nomes = nomes[:100000]

hora_ini = time()
bubble_sort(nomes)
hora_fim = time()

print(nomes)

print(f"Passadas: {passd}, comparações: {comps}, trocas: {trocas}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n\n")


