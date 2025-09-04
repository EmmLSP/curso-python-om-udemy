# Operador Lógico "and"

# Operadores logicos
# tabela verdade (e, ou, nao)
# and (e) or (ou) not (nao)
# and - Todas as condicoes precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressao inteira sera avaliada naquele valor
# Sao considerados false (que vc ja viu)
# 0 0.0 '' False
# Tambem existe o tipo None que é
# usado para representar um nao valor

'''entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')'''

print(True and True)
print(True and True and True)
print(bool(0)) # return False
print(bool(0.0)) # return False
print(bool('')) # return False
# Avaliacao de curto circuito
print(True and False and True)
print(True and 0 and True)
# Avaliacao de curto circuito com return de False
# da funcao bool(0)
print(True and bool(0) and True) 
