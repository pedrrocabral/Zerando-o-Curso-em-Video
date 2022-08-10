# <--   Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#       de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

a = float(input('Digite o Cateto Oposto: '))
b = float(input('Digite o Cateto Adjacente: '))
c = ((a ** 2 + b ** 2) ** 0.5)
print(f'O Hipotenusa é: {c:.2f}')
