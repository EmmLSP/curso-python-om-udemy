# if, elif e else: entendendo o fluxo do interpretador em condicionais

# if / elif      / else
# se / se nao se / se nao
# ... elipse
# pass -> passar para depois escrever codigo

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1: # se a condicao for verdadeira (True)
    print('Codigo para condicao 1!')
elif condicao2:
    print('Codigo para condicao 2!')
elif condicao3:
    print('Codigo para condicao 3!')
elif condicao4:
    pass
else:
    print('Nenhuma condição foi satisfeita!') 

if 10 == 10:
    print('Outro if')

print('Fora do if')
