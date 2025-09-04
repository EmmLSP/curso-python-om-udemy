# Usando a função input para coletar dados do usuário
# input() -> coletar dados usuario
# sempre a funcao input() vai passar uma string, por isso
# e preciso fazer coerção, convercao de tipos de dados

'''nome = input('Qual é o seu nome? ')
print(f'O seu nome é {nome}')
print(f'O seu nome é {nome=}')'''

# se digitar uma letra quebra programa
numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))
print(f'A soma dos numeros é {numero_1 + numero_2}')

# possibilidade checagem de numeros
numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro numero: ')
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
print(f'A soma dos numeros é {int_numero_1 + int_numero_2}') 
