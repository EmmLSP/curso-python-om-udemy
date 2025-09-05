# Introdução ao try e except para capturar erros (exceptions)

'''
Introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar
executar o codigo 
'''

# input() sempre return uma string
numero_str = input('Vou dobrar o numero que voce digitar: ')

# numero_str -> objeto
print(numero_str.isdigit()) # True se for somente numeros

# tratar input() do usuario
'''
numero_float = float(numero_str)
print(f'O dobro de {numero_str} e {numero_float * 2:.0f}')
print(f'O dobro de {numero_str} e {numero_float * 2:.1f}')
print(f'O dobro de {numero_str} e {numero_float * 2:.2f}')
'''

# True se for somente numeros digitados
'''
if numero_str.isdigit(): 
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso não é um numero.')
'''

# Try / Except
# except -> erro, excecao
'''
try:
    ...
    pass
'''

try:
    # print(f'{type(numero_str)}: {numero_str}')
    numero_float = float(numero_str)
    print(f'{type(numero_float)}: {numero_float}')
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um numero.')
