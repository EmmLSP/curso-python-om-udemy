# Exercício guiado - Calculadora

# Calculadoa com while

""" while True:
    total = 0
    while True:
        num_1 = input('Digite um numero: ')
        if num_1.isdigit() or num_1.find('.'):
            break
        print('Náo é um numero valido')
    while True:
        num_2 = input('Digite outro numero: ')
        if num_2.isdigit() or num_2.find('.'):
            break
        print('Náo é um numero valido')
    num_1_float = float(num_1)
    num_2_float = float(num_2)
    while True:
        oper = input('Digite operador [+ - / *]: ')
        if oper in '+-/*':
            break 
        print('Operador invalido')
    if oper == '+':
        total = num_1_float + num_2_float
    elif oper == '-':
        total = num_1_float - num_2_float
    elif oper == '/':
        total = num_1_float / num_2_float
    elif oper == '*':
        total = num_1_float * num_2_float
    
    print('-' * 30)
    print(f'{num_1_float} {oper} {num_2_float} = {total}')
    print('-' * 30)

    sair = input('Quer continuar? [S/N] ').lower().startswith('n')
    if sair is True:
        break

print('<<< Fim do Programa >>') """

# .startwith() -> metodo string, comeca com
# .lower() -> metodo string, transforma tudo em minusculo
# continue -> volta para o inicio do while, laco

while True:

    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite o operador: [+ - / *] ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    # se der alguma excecao, erro aqui da True
    if numeros_validos is None:
        print('Um ou ambos os numeros digitados sao invalidos.')
        continue
    
    operadores_permitidos = '+-/*'

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    # se operador nao está entre em operadores permitidos
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    print('Realizando a sua conta. Confira o resultado abaixo:')
    total = 0
    if operador == '+':
      total = num_1_float + num_2_float
    elif operador == '-':
      total = num_1_float - num_2_float
    elif operador == '/':
      total = num_1_float / num_2_float
    elif operador == '*':
      total = num_1_float * num_2_float
    else:
       print('Nunca deveria chegar aqui.')

    print(f'{num_1_float} {operador} {num_2_float} = {total}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

print('saiu')
