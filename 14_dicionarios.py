"""
DICIONÁRIO é uma das estruturas de dados nativa da linguagem Python
capazes de armazenar múltiplos valores em uma única variável, por
meio de pares chave-valor (key-value).
Um dicionário é delimitado entre chaves {}. Diferentemente da lista,
que tem posições numeradas, o dicionário possui posições NOMEADAS
(chaves). Cada par chave-valor também é chamado de PROPRIEDADE.
"""
# Um dicionário com dados que representam uma pessoa
# As chaves são sempre strings.
# Os valores podem ser de qualquer tipo válido na linguagem Python.

pessoa = {
    # "chave": valor
    "nome": "Orozimbo Oliveira Osório",     # string
    "sexo": "M",                            # string
    "idade": 72,                            # int
    "peso": 76,                             # int
    "altura": 1.68,                         # float
    "aposentado": True,                     # bool
    "filhos": ["Zeferina", "Adamastor", "Gercina"]  # lista
}

# Acessando o valor das propriedades
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("É aposentado?", pessoa["aposentado"])

# Usando o valor das propriedades para efetuar um cálculo
# (no caso, o Índice de Massa Corporal - IMC)
imc = pessoa["peso"] / pessoa["altura"] ** 2

print(f"O IMC de {pessoa["nome"]} é {imc:.4f}")

################################################################

# Usando dicionários para representar formas geométricas

forma1 = {
    "base": 7.5,
    "altura": 3,
    "tipo": "T"         # Triângulo
}

forma2 = {
    "base": 5,
    "altura": 3.75,
    "tipo": "E"         # Elipse
}

forma3 = {
    "base": 60,
    "altura": 45,
    "tipo": "R"         # Retângulo
}

forma4 = {
    "base": "batata",
    "altura": False,
    "tipo": "T"
}

from math import pi

# Reimplementação da função calc_area() do arquivo 01. Agora, porém,
# as informações necessárias para efetuar o cálculo são recebidas
# em parâmetro único, na forma de dicionário
def calc_area(forma):
    match forma["tipo"]:
        case "R":       # Retângulo
            return forma["base"] * forma["altura"]
        case "T":       # Triângulo
            return forma["base"] * forma["altura"] / 2
        case "E":       # Elipse/círculo
            return (forma["base"] / 2) * (forma["altura"] / 2) * pi
        case _:         # FORMA DESCONHECIDA/INVÁLIDA
            return None


# Lista de formas para rodar os testes
formas = [forma1, forma2, forma3, forma4]

print("*" * 80)

for forma in formas:
    print(f"Base: {forma["base"]}")
    print(f"Altura: {forma["altura"]}")
    print(f"Tipo: {forma["tipo"]}")
    print(f"Área: {calc_area(forma)}")
    print("-" * 30)