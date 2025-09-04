# Exercício de programação com if e comparação

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# python utiliza tabela unicode para fazer comparações strings
if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} e maior do {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} e maior do {primeiro_valor=}')
else:
    print(f'{primeiro_valor=} e igual ao {segundo_valor=}')
