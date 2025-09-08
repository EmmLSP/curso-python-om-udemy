# while e break - Estrutura de repetição

'''
Repetições
while (enquanto)
Executa uma acao enquanto uma condicao e verdadeira
Loop infinito -> quando um codigo nao tem fim
'''

condicao = True

while condicao:
    nome = input('qual e o seu nome: ').lower()
    if nome == 'sair':
        break
    print(f'Seu nome é {nome}')

print('Fim do Loop while!')
