from lib.deque import Deque, Position

# Instancia um novo deque
deque = Deque()

# PARTE 1: deque se comportando como uma fila comum

deque.insert("Antero",      Position.END)
deque.insert("Ermelinda",   Position.END)
deque.insert("Procópio",    Position.END)
deque.insert("Hermógenes",  Position.END)
deque.insert("Ivanilda",    Position.END)
deque.insert("Olentina",    Position.END)
print(deque)

removido = deque.remove(Position.START)
print(f"{removido} foi removido do início do deque.")
print(deque)

pessoa = "Tibúrcio"
deque.insert(pessoa,        Position.END)
print(f"{pessoa} foi inserido no final do deque.")
print(deque)

primeiro = deque.peek(Position.START)
print(f"{primeiro} é quem está no início do deque.")
print(deque)

print("-" * 80)

# PARTE 2: funcionalidades exclusivas do deque

# Inserção prioritária (na primeira posição)
pessoa = "Bartira"
deque.insert(pessoa,        Position.START)
print(f"{pessoa} foi inserida no início do deque.")
print(deque)

# Desistência (remoção do último item)
desistente = deque.remove(Position.END)
print(f"{desistente} foi removido do final do deque.")
print(deque)

# Consultando o último elemento do deque
ultimo = deque.peek(Position.END)
print(f"{ultimo}, no momento, é quem está no final do deque.")
print(deque)