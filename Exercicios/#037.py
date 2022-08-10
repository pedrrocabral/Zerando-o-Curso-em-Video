# <--   Exercício Python 037: Escreva um programa em Python que leia um número inteiro
#       qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário,
#       2 para octal e 3 para hexadecimal.

num = int(input('Digite Um Número Inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Escolha a Opção: '))

if opcao == 1:
    print(f'O número {num} convertido para binário é igual a: {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para octal é igual a: {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido para hexadecimal é igual a: {hex(num)[2:]}')
else:
    print('Opção Invalida ou Não Existente')