# Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string

# https://docs.python.org/3/library/stdtypes.html
# Built-in -> o que ja vem com Python
# Tipos Imutaveis que vimos: str, int, float, bool
# int, str, float, bool sao objetos, que realizam acoes

""" 
string = 'Luiz Otávio'
string[3] = 'ABC'
print(string[3])
TypeError: 'str' object does not support item assignment 
"""

string = 'Luiz Otavio'
outra_variavel = string # copia de string em outra_variavel
print(string[3])
print(outra_variavel[3])

string = 'Luiz Otavio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)

# Metodos de String
string = 'luiz Otavio'
print(string)
print(string.capitalize())
print(string.zfill(15))
