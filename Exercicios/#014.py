# <--   Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e
#       converta para graus Fahrenheit.

x = float(input('Digite a Temperatura em ºC: '))
print(f'{x} ºC São {x + 273.15} K')
print(f'{x} ºC São {(x * (9 / 5)) + 32} ºF')
