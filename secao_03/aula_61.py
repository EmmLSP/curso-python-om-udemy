# Exercício - Gerar o primeiro dígito de um CPF com Python

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

""" print('-=' * 20)
print(f'    Calculo do primeiro dígito do CPF')
print('-=' * 20)

cpf = input('CPF: ')

nove_digitos = cpf[:9]
print(nove_digitos)

valor = soma = resultado = 0
for i, digito in enumerate(nove_digitos):
    valor = (10 - i) * int(digito)
    soma += valor

soma *= 10
resto = soma % 11

if resultado > 9:
    resultado = 0
else:
    resultado = resto
print(f'O primeiro digito do CPF é {resultado}') """

cpf = '74682489070'
nove_digitos = cpf[:9] # 0/8
contador_regressivo_1 = 10

resultado_digito_1 = digito_1 = resultado = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += contador_regressivo_1 * int(digito_1)
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11

if digito_1 > 9:
    resultado = 0
else:
    resultado = digito_1
print(f'O primeiro digito do CPF é {resultado}')
