"""
CLASSE é uma estrutura de dados que representa simultaneamente
dados e algoritmos que operam sobre esses dados. Uma classe
pode ser comparada a uma "assadeira", com a qual se pode
produzir diferentes tipos de iguarias assadas (ou não),
variando os "ingredientes" (dados) da receita e o "modo de fazer"
(algoritmos). Apesar dessas variações, todos os objetos
("iguarias") criados a partir de uma classe terão sempre algumas
características comuns, impressas por ela.
"""
class FormaGeometrica:
    """
    Por convenção, nomes de classes em Python seguem o formato
    PascalCase (primeira letra de cada palavra em maiúscula).
    Uma classe pode ter, dentro de si, tanto dados quanto funções
    (estas, implementando os algoritmos). Uma função especial,
    chamada __init__(), é invocada sempre que se tenta criar um
    objeto a partir da classe. Essa função especial é conhecida
    como MÉTODO CONSTRUTOR.
    No contexto de classes e programação orientada a objetos:
    ~> funções passam a ser chamadas MÉTODOS. Em Python, o primeiro
       parâmetro de todo método é sempre "self", que representa
       o próprio objeto.
    ~> variáveis passam a ser chamadas ATRIBUTOS.
    """
    def __init__(self, base, altura, tipo):
        self.base = base
        self.altura = altura
        self.tipo = tipo

#####################################################################

# Criando uma forma geométrica como objeto (instância)
# da classe FormaGeometrica
forma1 = FormaGeometrica(12, 14, "R")

print(forma1)
print("Base:  ", forma1.base)
print("Altura:", forma1.altura)
print("Tipo:  ", forma1.tipo)