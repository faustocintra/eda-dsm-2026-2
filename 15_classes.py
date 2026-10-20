"""
CLASSE é uma estrutura de dados que representa simultaneamente
dados e algoritmos que operam sobre esses dados. Uma classe pode
ser comparada a uma "assadeira" com a qual se pode produzir
diferentes tipos de iguarias assadas (ou não), variando os
"ingredientes" (dados) da receita e o "modo de fazer" (algoritmos).
Apesar dessas variações, todos os objetos ("assados") criados a
partir de uma mesma classe terão sempre algumas características
comuns, impostas por ela.
"""
from math import pi

class FormaGeometrica:
    """
    Por convenção, nomes de classe em Python seguem o formato
    PascalCase (primeira letra de cada palavra em maiúscula).
    Uma classe pode ter, dentro de si, tanto dados quanto funções
    (estas, implementando os algoritmos). Uma função especial,
    chamada __init___, é invocada sempre que se tenta criar um
    novo objeto a partir da classe. Essa função especial é
    conhecida como MÉTODO CONSTRUTOR.
    No contexto de classes e programação orientada a objetos:
    ~> funções passam a ser chamadas de MÉTODOS. Em Python, o
       primeiro parâmetro de todo método é sempre "self", o qual
       representa o próprio objeto
    ~> variáveis passam a ser chamadas ATRIBUTOS
    """

    def __init__(self, base, altura, tipo):
        """ Método construtor """
        # Em Python, a forma de indicar que um atributo é PRIVADO
        # é iniciando seu nome com duplo sublinhado (bizarro!)
        # self.__base = base
        # self.__altura = altura
        # self.__tipo = tipo

        # Chamamos os setters para configurar os valores iniciais
        # dos atributos privados no construtor. Dessa forma, as 
        # validações também serão executadas no ato de instanciação
        # de qualquer objeto da classe
        self.set_base(base)
        self.set_altura(altura)
        self.set_tipo(tipo)

    # Getters e setters
    def get_base(self):
        return self.__base
    
    def set_base(self, val):
        if type(val) not in [int, float] or val <= 0:
            raise Exception("ERRO: atributo 'base' deve ser numérico e maior que zero.")
        self.__base = val
    
    def get_altura(self):
        return self.__altura
    
    def set_altura(self, val):
        if type(val) not in [int, float] or val <= 0:
            raise Exception("ERRO: atributo 'altura' deve ser numérico e maior que zero.")
        self.__altura = val
    
    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, val):
        if val not in ["R", "T", "E"]:
            raise Exception("ERRO: atributo 'tipo' deve ser 'R', 'T' ou 'E'.")
        self.__tipo = val

    def calc_area(self):
        """
        Método que calcula a área com base no valor dos atributos da forma
        """
        match self.get_tipo():
            case "R":       # Retângulo
                return self.get_base() * self.get_altura()
            case "T":       # Triângulo
                return self.get_base() * self.get_altura() / 2
            case "E": 
                return (self.get_base() / 2) * (self.get_altura() / 2) * pi
            # Não há necessidade de nenhum outro caso, já que outros valores
            # para o atributo self.__tipo não são aceitos


#####################################################################

# Criando um objeto a partir da classe FormaGeometrica
forma1 = FormaGeometrica(12.5, 14, "R")

print("VALORES ORIGINAIS DOS ATRIBUTOS")
print(f"Base: {forma1.get_base()}")
print(f"Altura: {forma1.get_altura()}")
print(f"Tipo: {forma1.get_tipo()}")
print(f"Área: {forma1.calc_area()}")

print("-" * 80)

# Os valores dos atributos podem ser alterados após a instanciação
# do objeto
forma1.set_base(8)
forma1.set_altura(6)
forma1.set_tipo("T")

print("VALORES ALTERADOS POSTERIORMENTE")
print(f"Base: {forma1.get_base()}")
print(f"Altura: {forma1.get_altura()}")
print(f"Tipo: {forma1.get_tipo()}")
print(f"Área: {forma1.calc_area()}")