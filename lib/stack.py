class Stack:
    """
    ESTRUTURA DE DADOS PILHA
    Trata-se de uma estrutura de dados linear de acesso restrito,
    na qual tanto a operação de inserção (tradicionalmente
    chamada "push") quanto a operação de remoção ("pop") ocorrem
    no final (ou topo) da estrutura. Como consequência, o
    funcionamento da pilha obedece ao princípio LIFO (Last In,
    First Out): o último elemento a entrar é o primeiro a sair.    
    """
    def __init__(self):
        """ Método construtor """
        # Inicializa uma lista privada e vazia para armazenar
        # os elementos da pilha
        self.__data = []

    def push(self, val):
        """
        Método para inserção de dados na estrutura
        Garante que qualquer elemento inserido vá para o final
        (topo)
        """
        self.__data.append(val)

    def is_empty(self):
        """ Método que retorna se a pilha está ou não vazia """
        return len(self.__data) == 0
    
    def pop(self):
        """
        Método para remoção de dados na estrutura
        Garante que o valor ser removido será retirado sempre do
        final (topo)
        Emite erro caso seja feita uma tentativa de remoção em
        uma pilha vazia
        """
        if self.is_empty():
            raise Exception("ERRO: impossível remover de uma pilha vazia.")
        return self.__data.pop()
    
    def peek(self):
        """
        Método que permite saber o valor que se encontra no final (topo)
        da pilha sem, no entanto, removê-lo
        Emite erro caso seja feita uma tentativa de consulta em uma
        pilha vazia
        """
        if self.is_empty():
            raise Exception("ERRO: impossível consultar uma pilha vazia.")
        return self.__data[-1]      # -1 ~> último elemento
    
    def __str__(self):
        """ Método que permite exibir a pilha como uma string """
        return str(self.__data)
    
##################################################################################