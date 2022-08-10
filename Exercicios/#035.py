# <--   Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao
#       usuário se elas podem ou não formar um triângulo.

seg1 = float(input('Seguimento nº1: '))
seg2 = float(input('Seguimento nº2: '))
seg3 = float(input('Seguimento nº3: '))
print('Os seguimentos acima PODEM FORMAR um triângulo'if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2 else 'Os seguimentos acima NÃO PODEM FORMAR um triângulo')