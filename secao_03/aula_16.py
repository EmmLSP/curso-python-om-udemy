# Introdução aos blocos de código + if / elif / else (condicionais)

# if / elif      / else
# se / se nao se / se nao

# string == objeto -> objeto tem metodos (.lower(), upper(), ...)
entrada = input('Você quer "entrar" ou "sair"? ').lower()
if entrada == 'entrar':
    print('Você entrou no sistema')
    print(123456789)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você nao digitou nem entrar e nem sair!')
print('FORA DOS BLOCOS')
