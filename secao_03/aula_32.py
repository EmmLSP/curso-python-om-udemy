# Exercícios - Enunciados

'''
1. Faca um programa que peca ao usuario para digitar um entrada inteiro,
informe se este numero é par ou impar. Caso o usuario nao digite um entrada
inteiro, informe que nao é um entrada inteiro.
'''

# A função isdigit() em Python é um método de strings que verifica 
# se todos os caracteres da string são dígitos (0–9).

entrada = input('Digite um entrada inteiro: ')
# if entrada.isnumeric() and entrada not in '.':
if entrada.isdigit():
    num_int = int(entrada)
    par_impar = num_int % 2 == 0
    par_impar_text = 'impar' # flag
    print('O número ', end='')
    if par_impar: # True
        par_impar_text = 'par'
        print(f'{num_int} é {par_impar_text}')
    else:
        print(f'{num_int} é {par_impar_text}')
else:
    print('Você nao digitou um numero inteiro')

entrada = input('Digite um entrada inteiro: ')
if entrada.isdigit():
    num_int = int(entrada)
    par_impar = num_int % 2 == 0
    par_impar_text = 'impar'
    if par_impar:
        par_impar_text = 'par'
    print(f'O número {num_int} é {par_impar_text}')
else:
    print('Você nao digitou um numero inteiro')

entrada = input('Digite um entrada inteiro: ')
try:
    num_int = int(entrada)
    par_impar = num_int % 2 == 0
    par_impar_text = 'impar'
    if par_impar:
        par_impar_text = 'par'
    print(f'O número {num_int} é {par_impar_text}')
except:
    print('Você nao digitou um numero inteiro')

'''
2. Faca um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudacao apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
'''

entrada = input('Digite a hora em numero inteiro: ')
if entrada.isdigit(): # 0-9
    hora = int(entrada)
    if 0 <= hora <= 11:
        print('Bom dia')
    elif 12 <= hora <= 17:
        print('Boa tarde')
    elif 18 <= hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
else:
    print('Por favor, digite apenas numeros inteiros e naturais')

entrada = input('Digite a hora em numero inteiro: ')
try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas numeros inteiros')

'''
3. Faca um programa que peca o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva  "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Se nome é normal"; maior que 6 escreva "Seu nome é muio grande".
'''

nome = input('Digite o seu nome: ')
qtd_letras = len(nome)
if qtd_letras <= 4:
    print('Seu nome é curto!')
elif qtd_letras in range(5, 7):
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')

nome = input('Digite o seu nome: ')
qtd_letras = len(nome)
if qtd_letras > 1:
    if qtd_letras <= 4:
        print('Seu nome é curto!')
    elif 5 <= qtd_letras <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Digite mais de uma letra')
