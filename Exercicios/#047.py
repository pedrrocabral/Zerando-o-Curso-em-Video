# <-- Exercício Python 047: Faça um programa que calcule a soma entre todos os
#       números que são múltiplos de três e impares e que se encontram no
#       intervalo de 1 até 500.

lista: list = []
for i in range(1, 501, 2):
    if i % 3 == 0:
        lista.append(i)

print(sum(lista))
