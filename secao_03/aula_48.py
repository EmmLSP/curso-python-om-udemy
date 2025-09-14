# Tipo list - Introdução às listas mutáveis em Python

"""
Tipo de dado: lista
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis: append, insert, pop, del, clear, extend, +
"""

#        +01234
#        -54321
string = 'ABCDE' # 5 caracteres
# lista = list()
# lista = [] -> ''
# print(lista, type(lista))
# print(bool(lista)) -> False

#        0    1      2             3    4
#       -5   -4     -3            -2   -1
lista = [123, True, 'Luiz Otavio', 1.2, []]
print(lista)
print(lista[2])   # 'Luiz Otavio'
print(lista[-3])  # 'Luiz Otavio'
print(lista[2], type(lista[2]))
print(lista[-3], type(lista[-3]))
print(lista[2].upper())
print(lista[2].lower())

# Alterando valor durante a execucao
lista = [123, True, 'Luiz Otavio', 1.2, []]
print(lista)
print(lista[-3])
lista[-3] = 'Maria'
print(lista)
print(lista[-3])
