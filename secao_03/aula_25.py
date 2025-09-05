# Interpolação de string com % em Python

'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
placeholder -> qtd de %d %04x
'''

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preco é R$%8.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (1500, 1500))
print('O hexadecimal de %d é %04X' % (1500, 1500))
print('O hexadecimal de %d é %08x' % (1500, 1500))
print('O hexadecimal de %d é %08X' % (1500, 1500))
