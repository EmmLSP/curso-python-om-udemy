# Operação ternária com Python (if e else de uma linha)

"""
Operacao ternaria (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

print('Valor' if True else 'Outro valor')
print('Valor' if False else 'Outro valor')

condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 9 # > 9 = 0
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito # condicional invertida
print(novo_digito)

# operacao ternaria nao recomendada
print('Valor' if True else 'outro valor' if False else 'fim')
print('Valor' if False else 'outro valor' if True else 'fim')
print('Valor' if False else 'outro valor' if False else 'fim')
