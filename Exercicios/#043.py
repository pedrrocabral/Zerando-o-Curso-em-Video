# <--   Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#       calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#       - IMC abaixo de 18,5: Abaixo do Peso
#       - Entre 18,5 e 25: Peso Ideal
#       - 25 até 30: Sobrepeso
#       - 30 até 40: Obesidade
#       - Acima de 40: Obesidade Mórbida

from os import system
system('cls')

weigth = float(input('Insira Seu Peso: '))
high = input('Insira Sua Altura: ')
high = float(high) if '.' in high else float(high) / 100
imc = round(weigth / (high**2), 1)
print(f'IMC: {imc}', end=', ')
if imc < 18.5:
    print('Você Está Abaixo do Peso')
elif imc < 25:
    print('Você Está no Peso Ideal')
elif imc < 30:
    print('Você Está Com Sobrepeso')
elif imc < 40:
    print('Você Está Com Obesidade')
else:
    print('Você Está Com Obesidade Mórbida')