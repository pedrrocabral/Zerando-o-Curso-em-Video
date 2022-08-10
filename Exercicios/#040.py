# <--   Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
#       mostrando uma mensagem no final, de acordo com a média atingida:
#       - Média abaixo de 5.0: REPROVADO
#       - Média entre 5.0 e 6.9: RECUPERAÇÃO
#       - Média 7.0 ou superior: APROVADO

nota1 = int(input('Digite a 1ª Nota: '))
nota2 = int(input('Digite a 2ª Nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'A Média do Aluno Foi: {media}\nSITUAÇÂO: REPROVADO')
elif media < 7:
    print(f'A Média do Aluno Foi: {media}\nSITUAÇÂO: RECUPERAÇÂO')
else:
    print(f'A Média do Aluno Foi: {media}\nSITUAÇÂO: APROVADO')