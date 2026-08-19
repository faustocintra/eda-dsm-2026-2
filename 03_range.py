"""
range() é uma função da linguagem Python que gera uma 
série (faixa) de números. É muito usada em associação
com listas e com a instrução "for".
"""

# 1) range() COM *1* PARÂMETRO
#    Gera uma faixa numérica que SEMPRE começa em 0
#    (zero) e termina no valor do parâmetro - 1
#    (mesmo raciocínio "exclusive" do fatiamento)
for num in range(10):
    print(num)

print("-" * 80)

# 2) range() com *2* PARÂMETROS
#    Gera uma faixa numérica que parte do valor do
#    primeiro parâmetro (inclusive) até o valor do
#    segundo parâmetro (exclusive)
for x in range(10, 18):
    print(x)

print("-" * 80)