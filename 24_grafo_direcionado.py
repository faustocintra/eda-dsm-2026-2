from lib.graph import Graph

familia = Graph(True)   # Grafo direcionado

familia.add_edge("Asdrúbal", "Adelma", "marido de")
familia.add_edge("Adelma", "Asdrúbal", "esposa de")

familia.add_edge("Asdrúbal", "Argemiro", "pai de")
familia.add_edge("Argemiro", "Asdrúbal", "filho de")

familia.add_edge("Asdrúbal", "Joaquim", "avô de")
familia.add_edge("Joaquim", "Asdrúbal", "neto de")

familia.add_edge("Asdrúbal", "Marialva", "sogro de")
familia.add_edge("Marialva", "Asdrúbal", "nora de")

familia.add_edge("Argemiro", "Marialva", "marido de")
familia.add_edge("Marialva", "Argemiro", "esposa de")

familia.add_edge("Argemiro", "Joaquim", "pai de")
familia.add_edge("Joaquim", "Argemiro", "filho de")

print(familia)

familia.visualize()

#familia.remove_vertex("Joaquim")