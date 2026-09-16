def fatorial_iter(num):
    """ 
    Calcula o fatorial de um número natural (inteiro >= 0)
    usando uma abordagem ITERATIVA (não recursiva)
    """
    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível")

    resultado = 1
    for n in range(num, 0, -1): resultado *= n
    return resultado

#####################################################################

print(f"O fatorial (iterativo) de 6 é igual a {fatorial_iter(6)}.")

#--------------------------------------------------------------------

def fatorial_rec(num):
    """
    Calcula o fatorial de um número natural usando uma abordagem
    RECURSIVA
    """
    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível")

    if num in [0, 1]: return 1      # Condição de saída
    return num * fatorial_rec(num - 1)

#####################################################################

print(f"O fatorial (recursivo) de 6 é igual a {fatorial_rec(6)}.")