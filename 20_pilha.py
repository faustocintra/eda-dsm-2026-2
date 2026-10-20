from lib.queue import Queue

# Inicializa uma fila
fila_ubs = Queue()

# Insere algumas pessoas na fila
fila_ubs.enqueue("Leonildes")
fila_ubs.enqueue("Otamar")
fila_ubs.enqueue("Waldisney")
fila_ubs.enqueue("Asdrúbal")

print(fila_ubs)

# Atende uma pessoa
atendido = fila_ubs.dequeue()
print(f"Foi atendido(a): {atendido}")
print(fila_ubs)

# Consulta o próximo a ser chamado
proximo = fila_ubs.peek()
print(f"{proximo} será o próximo a ser atendido")
print(fila_ubs)

# Mais duas pessoas chegaram na fila
fila_ubs.enqueue("Margarete")
fila_ubs.enqueue("Gervásio")
print(fila_ubs)

# Atende o primeiro da fila
atendido = fila_ubs.dequeue()
print(f"Foi atendido(a): {atendido}")
print(fila_ubs)