# <--   Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite Seu Nome Completo: ')
print(f'Seu Nome Tem Silva? {"silva" in nome.lower()}')
