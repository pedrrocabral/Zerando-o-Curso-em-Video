# <-- Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o Primeiro Número: '))
num2 = int(input('Digite o Segundo Número: '))
num3 = int(input('Digite o Terceiro Número: '))
num = [num1, num2, num3]
print(f'O Maior Número é: {max(num)}')
print(f'O Menor Número é: {min(num)}')