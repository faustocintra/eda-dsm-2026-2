from enum import Enum

class Position(Enum):
    """ 
    Classe de enumeração que define a posição onde serão
    feitas as operações de inserção, remoção e consulta
    no deque
    """
    START = "start"
    END = "end"

class Deque:
    """
    ESTRUTURA DE DADOS DEQUE
    Deque (Doubly-Ended QUEue) é uma estrutura de dados
    derivada da fila, permitindo inserções e remoções em
    qualquer uma de suas extremidades. Com isso, o deque
    pode se comportar tanto como uma fila comum quanto como
    uma fila que admite inserções prioritárias (na primeira
    posição) quanto a possibilidade de remoção do último
    item (desistência).
    """

    def __init__(self):
        """ Método construtor """
        self.__data = []        # Lista vazia

    def insert(self, val, position):
        """ Método para inserção """
        if position == Position.START:
            self.__data.insert(0, val)
        elif position == Position.END:
            self.__data.append(val)
        else:
            raise Exception(f"ERRO: posição '{position}' inválida para inserção.")
        
    def is_empty(self):
        """ Retorna True se o deque estiver vazio, ou False, caso contrário """
        return len(self.__data) == 0
    
    def remove(self, position):
        """ Método para remoção """
        if self.is_empty():
            raise Exception("ERRO: impossível remover de um deque vazio.")
        if position == Position.START:
            return self.__data.pop(0)
        if position == Position.END:
            return self.__data.pop()
        raise Exception(f"ERRO: posição '{position}' inválida para remoção.")
    
    def peek(self, position):
        if self.is_empty():
            raise Exception("ERRO: impossível consultar um deque vazio.")
        if position == Position.START:
            return self.__data[0]
        if position == Position.END:
            return self.__data[-1]
        raise Exception(f"ERRO: posição '{position}' inválida para consulta.")
    
    def __str__(self):
        """ Retorna uma representação do deque como string """
        return str(self.__data)

##################################################################################        
        
    
