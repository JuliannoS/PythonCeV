'''Escreva um programa que leia dois números ineiros e compare-os
, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
-não existe valor maior, os dois são iguais'''

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))


if a > b:
    print('O 1º número é maior!')
elif b > a:
    print('O 2º número é maior!')
else:
    print('Os dois números são iguais!')
