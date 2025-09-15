# Listas dentro de listas (iteráveis dentro de iteráveis)

"""
Lista de listas e seus indices
"""

salas = [
    # 0        1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine'], # 1
    # 0       1       2
    ['Luiz', 'Joao', 'Eduarda']] # 2

for sala in salas:
    print(f'A sala é {sala}:')
    for aluno in sala:
        print(aluno, end=' ')         
    print()

print('-=' * 15)

salas = [
    # 0        1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine'], # 1
    # 0       1       2          3
    #                                   2
    ['Luiz', 'Joao', 'Eduarda', (0, 10, 20, 30, 40)]] # 2

""" print(salas)
print(salas[1])
print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3])
print(salas[2][3][2]) """

for sala in salas:
    print(f'A sala é {sala}:')
    for i, item in enumerate(sala):
        if i < 3:
            print(item, end=' ')
        else:
            print()
            print(f'Numeros da tupla: {item}')
            for n in item:
                print(n, end=' ')
    print()
