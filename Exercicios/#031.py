# <--   Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#       Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta
#       viagens mais longas.

trip = float(input('Qual é a distância da sua viagem? '))
print(f'O preço da sua passagem será de R$ {trip * 0.5:.2f}' if trip <= 200 else f'O preço da sua passagem será de '
                                                                                 f'R$ {trip * 0.45:.2f}')