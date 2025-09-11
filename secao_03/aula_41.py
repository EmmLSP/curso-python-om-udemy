# while / else (recurso peculiar do Python)

""" while/else """

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaco na string.')
print('Fora do while')
