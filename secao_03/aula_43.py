# Introdução ao for / in - estrutura de repetição para coisas finitas
# while -> usado quando se sabe qtd de repeticoes, lacos
# for -> usado quando a qtd de lacos esta definida

# Exemplos com while

""" texto = 'Python'
i = 0
tamanho_string = len(texto)
while i < tamanho_string:
    print(texto[i])
    i += 1 

print('Fim do while') """

""" senha_salva = '123456'
senha_digitada = ''
repeticoes = 0
while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    repeticoes += 1

print(repeticoes)
print('aquele laco acima pode ter diversas repetições.') """

texto = 'Python'

for i in range(len(texto)):
    print(texto[i])
texto = 'Python'

for letra in texto:
    print(letra)

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

texto = 'Estou estudando Python'

vogais = ''
consoantes = ''
for letra in texto:
    if letra == ' ':
        continue
    if letra.lower() in 'aeiou':
        vogais += f'{letra} '
    else:
        consoantes += f'{letra} '
print(f'Vogais: {vogais}')
print(f'Consoantes: {consoantes}')
