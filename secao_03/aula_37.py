# while + continue - pulando alguma repetição

'''
Repetições
while (enquanto)
Executa uma acao enquanto uma condicao e verdadeira
Loop infinito -> quando um codigo nao tem fim
continue -> pula o laco, volta para o inicio
break -> interromper o laco
'''

contador = 0

while contador < 100:
    contador += 1
    
    if contador == 6:
        print(f'\033[1;33mNão vou mostrar o 6\033[m')
        continue

    if contador >= 10 and contador <= 27:
        print(f'\033[1;33mNão vou mostrar o {contador}\033[m')
        continue

    print(f'\033[1;32m{contador}\033[m')
    
    if contador == 40:
        break

print('Acabou')
