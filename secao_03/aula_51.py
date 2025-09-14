# Introdução ao empacotamento e desempacotamento

"""
Introdução ao desempacotamento
"""

# nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz']
# ValueError: not enough values to unpack (expected 4, got 3)
# print(nome2)

# nome1, nome2 = ['Maria', 'Helena', 'Luiz']
# ValueError: too many values to unpack (expected 2)
# print(nome2)

# *_ usa-se como convencao para o resto,
# valores que nao vao ser utilizados

nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1, _)

_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(_, nome2, _)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto)
