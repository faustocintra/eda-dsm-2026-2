from dataclasses import dataclass

class DblLinkedList:
    """
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, sem restrição de acesso, em que
    seus elementos (chamados nodos ou nós) não estão fisicamente
    adjacentes uns aos outros, mas encadeados de forma lógica por
    meio de ponteiros que indicam a localização de memória do nodo
    anterior e do nodo seguinte da sequência. Inserções, exclusões
    e consultas podem ser realizadas em qualquer posição da lista.
    """

    @dataclass
    class Node:
        """
        Classe interna que apenas armazena dados (por isso, o
        decorator @dataclass), cujas instâncias representam as
        unidades de informação que integram a lista duplamente
        encadeada
        """
        prev: int | None    = None      # Ponteiro para o nodo anterior
        data: any           = None      # Qualquer dado, de qualquer tipo
        next: int | None    = None      # Ponteiro para o nodo seguinte
    #---------------------------------------------------------------------

    def __init__(self):
        """ Construtor da classe principal DblLinkedList """
        self.__head = None              # Ponteiro para o início da lista
        self.__tail = None              # Ponteiro para o fim da lista
        self.__count = 0                # Número de elementos na lista

    def insert(self, pos, val):
        """ Método que insere na posição 'pos' o valor 'val' """
        # Se a posição passada for negativa, emitimos um erro
        if pos < 0:
            raise Exception("ERRO: posição não pode ser negativa.")
        
        # Criamos um novo nodo para armazenar 'val' e também os ponteiros
        # 'prev' e 'next', ambos apontando inicialmente para None (ponteiros
        # aterrados)
        new = self.Node(data = val)

        # 1º caso: a lista está vazia, e 'new' é o primeiro nodo a ser
        # inserido. Portanto, ele se tornará, ao mesmo tempo, o primeiro e
        # o último nodo da lista
        if self.__count == 0:
            self.__head = new
            self.__tail = new

        # 2º caso: inserção no início da lista (posição 0)
        elif pos == 0:
            new.next = self.__head
            self.__head.prev = new
            self.__head = new

        # 3º caso: inserção no final da lista
        # OBS.: sempre que a posição passada para inserção for
        # >= count, interpretaremos como inserção no final
        elif pos >= self.__count:
            new.prev = self.__tail
            self.__tail.next = new
            self.__tail = new

        # 4º caso: inserção em posição intermediária.
        # Não temos acesso direto às posições intermediárias da lista.
        # Nesse caso, para encontrar o nodo na posição desejada, é
        # necessário partir de alguma das extremidades (__head ou __tail)
        # e percorrer a lista até encontrar o nodo que, no momento,
        # ocupa a posição onde o novo nodo deverá ser inserido. A busca
        # propriamente dita é feita pelo método __find_node().
        else:
            # Busca o nodo que atualmente ocupa a posição de inserção
            current = self.__find_node(pos)
            # Encontra o nodo anterior a 'current'
            before = current.prev
            # Efetua o encaixe do novo nodo posição desejada, sem quebrar
            # a lista
            before.next = new
            new.prev = before
            new.next = current
            current.prev = new
        
        # Incrementa o número de nodos da lista
        self.__count += 1

    def push(self, val):
        """ Método de atalho para inserir 'val' no fim da lista """
        self.insert(self.__count, val)

    def count(self):
        """ Método que retorna a quantidade de elementos da lista """
        return self.__count
    
    def remove(self, pos):
        """ Método que remove um nodo da lisda, dada sua posição """
        # 1º caso: lista vazia ou posição fora dos limites
        if self.__count == 0 or pos < 0 or pos >= self.__count:
            raise Exception("ERRO: posição inválida para exclusão.")
        
        # 2º caso: exclusão do início da lista
        if pos == 0:
            # Vamos remover o nodo apontado por __head
            being_removed = self.__head
            # O novo __head passa a ser o sucessor do nodo sendo removido
            self.__head = being_removed.next
            # Se o novo __head for um nodo válido, ele não pode ter um
            # antecessor
            if self.__head is not None: self.__head.prev = None
            # SITUAÇÃO ESPECIAL: em caso de remoção do último nodo restante
            # da lista, __tail também precisa passar a valer None
            if self.__count == 1: self.__tail = None

        # 3º caso: exclusão do fim da lista
        elif pos == self.__count - 1:
            # Vamos remover o nodo apontado por __tail
            being_removed = self.__tail
            # O novo __tail passa a ser o antecessor do nodo sendo removido
            self.__tail = being_removed.prev
            # O novo __tail (se for um nodo válido) não pode ter um sucessor
            if self.__tail is not None: self.__tail.next = None
        
        # 4º caso: exclusão de nodo intermediário
        else:
            # Pedimos a __find_node() para localizar o nodo a ser removido
            being_removed = self.__find_node(pos)
            # before = nodo anterior ao que está sendo removido
            before = being_removed.prev
            # after = nodo seguinte ao que está sendo removido
            after = being_removed.next
            # O nodo anterior ao que está sendo removido passa a apontar,
            # à frente, para o sucessor
            before.next = after
            # O nodo sucessor ao que está sendo removido passa a apontar,
            # para trás, para o antecessor
            after.prev = before

        # Decrementa a contagem de elementos da lista
        self.__count -= 1

        # Retorna o dado armazenado no nodo removido
        return being_removed.data

    def pop(self):
        """ Método de atalho para excluir o último nodo """
        return self.remove(self.__count - 1)

    def peek(self, pos):
        """ 
        Método que retorna o valor armazenado no nodo da posição
        especificada, sem removê-lo da lista
        """
        if self.__count == 0 or pos < 0 or pos >= self.__count:
            raise Exception("ERRO: posição inválida para consulta.")
        
        # Busca o nodo da posição para recuperar o respectivo valor
        # armazenado
        node = self.__find_node(pos)
        return node.data

    def __find_node(self, pos):
        """ Método PRIVADO para encontrar um nodo na posição dada """
        # 1º caso: posição 0, retorna self.__head
        if pos == 0: return self.__head

        # 2º caso: posição final (self.__count - 1), retorna self.__tail
        elif pos == self.__count - 1: return self.__tail

        # 3º caso: posição intermediária

        # Se 'pos' estiver na primeira metade da lista (< self.__count // 2),
        # faz o percurso de busca a partir de self.__head
        if pos < self.__count // 2:
            node = self.__head
            for _ in range(1, pos + 1): node = node.next

        # Senão, estando a posição na segunda metade da lista, faz o
        # percurso reverso a partir de self.__tail
        else:
            node = self.__tail
            for _ in range(self.__count - 2, pos - 1, -1): node = node.prev

        return node

    def __str__(self):
        """
        Método que gera uma representação da lista duplamente encadeada
        como uma string
        """
        if self.__count == 0: return "[*** LISTA VAZIA ***]\n\n"

        repr = f"*** LISTANDO {self.__count} ITEM(NS) ***\n"
        repr += f"Endereço do __head: {hex(id(self.__head))}\n"
        repr += f"Endereço do __tail: {hex(id(self.__tail))}\n"
        repr += ("=" * 80) + "\n"

        node = self.__head
        for pos in range(self.__count):
            repr += f"NODO posição {pos}, endereço {hex(id(node))}\n"
            repr += f"     [prev] Endereço do nodo anterior: {hex(id(node.prev))}\n"
            repr += f"     [data] DADO DO USUÁRIO: {node.data}\n"
            repr += f"     [next] Endereço do nodo seguinte: {hex(id(node.next))}\n"
            repr += ("-" * 80) + "\n"
            node = node.next

        repr += ("=" * 80) + "\n\n"
    
        return repr
    
####################################################################################
    