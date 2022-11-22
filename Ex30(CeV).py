'''Crie um programa que leia um número inteiro e mostre na tela se é par ou impar'''

n = int(input("digite um numero: "))
p = n % 2 #divide e pega apenas o resto, 0 = par. 1 = impar
if p == 0 :
    print('O numero {} é par'.format(n))
else:
    print('O numero {} é impar'.format(n))