# Exercício de programação - Cálculo do IMC (Índice de Massa Corpórea) + Ellipsis

nome = 'Emmanuel'
altura = 1.71
peso = 132
# formula -> IMC = peso / (altura²)
# imc = ... -> Ellipsis
# imc = peso / (altura * altura)
imc = peso / altura ** 2 # segue a ordem de precedencia

# Luiz Otavio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

print(f'{nome} tem {altura:.2f} de altura,')
print(f'pesa {peso} quilos e seu IMC é')
print(f'{imc:.2f}')
# print(...) # Ellipsis