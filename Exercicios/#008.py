# <--   Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em
#       centímetros e milímetros

x = int(input('Digite Um Valor em Metros (m): '))
print(f'{x} M são {x / 1000} KM')
print(f'{x} M são {x / 100} HM')
print(f'{x} M são {x / 10} DAM')
print(f'{x} M são {x * 10} DM')
print(f'{x} M são {x * 100} CM')
print(f'{x} M são {x * 1000} MM')
