# Precedência entre os operadores aritméticos

# 1. (n + n) -> resolve primeiro parenteses de dentro para fora
# 2. **
# 3. * / // %
# 4. + -
conta_1 = 1 + 1 ** 5 + 5 # 1 + 1 + 5 == 7
print(conta_1)
conta_2 = (1 + 1) ** (5 + 5) # 2 ** 10 == 1024
print(conta_2)
conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 2 ** 10 ==
print(conta_3)
