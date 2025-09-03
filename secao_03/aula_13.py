# Uma introdução às f-strings (formatação de strings)

nome = 'Emmanuel'
altura = 1.71
peso = 132
# formula -> IMC = peso / (altura²)
imc = peso / altura ** 2
"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)
print(...) # Ellipsis
