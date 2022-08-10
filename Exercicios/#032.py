# <-- Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Qual ano você quer analizar? (Se desejar o ano atual digite 0) '))
atual = date.today().year

if ano == 0:
    ano = atual

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
