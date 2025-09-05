# Fatiamento de strings e a função len

'''
Fatiamento de strings
strings sao iteraveis
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len() return qtd
de caracteres da str 
Em Python geralmente indice final
nao e incluido
Ex.: variavel[4:8] -> ignora 8
e mostra ate 7
'''

variavel = 'Olá mundo'
print(variavel[1])
print(variavel[-8])
print(variavel[5])
print(variavel[-4])
# fatiamento
print(variavel[4:])
print(variavel[4:8])
print(variavel[0:5]) # Olá m
print(variavel[:5]) # Olá m
print(variavel[-8:-2]) # lá mun
# len()
print(len(variavel[3])) # ' '
print(len(variavel))
print(variavel[0:9:1])
print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print(variavel[::-1]) # odnum álO
print(variavel[-1:-10:-1]) # odnum álO
print(variavel[-1:-9:-1]) # odnum ál
print(variavel[-1:-10:-2]) # onmáO
