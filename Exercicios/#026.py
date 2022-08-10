# <--   Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
#       aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a
#       última vez.

x = input('Digite Uma Frase: ').lower().strip()
print(f'A lentra A apareceu {x.count("a")}')
print(f'A primeira letra A apareceu na posição numero: {x.find("a") + 1 }')
print(f'A primeira letra A apareceu na posição numero: {x.rfind("a") + 1 }')