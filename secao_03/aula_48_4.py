# Concatenando e estendendo listas em Python

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
None - nao valor
polimorfismo de sinal de + -> pode ser somar, concatenar
+ -> return valor da concatenacao de listas
extend () -> nao return nada, return: None
"""

# + concatenar lista
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
# modifica na propria lista_a e nao return nada
lista_b.extend(lista_b)
print(lista_a)
