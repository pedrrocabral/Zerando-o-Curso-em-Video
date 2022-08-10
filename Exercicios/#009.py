# <-- Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

x = int(input('Digite Um Valor: '))
print(10 * '_')
for i in range(1, 11):
    print(f'{x} x {i:2} = {x * i:2}')
print(10 * '_')
