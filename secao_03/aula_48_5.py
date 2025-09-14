# Cuidados com tipos de dados mutáveis - list e copy

"""
Cuidados com dados mutaveis
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
garbage colet -> robo python limpar memoria
"""

# string -> dados imutaveis

nome = 'Luiz'
noutra_variavel = nome
nome = 'Joao'
print(nome)
print(noutra_variavel)

print('-' * 30)

# listas -> dados mutaveis

# lista_a e lista_b estao apontando
# para o mesmo lugar na memoria
lista_a = ['Luiz', 'Maria']
lista_b = lista_a
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

print('-' * 30)

# copy() -> copia elementos da lista_a
# para a lista_b
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
