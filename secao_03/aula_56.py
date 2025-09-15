# split, join e strip são métodos muito úteis da str

"""
split e join com list e str
split - divide uma string -> return (list)
join - une uma string
"""

frase = 'Olha so que, coisa interessante'
lista_palavras = frase.split()
print(lista_palavras)

frase = 'Olha so que, coisa interessante'
lista_palavras = frase.split(',')
print(lista_palavras)

frase = 'Olha so que, coisa interessante'
lista_palavras = frase.split(', ')
print(lista_palavras)

frase = '  Olha so que, coisa interessante   '
lista_palavras = frase.split(',')

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())
print(lista_palavras)

frase = '   Olha so que, coisa interessante   '
lista_palavras = frase.split()

for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()
print(lista_palavras)

print('-' * 30)
 
frase = '  Olha so que, coisa interessante  '
lista_palavras_crua = frase.split(',')

lista_frases_fixed = []
for i, frase in enumerate(lista_palavras_crua):
    lista_frases_fixed.append(lista_palavras_crua[i].strip())
print(lista_palavras_crua)
print(lista_frases_fixed)

frases_unidas = ''.join('abc')
print(frases_unidas)
frases_unidas = '-'.join('abc')
print(frases_unidas)

# passar como argumento somente iteravei
# listas, string, tuplas
frases_unidas = ', '.join(lista_frases_fixed)
print(frases_unidas)
