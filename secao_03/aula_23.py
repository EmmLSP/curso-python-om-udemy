# Operador logico "not"
# Usado para inverter expressoes
# not True = False
# not False = True

'''senha = input('Senha: ')

if senha == '123456':
    print('Entrou')
else:
    print('Senha incorreta.')'''

senha = input('Senha: ')

# a negacao de False e True
# not False = True
if not senha:
    print('Voce nao digitou nada.')

print(f'not True = {not True}') # False
print(f'not False = {not False}') # True
print(f'not 0 = {not 0}') # True
print(f'not 1 = {not 1}') # False
print(f'not 0.0 = {not 0.0}') # True
print(f'not "" = {not ''}') # True
