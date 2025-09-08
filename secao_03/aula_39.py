"""
Interando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio' # Iteraveis

nome = 'Maria Helena'
novo_nome = '' # variavel acumuladora
index = 0

while index < len(nome):
    letra = nome[index]
    novo_nome += f'*{letra}'
    index += 1
novo_nome += '*'
print(novo_nome)
