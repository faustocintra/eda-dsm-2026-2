# Nas linguagens de programação, normalmente, cada
# variável armazena um único valor

nome = "Orkutilson"
x = 10
altura = 1.74
aposentado = False

# LISTA é uma estrutura de dados nativa da linguagem
# Python. Ela permite que uma série de valores seja
# armazenada em uma única variável. Uma lista é
# delimitada por colchetes [].

# Lista de frutas
frutas = ["maçã", "morango", "laranja", "uva", "manga", "goiaba"]

# Lista de números primos
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Embora o mais comum seja que uma lista contenha valores de
# um mesmo tipo, não há impedimento para criar listas com
# valores de tipos diferentes
mistureba = ["Pafúncio", 37, 1.81, True]

#------------------------------------------------------------------
# OPERAÇÕES SOBRE LISTAS

# 1) PERCURSO
# Percorrer uma lista significa visitar cada um de seus elementos,
# geralmente do primeiro até o último, e fazer algo com cada elemento.

# Percorrendo a lista de frutas. Será dado print() em cada uma delas.
for elemento in frutas:
    print(elemento)

print("-" * 80)  # Traço separador

# Percorrendo a lista de números primos e exibindo cada valor elevado
# ao quadrado
for n in primos:
    print(n ** 2)

print("-" * 80)  # Traço separador

# 2) INSERÇÃO DE UM NOVO ELEMENTO NA LISTA

print("Lista de frutas, ANTES da inserção de um novo elemento no final:")
print(frutas)
print("Lista de números primos, ANTES da inserção de um novo elemento no final:")
print(primos)

# 2.1) Inserindo um novo elemento no FINAL da lista: append()
frutas.append("maracujá")
primos.append(37)

print("Lista de frutas, DEPOIS da inserção de um novo elemento no final:")
print(frutas)
print("Lista de números primos, DEPOIS da inserção de um novo elemento no final:")
print(primos)

print("-" * 80)  # Traço separador

# 2.2) Inserindo um novo elemento em uma posição específica: insert()
#      insert() espera dois parâmetros:
#      1º ~> posição na qual será feita a inserção (ATENÇÃO: a contagem
#            de posições SEMPRE COMEÇA EM ZERO)
#      2º ~> o novo elemento a ser inserido

# Inserindo um elemento na PRIMEIRA posição (posição 0)
frutas.insert(0, "melancia")
print("Lista de frutas após inserção na primeira posição:")
print(frutas)

print("-" * 80)  # Traço separador

# Inserindo um elemento na QUARTA POSIÇÃO (posição 3)
frutas.insert(3, "amora")
print("Lista de frutas após inserir 'amora' na posição 3 (QUARTA posição):")
print(frutas)

print("-" * 80)  # Traço separador

# 3) ACESSANDO OS VALORES DA LISTA POR SUA POSIÇÃO

print("Elemento da QUINTA posição:", frutas[4])
print("Elemento da PRIMEIRA posição:", frutas[0])
print("Elemento da ÚLTIMA posição:", frutas[-1])
print("Elemento da PENÚLTIMA posição:", frutas[-2])

print("-" * 80)  # Traço separador

# 4) SUBSTITUINDO VALORES EXISTENTES

print("Lista de frutas ANTES das substituições:")
print(frutas)

# Substituindo o valor da QUARTA posição
frutas[3] = "framboesa"
# Substituindo o valor da PRIMEIRA posição
frutas[0] = "pitanga"
# Substituindo o valor da ÚLTIMA posição
frutas[-1] = "melão"

print("Lista de frutas APÓS das substituições:")
print(frutas)

print("-" * 80)  # Traço separador

# 5) DETERMINANDO A QUANTIDADE DE ELEMENTOS DA LISTA: len()

print("Quantidade de elementos da lista de frutas:", len(frutas))
print("Quantidade de elementos da lista de números:", len(primos))

print("-" * 80)  # Traço separador

# 6) REMOVENDO ELEMENTOS DA LISTA

print("Lista de frutas, ANTES das remoções:")
print(frutas)

# 6.1) Remoção do ÚLTIMO elemento da lista: pop() (SEM parâmetro)

print("Removendo o último elemento...")
removido = frutas.pop()
print("Elemento removido:", removido)
print("Lista de frutas, após a remoção do último elemento:")
print(frutas)

print("-" * 80)  # Traço separador

# 6.2) Remoção de um elemento por sua POSIÇÃO: pop() (COM parâmetro)

print("Removendo o elemento da posição 5...")
removido = frutas.pop(5)
print("Elemento removido:", removido)
print("Lista de frutas, após a remoção do elemento na posição 5:")
print(frutas)

print("-" * 80)  # Traço separador

# 6.3) Removendo o elemento por seu VALOR: remove()

print("Removendo o elemento 'maçã'...")
frutas.remove("maçã")  # remove() não retorna valor
print("Lista de frutas, após a remoção do elemento 'maçã':")
print(frutas)

print("-" * 80)  # Traço separador

# 7) AUMENTANDO UMA LISTA COM ELEMENTOS DE OUTRA LISTA: extend()

mais_frutas = ["carambola", "pera", "acerola", "jabuticaba", "caqui"]
frutas.extend(mais_frutas)
print("Lista de frutas, estendida com os elementos de mais_frutas:")
print(frutas)

print("-" * 80)  # Traço separador

# 8) FATIANDO UMA LISTA
#    Fatiar significa copiar uma parte da lista (sublista),
#    criando uma nova lista. A lista original não é modificada.

# Cria uma nova lista com os elementos das posições de 3 a 7
# (posição 7 *NÃO* entra na lista)
sublista3a7 = frutas[3:7]
print("Sublista com elementos das posições 3 (inclusive) a 7 (exclusive):")
print(sublista3a7)

# Cria uma nova sublista com todos os elementos até a posição 5
# (posição 5 *NÃO* entra na lista)
sublista_ate5 = frutas[:5]
print("Sublista com os elementos desde o início até a posição 5 (exclusive):")
print(sublista_ate5)

# Cria uma nova sublista com todos os elementos da posição 5 até o final
# (posição 5 *ENTRA* na lista)
sublista_desde5 = frutas[5:]
print("Sublista com todos os elementos desde a posição 5 (inclusive) até o final:")
print(sublista_desde5)

