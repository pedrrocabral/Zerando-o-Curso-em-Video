# <--   Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de
#       trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

x = input('Primeiro Aluno: ')
y = input('Segundo Aluno: ')
z = input('Terceiro Aluno: ')
w = input('Quarto Aluno: ')
lista = [x, y, z, w]
random.shuffle(lista)
print(f'A Ordem de Apresentação será:\n{lista}')