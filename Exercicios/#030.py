# <--   Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um Número: '))
print(f'O número {num} é Par' if num % 2 == 0 else f'O número {num} é Ímpar')