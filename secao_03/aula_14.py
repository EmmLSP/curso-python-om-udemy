# Formatação de strings com o método format
# Em python tudo sao objetos, em objetos tem metodos
# Objetos tem acoes, que sao os metodos
# erro => index 3 out of range -> fora do intervalo
# string = 'a={0} b={1} c={2} {x}'

a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
print(formato)
string = 'a={0} a={0} a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)
print(formato)

# parametro nomeado
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)

