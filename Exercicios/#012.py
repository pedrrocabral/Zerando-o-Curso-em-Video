# <-- Exercício Python 012: Faça um algoritmo que leia o preço de um produto e
#       mostre seu novo preço, com 5% de desconto.

x = float(input('Qual o Valor do Produto? R$ '))
print(
    f'O Produto Custava R$ {x} e na Promoção de 5% Vai Custar Apenas R$ {x * 0.95:.2f}')
