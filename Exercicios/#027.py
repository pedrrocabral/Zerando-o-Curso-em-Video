# <--   Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em
#       seguida o primeiro e o último nome separadamente.

nome = input('Digite Seu Nome Completo: ').strip().title()
print('Muito Prazer em te conhecer!'.title())
print(f'Seu Primeiro nome é: {nome[:nome.find(" ")]}')
print(f"Seu Ultimo Nome é: {nome[nome.rfind(' ') + 1:]}")
