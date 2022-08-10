# <--   Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
#       considerando o seu preço normal e condição de pagamento:
#       - à vista dinheiro/cheque: 10% de desconto
#       - à vista no cartão: 5% de desconto
#       - em até 2x no cartão: preço formal
#       - 3x ou mais no cartão: 20% de juros

from os import system
system('cls')

print(3 * '-=-' + ' LOJAS CABRAL ' + 3 * '-=-')
valor = input('\nPreço das Compras: R$ ')
formas = input('''\n
FORMAS DE PAGAMENTO

[1] À VISTA DINHEIRO
[2] À VISTA CARTAO
[3] 2X NO CARTÃO
[4] MAIS FORMAS DE PARCELAMENTO

Qual Opcao Voce Deseja? ''')