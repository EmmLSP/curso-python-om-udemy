# Tipo tuple (tuplas)

"""
Tipo tupla - Uma lista imutavel
Tuplas nao modem ser alteradas durante
a execucao do python, pq e imutavel
"""

""" 
nomes = 'Maria', 'Joao', 'Luiz'
nomes[1] = 'outro_nome'
TypeError: 'tuple' object does not support item assignment
print(nomes[1]) 
"""

# nomes = ('Maria', 'Helena', 'Luiz')
nomes = 'Maria', 'Helena', 'Luiz'
print(nomes[0])
print(nomes[-1])
print(nomes)

# conversao de tupla para lista
# e de lista para tupla
nomes = ('Maria', 'Helena', 'Luiz')
print(nomes)
nomes_list = list(nomes)
nomes_list[0] = 'Joana'
print(nomes_list)
del nomes_list[0]
nomes_list.insert(0, 'Maria')
nomes_tupla = tuple(nomes_list)
print(nomes_tupla) 

print('-' * 30)

nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)
print(nomes)
nomes = list(nomes)
print(nomes[-1])
print(nomes)
