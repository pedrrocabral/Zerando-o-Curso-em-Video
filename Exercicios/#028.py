# <--   Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número
#       inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
#       pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep
from random import randint

print(20 * '-=-')
print('vou pensar em um número de 0 a 5. Tente adivinhar...'.title())
print(20 * '-=-')
user = int(input('Qual número eu pensei? '.title()))
print('PROCESSANDO....')
sleep(2)
num = randint(0, 5)
print('PARABÉNS! Você Conseguiu me Vencer!' if user == num else 'Você Perdeu!')