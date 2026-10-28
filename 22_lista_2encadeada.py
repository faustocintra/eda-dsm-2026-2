from lib.dbl_linked_list import DblLinkedList

lista = DblLinkedList()

print(lista)

lista.insert(0, "Zero")
lista.insert(1, "Um")
lista.insert(2, "Dois")
lista.insert(3, "Três")
lista.insert(4, "Quatro")
lista.insert(5, "Cinco")
lista.insert(6, "Seis")
lista.insert(7, "Sete")

# Inserindo na última posição com 'push'
lista.push("Oito")

# Inserindo em uma posição intermediária
lista.insert(5, "Quatro e meio")

print(lista)

# Removendo o primeiro elemento
removido = lista.remove(0)

print("O SEGUINTE VALOR FOI REMOVIDO DO INÍCIO DA LISTA:", removido, "\n")
print(lista)

# Removendo o último elemento
# lista.pop() é um atalho para lista.remove(lista.count() - 1)
removido = lista.pop()
print("O SEGUINTE VALOR FOI REMOVIDO DO FIM DA LISTA:", removido, "\n")
print(lista)

# Removendo um nodo intermediário
removido = lista.remove(4)
print("O SEGUINTE VALOR FOI REMOVIDO DO MIOLO DA LISTA:", removido, "\n")
print(lista)

# Executando algumas consultas
primeiro = lista.peek(0)
elem_pos3 = lista.peek(3)
ultimo = lista.peek(lista.count() - 1)
print("PRIMEIRO ELEMENTO:", primeiro)
print("ELEMENTO NA POSIÇÃO 3:", elem_pos3)
print("ÚLTIMO ELEMENTO:", ultimo)