# funcao print(), usada para exibir coisas na tela
# funcao print() recebe algo () chamado argumento

'''
print(12, 34)
print(56, 78)
argumentos nao nomeados
'''

# argumentos nomeados (sep='', end='')
# sep='' separador
# \r\n (windows antigo) - CRFL -> quebra de linha padrao sistema windows
# \n (unix, mac) - LF -> quebra de linha padrao para sistema unix, mac
# end='' - quebra de linha final print()

print(12, 34, 1011, sep="-", end='\r\n')
print(56, 78, sep='-', end='##\n')
print(9, 10, sep='-', end='\n')
