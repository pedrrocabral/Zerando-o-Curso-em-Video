# <--   Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou
#       não com o nome "SANTO".

cidade = input('Qual Cidade Você Nasceu? ').strip()
# x = cidade.split()
# print(True if x[0].lower() == 'santo'else False)
print(cidade[:5].lower() == 'santo')