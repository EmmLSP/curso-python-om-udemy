# Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)

"""
Iterável -> str, range, etc -> (__iter__())
iteravel tem um metodo dentro dele chamado __iter__()
Iterador -> quem sabe entregar um valor por vez
next -> me entrega o seu proximo valor
iter -> me entrega seu iterador
"""

texto = 'Luiz'.__iter__()
print(texto)

texto = iter('Luiz') # __iter__()
print(texto)

texto = iter('Luiz') # __iter__()
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
# erro -> StopIteration
# print(texto.__next__())

texto = iter('Luiz') # __iter__()
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
# erro -> StopIteration
# print(next(texto))

# for letra in texto
texto = 'Luiz' # iteravel
interador = iter(texto) # iterador

while True:
    try:
        letra = next(interador)
        print(letra)
    except StopIteration:
        print('StopIteration')
        break

texto = 'Luiz'
for letra in texto:
    print(letra)
