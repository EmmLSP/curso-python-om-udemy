# Inserindo itens em qualquer índice da lista com insert (Tipo list)

"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis:
    append - adiciona um item ao final
    insert - adiciona um item no indice escolhido
    pop - remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena lista
Create   Read   Update   Delete
Criar    Ler    Alterar  Apagar = lista[i] (CRUD)
Em Python tudo e objeto e os objetos tem metodos, acoes
argumentos sao valores que passam para os metodos em Python
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop() # apaga do final e return
print(lista, nome)
lista.append('Maria')
print(lista, lista.pop())
lista.append(12345)
print(lista)
# deletar ultimo elemento da lista
del lista[-1]
print(lista)
# limpar lista
lista.clear() 
print(lista)

#        0   1   2   3
lista = [10, 20, 30, 40]
# adiciona um elemento ao indice escolhido
lista.insert(4, 5)
# acessar ultimo indice 4
print(lista[4])
