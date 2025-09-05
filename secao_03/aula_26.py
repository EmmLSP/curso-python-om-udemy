# Formatação de strings com f-strings

'''
Formatacao basica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Forca o numero a aparecer antes dos zeros
Sinal - + ou -
Ex: 0>-100,.1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:>10}')
print(f'{variavel:<10}')
print(f'{variavel:^10}')
print(f'{variavel:$^10}')
print(f'{1000.4816511555:.1f}')
print(f'{1000.4816511555:,.1f}')
print(f'{1000.4816511555:+,.1f}')
print(f'{-1000.4816511555:+,.1f}')
print(f'{-1000.4816511555:-,.1f}')
print(f'{1000.4816511555:0=+11,.2f}')
print('>', 'O hexadecimal de %d é %04X' % (1500, 1500))
print(f'O hexadecimal de 1500 é {1500:04x}')
print(f'O hexadecimal de 1500 é {1500:04X}')
print('>', 'O hexadecimal de %d é %08X' % (1500, 1500))
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 1500 é {1500:08X}')
