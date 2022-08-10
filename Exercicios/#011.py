# <--   Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule
#       a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
#       área de 2 metros quadrados.

x = float(input('Largura da Parede: '))
y = float(input('Altura da Parede: '))
print(f'Área da Parede: {x * y:.2f}m² e Irá Ser Necessário {(x*y)/2:.2f}L de Linta')
