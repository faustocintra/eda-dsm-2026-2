"""
Programa simples que inverte uma palavra informada pelo usuário
e verifica se ela é um PALÍNDROMO, isto é, uma palavra que pode
ser lida tanto da esquerda para a direita quanto da direita para
a esquerda, mantendo seu valor. Para tanto, usaremos uma estrutura
de dados pilha baseada na lista nativa da linguagem Python.
"""

# Pede para o usuário informar uma palavra e já converte o
# valor informado todo para minúsculas, para não interferir
# na posterior comparação
palavra = input("Informe a palavra a ser verificada: ").lower()

# Lista nativa do Python que será usada como pilha
pilha = []

# PARTE 1: PREENCHIMENTO DA PILHA
# Pega cada letra da palavra informada e a insere no final
# (topo) da pilha
for letra in palavra:
    # ATENÇÃO: se um método de inserção diferente de append()
    # for utilizado aqui, isso descaracterizará a pilha
    pilha.append(letra)     # Insere no final (topo)
    print(pilha)

print("-" * 80)

# PARTE 2: ESVAZIAMENTO DA PILHA
# Enquanto a pilha não estiver vazia, vamos retirar a letra
# que estiver no final (topo) e vamos adicionando-a à
# variável "inverso"
inverso = ""
while len(pilha) > 0:
    # ATENÇÃO: se um método de remoção diferente de pop()
    # (sem parâmetros) for utilizado aqui, a pilha será
    # descaracterizada
    letra = pilha.pop()     # Retira a letra do final (topo)
    inverso += letra        # Adiciona a letra ao inverso
    print("PILHA:  ", pilha)
    print("INVERSO:", inverso, "\n")

print("=" * 80)

# Comparação entre a palavra original e o seu inverso
if palavra == inverso:
    print(f"*** A palavra '{palavra}' É UM PALÍNDROMO ***")
else:
    print(f"!!! A palavra '{palavra}' NÃO É um palíndromo !!!")

    