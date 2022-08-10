# <--   Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#       - O nome com todas as letras maiúsculas e minúsculas.
#       - Quantas letras ao todo (sem considerar espaços).
#       - Quantas letras tem o primeiro nome.

nome = input('Digite Seu Nome Completo: ').strip()
x = nome.split()
print('Analisando Seu Nome.....')
print(f'Seu Nome Em Maiusculo é: {nome.upper()}')
print(f'Seu Nome Em Minusculo é: {nome.lower()}')
print(f'Seu Nome Tem {len(nome) - nome.count(" ")} Letras')
print(f'Seu Primeiro Nome é {x[0]} e tem {len(x[0])} Letras')
