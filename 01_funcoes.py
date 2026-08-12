"""
Função que calcula o Índice de Massa Corporal (IMC) de uma pessoa, dados o
seu peso e a sua altura
"""
# Declaração da função
def imc(peso, altura):
  resultado = peso / altura ** 2  # ** é o operador de exponenciação
  return resultado

imc_pessoa1 = imc(78, 1.65) # Chamada de função
print("O IMC da Pessoa 1 é", imc_pessoa1)
print(f"O IMC da Pessoa 1 é {imc_pessoa1}") # print com f-string

print("O IMC da Pessoa 2 é", imc(104, 1.82))
print(f"O IMC da Pessoa 2 é {imc(104, 1.82)}")

#------------------------------------------------------------
# Retângulo: base * altura
# Triângulo: base * altura / 2
# Elipse/círculo: (base / 2) * (altura / 2) * pi

# Usando o pi da biblioteca math do Python
from math import pi

def calc_area(base, altura, tipo):
  """
  Função que calcula a área de uma forma geométrica plana, dadas
  as medidas da base e da altura e o tipo de forma
  """
  match tipo:
    case "R":   # Retângulo
      return base * altura
    case "T":   # Triângulo
      return base * altura / 2
    case "E":   # Elipse/círculo
      return (base / 2) * (altura / 2) * pi
    case _:     # Nenhuma das anteriores
      return None     # None = valor nulo no Python
  # if tipo == "R":
  #   return base * altura
  # elif tipo == "T":
  #   return base * altura / 2
  # elif tipo == "E":
  #   return (base / 2) * (altura / 2) * pi
  # else:
  #   return None

#--------------------------------------------------------------------

# Chamadas à função calc_area()
area_forma1 = calc_area(12, 17, "T")
print(f"Área de um triângulo 12x17: {area_forma1}")

area_forma2 = calc_area(10, 10, "E")
print(f"Área de um círculo 10x10: {area_forma2}")

area_forma3 = calc_area(16, 4.5, "R")
print(f"Área de um retângulo 16x4,5: {area_forma3}")

area_forma4 = calc_area(14, 12, "X")
print(f"Área de uma forma inválida/desconhecida: {area_forma4}")