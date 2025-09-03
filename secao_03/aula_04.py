# Tipos Primitivos - numeros: int e float

# Tipos int e float
# int -> Numero inteiro
# o tipo int representa qualquer numero
# positivo ou negativo. int sem sinal é
# considerado positivo

print(11) # int
print(-11) # int
print(0) # int

# float -> Numero com ponto flutuante
# O tipo float representa qualquer numero
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.

print(1.1, 10.11, sep='_') # float
print(0.0, -1.5, sep='_') # float 

# A funcao type() mostra o tipo que o Python
# inferiu o valor.
# tudo em Python é um objeto

name = 'Otavio'
print(name)
print(type(name))
# <class 'str'> -> class é um objeto do tipo string
num = 1
print(num)
print(type(num))
num = -1
print(num)
print(type(num))
num = 0
print(num)
print(type(num))
# <class 'int'> -> class e um objeto do tipo inteiro

print(type(1.1), type(-1.1), type(0.0))
