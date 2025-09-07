# id - A identidade do valor que está na memória

'''
Flag (bandeira) - Marcar um local
None = nao valor
is e is not = é ou nao é (tipo, valor, identidade)
id = Identidade do objeto
'''

# identidade de um elemento na memoria
""" v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))
v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2)) """

# Flags, is, is not e None

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Não faca algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

# None == None
if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

# True != None
if passou_no_if is not None:
    print('Passou no if')
