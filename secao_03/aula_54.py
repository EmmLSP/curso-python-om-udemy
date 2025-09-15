# Exercício - crie uma lista de compras com listas

"""
Faca uma lista de compras com listas
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de indices inexistentes na lista.
"""

import os

lista = []

while True:
    print('Selecione uma opcao')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite numero inteiro.')
        except IndexError:
            print('Indice nao existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
 
""" import os

lista_compras = []
while True:
    print('Selecione uma opcao')
    opcao = input('[i]nserir [a]pagar [l]istar [c]lear [e]ncerrar: ')
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_compras.append(valor)
        continue
    elif opcao == 'a':
        indice = input('Escolha o indice para apagar: ')
        if indice.isnumeric():
            indice_int = int(indice)
            if 0 <= indice_int < len(lista_compras):
                lista_compras.pop(indice_int)
                print(f'Indice: {indice} apagado com suscesso!')
            else:
                print('indice fora de range')
                print('Indice Produtos:')
                # 0/9
                print('-' * (len(lista_compras) + len(lista_compras)-1))
                for indice, valor in enumerate(lista_compras):
                    print(indice, end=' ')
                print()
                print('-' * (len(lista_compras) + len(lista_compras)-1))
                print('Não foi possivel apagar este indice')
        else:
            print('Digite um numero para o indice')
    elif opcao == 'l':
        if len(lista_compras) == 0:
            os.system('cls')
            print('Nada para listar')
            os.system('cls')
        # o for nao itera numa lista vazia
        for indice, valor in enumerate(lista_compras):
            print(indice, valor)
        continue
    elif opcao == 'c':
        os.system('cls')
        continue
    elif opcao == 'e':
        sair = input('Deseja continuar? [s/n] ').startswith('n')
        if sair is True:
            break
        os.system('cls')
        continue
    else:
        print('Por favor, escolha i, a ou l.')

print('Fim do programa') """
