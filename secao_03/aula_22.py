# Operador Lógico "ou"

# Operadores logicos
# tabela verdade (e, ou, nao)
# and (e) or (ou) not (nao)
# or - Qualquer condicao verdadeira avalia
# toda a expressao como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressao inteira sera avaliada naquele valor.
# Sao considerados falsy (que vc ja viu)
# 0 0.0 '' False
# Tambem existe o tipo None que é
# usado para representar um nao valor

'''entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

# Avaliacao curto circuito -> entrada == 'E' or entrada == 'e'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')'''

# Avaliacao de curto circuito
print(True and 0 and True)
print(0 or False or 0 or 'abc')
print(0 or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)
