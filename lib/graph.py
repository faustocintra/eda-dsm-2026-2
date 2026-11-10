class Graph:
    """
    ESTRUTURA DE DADOS GRAFO
    Trata-se de uma estrutura de dados não linear, formada
    por vértices (ou nodos) e arestas (ou arcos). Sua principal
    finalidade é representar as relações entre diferentes
    entidades. Tais relações podem ser bidirecionais, resultando
    em grafos não direcionados, ou então unidirecionais,
    constituindo grafos direcionados (digrafos). Entre suas
    aplicações, estão representações de redes de computadores,
    mapas, percuros e redes sociais.
    """
    def __init__(self, is_directed = False):
        """ Método construtor """
        self.__is_directed = is_directed    # O grafo é direcionado?
        self.__data = {}    # Dicionário vazio

    def add_vertex(self, val):
        """ 
        Método que adiciona um novo vértice ao grafo
        """
        # Verifica se o vértice já existe no dicionário. A criação
        # somente será efetivada caso ainda não exista
        if not val in self.__data:
            self.__data[val] = set()    # Conjunto vazio

    def add_edge(self, origin, dest):
        """
        Método que adiciona uma aresta ao grafo. Utiliza as 
        seguintes informações:
        * origin ~> vértice de origem da aresta
        * dest ~> vértice de destino da aresta
        """
        # Cria os vértices de origem e destino, caso ainda
        # não existam
        if not origin in self.__data: self.add_vertex(origin)
        if not dest in self.__data: self.add_vertex(dest)

        # Monta a aresta origin --> dest
        # Adiciona a aresta origin --> dest
        self.__data[origin].add(dest)

        # Se o grafo não for direcionado, devemos também
        # adicionar uma aresta no sentido oposto, isto é,
        # dest --> origin
        if not self.__is_directed:
            self.__data[dest].add(origin)

    def remove_edge(self, origin, dest):
        """
        Método que remove uma aresta do grafo, tendo sido
        fornecedos o vértice de origem e o vértice de destino
        """
        # Retira dest do conjunto de arestas do vértice de origem
        self.__data[origin].discard(dest)

        # Se o grafo NÃO FOR direcionado, precisamos também
        # remover a aresta em sentido contrário
        if not self.__is_directed:
            self.__data[dest].discard(origin)

    def __get_degree(self, vertex):
        """
        Método PRIVADO que retorna o grau (número de arestas que entram
        ou saem) de um vértice
        """
        total = 0

        # GRAU DE SAÍDA (OUT-DEGREE)
        # É determinado contando-se o número de itens associados à entrada
        # de dicionário correspondente ao vértice
        if vertex in self.__data: total = len(self.__data[vertex])

        # GRAU DE ENTRADA (IN-DEGREE)
        # É determinado procurando-se referências ao vértice nos conjuntos
        # de adjacência associados a cada um dos vértices no dicionário
        for v in self.__data.keys():    # Percorre o dicionário (vértices)
            for s in self.__data[v]:    # Percorre os conjuntos (arestas)
                if vertex == s: total += 1

        # O grau total é a soma dos graus de entrada e de saída
        return total

    def remove_vertex(self, vertex):
        """
        Método que exclui um vértice do grafo.
        Para que essa operação seja possível, o vértice precisa ter
        grau 0 (nenhuma aresta saindo ou entrando nele)
        """
        degree = self.__get_degree(vertex)
        if degree > 0:
            raise Exception(f"ERRO: impossível remover um vértice cujo grau seja maior que zero (grau encontado: {degree})")
        if vertex in self.__data: del self.__data[vertex]

    def __str__(self):
        """
        Método que cria uma representação do grafo como string
        """
        output = f"** Grafo é direcionado? {self.__is_directed}\n"
        output += str(self.__data) + "\n"
        output += ("-" * 80) + "\n"
        return output
    
#####################################################################