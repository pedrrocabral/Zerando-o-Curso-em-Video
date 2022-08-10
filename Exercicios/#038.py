# <--   Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na
#       tela uma mensagem:
#       - O primeiro valor é maior
#       - O segundo valor é maior
#       - Não existe valor maior, os dois são iguais.

num1 = float(input('1º Número: '))
num2 = float(input('2º Número: '))

if num1 > num2:
    print('O Primeiro Valor É Maior')
elif num1 < num2:
    print('O Segundo Valor É Maior')
else:
    print('Não existe valor maior, os dois são iguais')