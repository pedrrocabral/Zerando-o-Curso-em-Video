# <--   Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
#       que tipo de triângulo será formado:
#       - EQUILÁTERO: todos os lados iguais
#       - ISÓSCELES: dois lados iguais, um diferente
#       - ESCALENO: todos os lados diferentes

from os import system
system('cls')

seg1 = float(input('Seguimento nº1: '))
seg2 = float(input('Seguimento nº2: '))
seg3 = float(input('Seguimento nº3: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os seguimentos acima PODEM FORMAR um triângulo')
    if seg1 == seg2 == seg3:
        print('É um Triângulo EQUILÁTERO')
    elif seg1 == seg2 != seg3 or seg2 == seg3 != seg3 or seg3 == seg1 != seg2:
        print('É um Triângulo ISÓSCELES')
    elif seg1 != seg2 != seg3:
        print('É um Triângulo ESCALENO')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo')

