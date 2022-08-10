# <--   Exercício Python 015: Escreva um programa que pergunte a quantidade
#       de Km percorridos por um carro alugado e a quantidade de dias pelos
#       quais ele foi alugado. Calcule o preço a pagar, sabendo que o
#       carro custa R$60 por dia e R$0,15 por Km rodado.

x = float(input('Quantos Dias Foi Alugado? '))
y = float(input('Quantos KM Foram Rodados? '))
print(f'O Valor do Aluguel do Veiculo é R$ {(x * 60) + (y * 0.15)}')
