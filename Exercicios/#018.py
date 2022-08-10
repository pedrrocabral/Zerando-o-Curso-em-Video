# <--   Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#       cosseno e tangente desse ângulo.

import math
x = float(input('Digite Seu Ângulo: '))
sin = math.sin(math.radians(x))
cos = math.cos(math.radians(x))
tan = math.tan(math.radians(x))
print(f'O Seno de {x}º é: {sin:.2f}')
print(f'O Cosseno de {x}º é: {cos:.2f}')
print(f'O Tangente de {x}º é: {tan:.2f}')