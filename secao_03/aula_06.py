# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
# Python é uma linguagem dinamica e forte 
# que idenfica o tipo de dado durante a interpretacao

# print('1' + 1)
# TypeError: can only concatenate str (not "int") to str

print(1 + 1) # soma de numeros iprintnteiros
print('a' + 'b') # concatenando duas strings

print('1', type('1'))
print(int('1'), type(int('1'))) # coercao, conversao
print(int('1') + 1)
print(float('1') + 1)
print(type(float('1') + 1))
print(bool('')) # string vazia, False
print(bool(' ')) # string nao vazia, True
print(str(11) + 'b') # coercao de int para str
