# <--   Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de
#       nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#       - Até 9 anos: MIRIM
#       - Até 14 anos: INFANTIL
#       - Até 19 anos: JÚNIOR
#       - Até 25 anos: SÊNIOR
#       - Acima de 25 anos: MASTER

from datetime import date
import os
os.system('cls')


ano = input('Digite o Ano de Nascimento: ')
atual = date.today().year
idade = atual - int(ano)

if idade < 10:
    print(f'IDADE: {idade}\nCATEGORIA: MIRIM')
elif idade < 15:
    print(f'IDADE: {idade}\nCATEGORIA:INFANTIL')
elif idade < 20:
    print(f'IDADE: {idade}\nCATEGORIA:JÚNIOR')
elif idade < 26:
    print(f'IDADE: {idade}\nCATEGORIA:SÊNIOR')
else:
    print(f'IDADE: {idade}\nCATEGORIA:MASTER')
