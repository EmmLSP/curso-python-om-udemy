# Exercício: teste seu conhecimento até aqui

'''
Exercicio
Peca ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contem (ou nao) espações
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba 'Desculpe, você deixou campos vazios.'
'''
nome = input('Digite o seu nome: ') # se der enter o valor de nome for '' sera False
idade = input('Digite sua idade: ') # se der enter o valor de idade for '' sera False

if nome and idade: # True se o valor de nome e idade nao for '' vazio
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contem espaços')
    else:
        print(f'Seu nome NAO contem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios.')
