# <--   Exercício Python 004: Faça um programa que leia algo pelo teclado
#       e mostre na tela o seu tipo primitivo e todas as informações
#       possíveis sobre ele.

x = input('Digite algo: ')
print(f'O tipo Primitivo Desse Item é: {type(x)}')
print('Só tem Espaços?', x.isspace())
print('É um Número?', x.isnumeric())
print('É Alfabético?', x.isalpha())
print('É Alfanúmerico? ', x.isalnum())
print('É Tudo Minúsculo?', x.islower())
print('É Tudo Maiúcula?', x.isupper())
print('É Tudo Capitalizada?', x.istitle())
