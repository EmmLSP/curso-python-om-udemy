# Exercício - Jogo da palavra secreta

"""
Faça um jogo para o usuario adivinhar qual a palavra secreta.
- Voce vai propor uma palavra secreta qualquer e vai dar a 
possibilidade para o usuario digitar apenas uma letra.
- Quando o usuario digitar uma letra, voce vai conferir se a
letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba
    a letra; 
    - Se a letra digitada nao estiver na palavra secreta, 
    exiba *.
Faca a contagem de tentativas do seu usuario.
"""

import os
from time import sleep

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0
while True:
    letra_digitada = input('Digite uma letra: ').lower()
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
        
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('-' * 30)
        print('Você GANHOU! Parabens!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas: {numero_tentativas}x')
        letras_acertadas = ''
        numero_tentativas = 0
        print('-' * 30)
        sair = input('Quer continuar? ').lower().startswith('n')
        if sair is True:
            print('Finalizando programa...')
            sleep(1)
            break
        
