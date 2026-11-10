from lib.graph import Graph

mapa = Graph()      # Não direcionado

# Criando dois vértices
mapa.add_vertex("Brasil")
mapa.add_vertex("Argentina")
print(mapa)

# Estabelecendo uma aresta entre os vértices criados
mapa.add_edge("Brasil", "Argentina")
print(mapa)

# Adicionando arestas com criação automática de vértices
mapa.add_edge("Bolívia", "Peru")
mapa.add_edge("Colômbia", "Venezuela")
print(mapa)

# Completando o mapa de fronteiras da América do Sul
mapa.add_edge("Brasil", "Uruguai")
mapa.add_edge("Brasil", "Paraguai")
mapa.add_edge("Brasil", "Bolívia")
mapa.add_edge("Brasil", "Peru")
mapa.add_edge("Brasil", "Colômbia")
mapa.add_edge("Brasil", "Venezuela")
mapa.add_edge("Brasil", "Guiana")
mapa.add_edge("Brasil", "Suriname")
mapa.add_edge("Brasil", "França")
mapa.add_edge("Argentina", "Uruguai")
mapa.add_edge("Argentina", "Chile")
mapa.add_edge("Argentina", "Paraguai")
mapa.add_edge("Argentina", "Bolívia")
mapa.add_edge("Bolívia", "Paraguai")
mapa.add_edge("Bolívia", "Chile")
mapa.add_edge("Peru", "Chile")
mapa.add_edge("Peru", "Equador")
mapa.add_edge("Peru", "Colômbia")
mapa.add_edge("Colômbia", "Equador")
mapa.add_edge("Venezuela", "Guiana")
mapa.add_edge("Guiana", "Suriname")
mapa.add_edge("Suriname", "França")
print(mapa)