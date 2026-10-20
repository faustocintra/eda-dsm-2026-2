"""
Programa simples que verifica o balanceamento de parênteses
em expressões matemáticas, usando a estrutura de dados pilha
"""
from lib.stack import Stack
pilha = Stack()

# Expressão balanceada
# expr = "5 - (2 * (3 + 4) - (5 / 3) + 1) * 2"

# Expressão desbalanceada (fecha mais que abre)
expr = "5 - (2 * (3 + 4) - (5 / 3)) + 1)) * 2"

# Expressão desbalanceada (abre mais que fecha)
expr = "5 - (2 * ((3 + 4) - (5 / 3) + 1) * (2"

# Percorre a expressão caractere a caractere, analisando
# cada um deles
for pos in range(len(expr)):
    match expr[pos]:
        # 1ª parte: percorre a expressão e EMPILHA as
        # posições onde foi encontrado o caractere "("
        case "(": pilha.push(pos)

        # 2ª parte: ao encontrar um caractere ")", 
        # tenta desempilhar, verificando se há um "("
        # correspondente
        case ")":
            if pilha.is_empty():
                print(f"* ERRO: ')' na posição {pos} não possui '(' correspondente")
            else:
                pos_abre = pilha.pop()
                print(f"'(' na posição {pos_abre} corresponde a ')' na posição {pos}")

# Verifica se há sobras na pilha, emitindo as mensagens de erro
# correspondentes
while not pilha.is_empty():
    pos_abre = pilha.pop()
    print(f"* ERRO: '(' na posição {pos_abre} não possui o ')' correspondente")