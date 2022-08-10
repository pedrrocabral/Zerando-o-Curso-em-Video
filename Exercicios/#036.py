# <--   Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a
#       compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos
#       ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
#       será negado.

casa = float(input('Qual o Valor da Casa? '))
salario = float(input('Qual seu salário? '))
tempo = int(input('Em quantos anos você deseja pagar? '))
meses = tempo * 12
prestacao = casa / meses

print(f'Empéstimo NEGADO! Valor da Prestação de R$ {prestacao:.2f} Está Muito Alto.'
      if prestacao > (salario * 0.30) else f'Empréstimo APROVADO! A Parcela Ficou no '
                                           f'Valor de R$ {prestacao:.2f}.')