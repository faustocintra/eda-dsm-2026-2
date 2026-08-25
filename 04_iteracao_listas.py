frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# Para percorrer (iterar) uma lista e acessar apenas
# o valor dos respectivos elementos, usamos a
# estrutura de repetição for..in, conforme já visto
# no arquivo 02.
for f in frutas:
    print(f)

print("-" * 80)

# Iterando a lista em ordem inversa: reversed()
for f in reversed(frutas):
    print(f)

print("-" * 80)

# Contudo, é frequente precisar acessar, além do valor
# de cada elemento, também sua posição na lista. Nesse
# caso, podemos usar a estrutura for..in combinada com
# as funções range() e len()
print("Iteração mostrando a posição e o valor dos elementos:")
for pos in range(len(frutas)):
    print(f"Posição {pos} => {frutas[pos]}")

print("-" * 80)

# Às vezes, é necessário iterar a lista em ordem inversa,
# mas também tendo acesso às posições dos elementos. Para
# isso, usamos for..in combinado com as funções range()
# (com três parâmetros) e len()
print("Iteração reversa mostrando a posição e o valor dos elementos:")
for pos in range(len(frutas) - 1, -1, -1):
    print(f"Posição {pos} => {frutas[pos]}")