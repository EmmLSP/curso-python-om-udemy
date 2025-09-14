# enumerate para enumerar valores de iteráveis (pegar índices)

"""
enumerate - enumera iteraveis (indices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

lista_enumerada = enumerate(lista)
# print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)

for k, v in enumerate(lista):
    print(k, v)

# converter enumerate para lista
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
lista_enumerada = tuple(enumerate(lista))
print(lista_enumerada)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR da Tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
