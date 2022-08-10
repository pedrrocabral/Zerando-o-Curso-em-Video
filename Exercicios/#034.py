# <--   Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule
#       o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para
#       os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual seu salário? '))
print(f'Seu Salario com aumento de 10% ficou R$ {salario * 1.1:.2f}' if salario > 1250 else f'Seu Salario com '
                                                                                            f'aumento de 10% ficou '
                                                                                            f'R$ {salario * 1.15:.2f}')
