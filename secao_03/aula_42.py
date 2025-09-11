# while - Qual letra apareceu mais vezes na frase? (Iterando strings com while)
# caracteres no unicode -> letra maiscula, letra minuscula sao caracteres diferentes

""" frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossun.' """

# contar quantidade de vezes aparece str
# print(frase.count('Python'))

"""
i = 0
apareceu_mais_vezes = 0
letra_mais_rep = ''
while i < len(frase):
    letra = frase[i]
    qtd_caract = frase.count(letra)

    if letra == ' ':
        i += 1
        continue

    if i == 0:
        letra_mais_rep = letra
    else:
        if qtd_caract > frase.count(letra_mais_rep):
            apareceu_mais_vezes = qtd_caract
            letra_mais_rep = letra
    i += 1

print('A letra que apareceu mais vezes foi ' 
      f'"\033[1;32m{letra_mais_rep}\033[m", {apareceu_mais_vezes}x')

"""

""" frase = 'aaaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1

print('A letra que apareceu mais vezes foi '
    f'"\033[1;32m{letra_apareceu_mais_vezes}\033[m" que apareceu '
    f'{qtd_apareceu_mais_vezes}x.') """

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossun.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1

print('A letra que apareceu mais vezes foi '
    f'"\033[1;32m{letra_apareceu_mais_vezes}\033[m" que apareceu '
    f'{qtd_apareceu_mais_vezes}x.')
