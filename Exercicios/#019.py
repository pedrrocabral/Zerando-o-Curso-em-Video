# <--   Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#       Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

x = input('Primeiro Aluno: ')
y = input('Segundo Aluno: ')
z = input('Terceiro Aluno: ')
w = input('Quarto Aluno: ')
lista = [x, y, z, w]
sorteado = random.choice(lista)
print(f'O Aluno Sorteado Foi: {str(sorteado)}')