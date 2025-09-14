# Exercício - exiba os índices da lista (aula com solução)

"""
Exercicio
Exiba os indices da lista:
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']

for i in range(len(lista)):
    print(i, lista[i], type(lista[i]))

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
