# Alterando uma lista com índices, del, append e pop (Tipo list)

"""
Tipo de dado: lista
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
numero = lista[2]
print(numero, type(numero), type(lista))

lista = [10, 20, 30, 40]
print(lista)
lista[2] = 300
print(lista)
print(lista[2])

lista = [10, 20, 30, 40]
lista[2] = 300
print(lista)
del lista[2]
print(lista)
print(lista[2])

# append() -> metodo add ao final da lista
lista = [10, 20, 30, 40]
print(lista)
remover_20 = lista.pop(1) # usar indice para remover usando pop(index)
print(lista, 'Removendo:', remover_20)
lista.append(50)
print(lista)
# pop() -> remove ultimo elemento da lista
lista.pop()
lista.append(60)
lista.append(70)
print(lista)
ultimo_valor = lista.pop()
print(lista, 'Removido:', ultimo_valor)
