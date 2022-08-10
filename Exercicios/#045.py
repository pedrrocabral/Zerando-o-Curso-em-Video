# <-- Exercício Python 045: Crie um programa que faça o computador jogar
#       Jokenpô com você.

from random import choice
from time import sleep

lista = [1, 2, 3]
while True:
    x = int(input('''Suas Opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual asua jogada? '''))
    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO !!!')
    y = choice(lista)
    if x == 1:
        print('\nVOCÊ JOGOU PEDRA')
        if y == 1:
            print('ROBO JOGOU PEDRA')
            print('\n-=-=-=-=-=-=-=-=-=-')
            print('\nEMPATE.. VAMOS DE NOVO')
            print('\n-=-=-=-=-=-=-=-=-=-')
            continue
        elif y == 2:
            print('ROBO JOGOU PAPEL')
            print('\n-=-=-=-=-=-=-=-=-=-')
            print('\nIHUULL.. GANHEI DE VOCÊ')
            print('\n-=-=-=-=-=-=-=-=-=-')
            break
        elif y == 3:
            print('ROBO JOGOU TESOURA')
            print('\n-=-=-=-=-=-=-=-=-=-')
            print('\nVOCÊ GANHOU.. PARABÉNS')
            print('\n-=-=-=-=-=-=-=-=-=-')
            break
    elif x == 2:
        print('\nVOCÊ JOGOU PAPEL')
        if y == 1:
            print('ROBO JOGOU PEDRA')
            print('\n-=-=-=-=-=-=-=-=-=-')
            print('\nVOCÊ GANHOU.. PARABÉNS')
            print('\n-=-=-=-=-=-=-=-=-=-')
            break
        elif y == 2:
            print('ROBO JOGOU PAPEL')
            print('\n-=-=-=-=-=-=-=-=-=-')
            print('\nEMPATE.. VAMOS DE NOVO')
            print('\n-=-=-=-=-=-=-=-=-=-')
            continue
        elif y == 3:
            print('ROBO JOGOU TESOURA')
            print('\n-=-=-=-=-=-=-=-=-=-')
            print('\nIHUULL.. GANHEI DE VOCÊ')
            print('\n-=-=-=-=-=-=-=-=-=-')
            break
    elif x == 3:
        print('\nVOCÊ JOGOU TESOURA')
        if y == 1:
            print('ROBO JOGOU PEDRA')
            print('\n-=-=-=-=-=-=-=-=-=-')
            print('\nIHUULL.. GANHEI DE VOCÊ')
            print('\n-=-=-=-=-=-=-=-=-=-')
            break
        elif y == 2:
            print('ROBO JOGOU PAPEL')
            print('\n-=-=-=-=-=-=-=-=-=-')
            print('\nVOCÊ GANHOU.. PARABÉNS')
            print('\n-=-=-=-=-=-=-=-=-=-')
            break
        elif y == 3:
            print('ROBO JOGOU TESOURA')
            print('\n-=-=-=-=-=-=-=-=-=-')
            print('\nEMPATE.. VAMOS DE NOVO')
            print('\n-=-=-=-=-=-=-=-=-=-')
            continue
    else:
        print('OPÇÃO INVALIDA.. ESCOLHA OUTRA VEZ')
