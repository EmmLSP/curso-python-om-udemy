# range + for para usar intervalos de números
# range() -> funcao que e um interavel
# iteravel -> while, for passando por uma string, lista, array

"""
For + range
range -> range(start, stop, step)
"""

numeros = range(10)
for numero in numeros:
    print(numero)
print('-' * 10)

numeros = range(5, 10)
for numero in numeros:
    print(numero)
print('-' * 10)

numeros = range(5, 10, 2)
for numero in numeros:
    print(numero)
print('-' * 10)

numeros = range(0, 10, 2)
for numero in numeros:
    print(numero)
print('-' * 10)

numeros = range(10, -1, -2)
for numero in numeros:
    print(numero)
print('-' * 10)

numeros = range(0, -11, -2)
for numero in numeros:
    print(numero)
print('-' * 10)

# todos numeros pares de 0 a 100
numeros = range(0, 101, 2)
for numero in numeros:
    print(numero)
print('-' * 10)

# multiplo de 8 de 0 a 100
numeros = range(0, 101, 8)
for numero in numeros:
    print(numero)
