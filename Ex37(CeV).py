'''Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a nase de conversão
1 --> binário
2 --> octal
3 --> hexadecimal
'''

numero = int(input('Digite um numero: '))
print('''Escolha o modo de conversão:
[1] Binario
[2] Octal 
[3] Hexadecimal''')

escolha = int(input('Escolha: '))

if escolha == 1:
    print('{} Em binario é {}'.format(numero,bin(numero)[2:])) #0b para cortar isso por o [2:]
elif escolha == 2:
    print('{} Em octal é {}'.format(numero,oct(numero)[2:])) #0o
elif escolha == 3:
    print('{} Em hexadecimal é {}'.format(numero,hex(numero)[2:])) #0x
else:
    print('Você escolheu uma opção indisponível, repita.')