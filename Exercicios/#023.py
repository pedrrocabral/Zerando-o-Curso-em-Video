# <--   Exercício Python 023: Faça um programa que leia um número de 0 a 9999
#       e mostre na tela cada um dos dígitos separados.

x: str = input('Informe um Numero: ')
x: int = int(x)
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print('ANALISANDO O NUMERO....')
print(f'UNIDADE: {u}')
print(f'DEZENA: {d}')
print(f'CENTENA: {c}')
print(f'MILHAR: {m}')
