# <-    Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#       80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km
#       acima do limite.

vel = int(input('Qual Velocidade do Carro? '))
print('Tenha um bom dia! Dirija com segurança!' if vel <= 80 else f'MULTADO! Você excedeu o limite de velocidade '
                                                               f'que é de 80km/h.\nVocê deve pagar uma multa de '
                                                               f'R$ {((vel - 80) * 7):.2f} ')
