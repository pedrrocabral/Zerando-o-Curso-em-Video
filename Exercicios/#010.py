# <--   Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#       quantos dólares ela pode comprar.

x = float(input('Quanto Dinheiro Você tem na carteira? R$ '))
print(f'Com R$ {x} Você Pode Comprar U$ {x / 4.69:.2f}')
