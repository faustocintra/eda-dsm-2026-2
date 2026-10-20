# Importamos a classe Stack a partir do arquivo
# "stack.py" que está na pasta "lib"
from lib.stack import Stack

# Criamos uma nova pilha
p = Stack()

# Algumas inserções na pilha
p.push(1001)
p.push(1240)
p.push(1131)
p.push(1094)

# Exibindo a pilha
print("PILHA INICIAL:", p)

# Removendo um elemento da pilha
removido = p.pop()
print("Removido:", removido)
print("PILHA APÓS REMOÇÃO:", p)

# Conhecendo o elemento que está no topo da pilha
ultimo = p.peek()
print("Último:", ultimo)
print("PILHA APÓS CONSULTA:", p)