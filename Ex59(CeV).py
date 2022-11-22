'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
sey programa deverá realizar a operação solicitada em cada caso.'''
a = 0
from time import sleep
print('Escolha dois numeros')
n1 = float(input('1º Valor: '))
n2 = float(input('2º Valor: '))
while a != 5:
    print('''O que fazer com os numeros ? 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa ''')
    a = int(input('---> Opção: '))
    print('-_-' * 20)
    if a == 1:
        print('Você escolheu a opção Somar')
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
        print('-_-' * 20)
    if a == 2:
        print('Você escolheu a opção Multiplicar')
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
        print('-_-' * 20)
    if a == 3:
        print('Você escolheu a opção Maior')
        maior = n1
        if n2 > n1:
            maior = n2
        if n1 == n2:
            maior = str('nenhum, os dois numeros são iguais!')
        print('Entre {} e {} o maior numero é {}'.format(n1, n2, maior))
        print('-_-' * 20)
    if a == 4:
        print('Você escolheu a opção Novos números')
        n1 = float(input('1º novo numero: '))
        n2 = float(input('2° novo numero: '))
        print('-_-' * 20)
    if a == 5:
        print('Desligando o codigo!')
    if (a == 0) or (a > 5):
        print('Opção invalida, tente novamente! ')
        print('-_-' * 20)
    sleep(1)
print('-_-' * 20)