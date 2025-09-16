# Desempacotamento em chamadas de funções

# Desempacotamento em chamadas
# de metodos e funcoes

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = ('Python', 'é', 'legal')

""" 
a, b, c, *_ = lista
print(a, c)

p, b, *_, ap, u = lista
print(p, ap, u) 
"""

# desempacotamento na chamada das funcoes

for nome in lista:
    print(nome, end=' ')
print()

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista) # * + iteravel
print(*string) # * + iteravel
print(*tupla) # * + iteravel

salas = [
    # 0        1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine'], # 1
    # 0       1       2
    ['Luiz', 'Joao', 'Eduarda'] # 2
]

print(salas)
print(*salas)
print(*salas, sep=', ')
print(*salas, sep='\n')
